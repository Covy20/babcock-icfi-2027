/**
 * 7th ICFI 2027 — Conference & ICFI Membership Web App (Google Apps Script)
 * ------------------------------------------------------------------------
 * Bound to Spreadsheet: "7th ICFI 2027 - Conference Registrations"
 * Spreadsheet ID: 1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q
 *
 * Deployment / Update steps:
 *   1. Open the spreadsheet -> Extensions -> Apps Script.
 *   2. Replace Code.gs with this file and click Save.
 *   3. If updating an existing deployment (keeps the SAME /exec URL):
 *      Deploy -> Manage deployments -> Edit (pencil) -> Version: New version -> Deploy.
 */

const CONFIG = {
  SPREADSHEET_ID: '1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q',
  SHEET_NAME: 'Registrations',
  MEMBERSHIP_SHEET_NAME: 'Membership',
  DRIVE_FOLDER_NAME: '7th ICFI 2027 - Uploaded Receipts & Proofs',
  MAX_FILE_BYTES: 10 * 1024 * 1024, // 10 MB per file (matches Google Form limit)
  SEND_CONFIRMATION_EMAIL: true,
  ADMIN_NOTIFY_EMAIL: '' // Optional: e.g. 'icfi@babcock.edu.ng'
};

function doGet() {
  return jsonOutput({
    ok: true,
    service: '7th ICFI 2027 Registration & Membership API',
    forms: ['conference', 'membership'],
    spreadsheetId: CONFIG.SPREADSHEET_ID
  });
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);

    if (!e || !e.postData || !e.postData.contents) {
      return jsonOutput({ ok: false, error: 'Empty request payload.' });
    }

    const data = JSON.parse(e.postData.contents);

    // Honeypot bot guard
    if (data.websiteUrl && String(data.websiteUrl).trim() !== '') {
      return jsonOutput({ ok: false, error: 'Submission rejected.' });
    }

    const ss = SpreadsheetApp.getActiveSpreadsheet() || SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);

    if (data.formType === 'membership') {
      return handleMembershipPost(ss, data);
    }
    return handleConferencePost(ss, data);
  } catch (err) {
    return jsonOutput({
      ok: false,
      error: err && err.message ? err.message : String(err)
    });
  } finally {
    lock.releaseLock();
  }
}

function handleConferencePost(ss, data) {
  const required = [
    'participantCategory',
    'participationMode',
    'registrationPeriod',
    'membershipStatus',
    'fullName',
    'email',
    'phone',
    'country',
    'amountPaid',
    'paymentDate',
    'accountHolderName'
  ];

  const missing = findMissingField(data, required);
  if (missing) {
    return jsonOutput({ ok: false, error: 'Missing required field: ' + missing });
  }

  if (data.declarationAgreed !== true && data.declarationAgreed !== 'Yes') {
    return jsonOutput({ ok: false, error: 'Declaration agreement is required.' });
  }

  if (!data.paymentReceipt || !data.paymentReceipt.base64) {
    return jsonOutput({ ok: false, error: 'Payment receipt upload is required.' });
  }

  if (data.membershipStatus === 'Registered Member' && (!data.membershipProof || !data.membershipProof.base64)) {
    return jsonOutput({ ok: false, error: 'Membership verification proof upload is required.' });
  }

  const sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
  if (!sheet) {
    return jsonOutput({ ok: false, error: 'Sheet "' + CONFIG.SHEET_NAME + '" not found.' });
  }

  const regId = generatePrefixedId(sheet, 'ICFI27-');
  const folder = getOrCreateReceiptsFolder();
  const safeNameSlug = sanitizeFileSlug(data.fullName);

  let membershipProofUrl = '';
  if (data.membershipProof && data.membershipProof.base64) {
    membershipProofUrl = saveUploadedFile(
      folder,
      data.membershipProof,
      regId + '_MemberProof_' + safeNameSlug
    );
  }

  const paymentReceiptUrl = saveUploadedFile(
    folder,
    data.paymentReceipt,
    regId + '_PaymentReceipt_' + safeNameSlug
  );

  const submittedAt = formatTimestamp(ss);
  const initialStatus = data.membershipStatus === 'New Member Applicant'
    ? 'Membership Pending'
    : 'Pending Verification';

  const row = [
    submittedAt,
    regId,
    safeCell(data.participantCategory),
    safeCell(data.participationMode),
    safeCell(data.registrationPeriod),
    safeCell(data.membershipStatus),
    membershipProofUrl,
    safeCell(data.currency || ''),
    safeCell(data.applicableFee || ''),
    safeCell(data.fullName),
    safeCell(data.email),
    forceTextCell(data.phone),
    safeCell(data.country),
    safeCell(data.stateOfResidence || ''),
    safeCell(data.organisation || ''),
    safeCell(data.designation || ''),
    safeCell(data.specialisation || ''),
    safeCell(data.amountPaid),
    forceTextCell(data.paymentDate),
    forceTextCell(data.transactionRef || ''),
    safeCell(data.accountHolderName),
    paymentReceiptUrl,
    'Yes',
    initialStatus
  ];

  sheet.appendRow(row);

  if (CONFIG.SEND_CONFIRMATION_EMAIL) {
    sendDelegateConfirmation(data, regId);
  }
  if (CONFIG.ADMIN_NOTIFY_EMAIL) {
    sendAdminNotification(
      '[ICFI 2027] New Registration: ' + data.fullName + ' (' + regId + ')',
      'Ref: ' + regId + '\nName: ' + data.fullName + '\nEmail: ' + data.email + '\nReceipt: ' + paymentReceiptUrl + '\nSheet: ' + ss.getUrl()
    );
  }

  return jsonOutput({
    ok: true,
    registrationId: regId,
    submittedAt: submittedAt,
    verificationStatus: initialStatus,
    receiptUrl: paymentReceiptUrl
  });
}

function handleMembershipPost(ss, data) {
  const required = [
    'fullName',
    'profession',
    'institutionalAddress',
    'cellPhone',
    'whatsappContact',
    'email',
    'registrationDate'
  ];

  const missing = findMissingField(data, required);
  if (missing) {
    return jsonOutput({ ok: false, error: 'Missing required field: ' + missing });
  }

  if (data.conditionsAgreed !== true && data.conditionsAgreed !== 'I agree' && data.conditionsAgreed !== 'Yes') {
    return jsonOutput({ ok: false, error: 'You must agree to the membership conditions to submit.' });
  }

  if (!data.paymentEvidence || !data.paymentEvidence.base64) {
    return jsonOutput({ ok: false, error: 'Evidence of membership payment is required.' });
  }

  const sheet = ss.getSheetByName(CONFIG.MEMBERSHIP_SHEET_NAME);
  if (!sheet) {
    return jsonOutput({ ok: false, error: 'Sheet "' + CONFIG.MEMBERSHIP_SHEET_NAME + '" not found.' });
  }

  const memberId = generatePrefixedId(sheet, 'ICFI-MEM-');
  const folder = getOrCreateReceiptsFolder();
  const safeNameSlug = sanitizeFileSlug(data.fullName);
  const evidenceUrl = saveUploadedFile(
    folder,
    data.paymentEvidence,
    memberId + '_MembershipPayment_' + safeNameSlug
  );

  const submittedAt = formatTimestamp(ss);
  const initialStatus = 'Pending Verification';

  const row = [
    submittedAt,
    memberId,
    'Yes',
    safeCell(data.fullName),
    safeCell(data.profession),
    safeCell(data.institutionalAddress),
    forceTextCell(data.cellPhone),
    forceTextCell(data.whatsappContact),
    safeCell(data.email),
    forceTextCell(data.registrationDate),
    safeCell(data.annualFee || 'US$5 / ₦7,000'),
    evidenceUrl,
    initialStatus
  ];

  sheet.appendRow(row);

  if (CONFIG.SEND_CONFIRMATION_EMAIL) {
    sendMembershipConfirmation(data, memberId);
  }
  if (CONFIG.ADMIN_NOTIFY_EMAIL) {
    sendAdminNotification(
      '[ICFI Membership] New Application: ' + data.fullName + ' (' + memberId + ')',
      'Ref: ' + memberId + '\nName: ' + data.fullName + '\nEmail: ' + data.email + '\nEvidence: ' + evidenceUrl + '\nSheet: ' + ss.getUrl()
    );
  }

  return jsonOutput({
    ok: true,
    membershipId: memberId,
    submittedAt: submittedAt,
    verificationStatus: initialStatus,
    evidenceUrl: evidenceUrl
  });
}

function findMissingField(data, required) {
  for (let i = 0; i < required.length; i++) {
    const key = required[i];
    if (!data[key] || String(data[key]).trim() === '') {
      return key;
    }
  }
  return '';
}

function formatTimestamp(ss) {
  return Utilities.formatDate(new Date(), ss.getSpreadsheetTimeZone() || 'Africa/Lagos', 'yyyy-MM-dd HH:mm:ss');
}

function getOrCreateReceiptsFolder() {
  const iter = DriveApp.getFoldersByName(CONFIG.DRIVE_FOLDER_NAME);
  if (iter.hasNext()) {
    return iter.next();
  }
  return DriveApp.createFolder(CONFIG.DRIVE_FOLDER_NAME);
}

function saveUploadedFile(folder, fileObj, baseLabel) {
  const bytes = Utilities.base64Decode(fileObj.base64);
  if (bytes.length > CONFIG.MAX_FILE_BYTES) {
    throw new Error('Uploaded file exceeds 10 MB limit: ' + (fileObj.name || baseLabel));
  }
  const origName = String(fileObj.name || 'upload.bin');
  const dotIdx = origName.lastIndexOf('.');
  const ext = dotIdx > -1 ? origName.slice(dotIdx).replace(/[^a-zA-Z0-9.]/g, '') : '';
  const finalName = baseLabel + ext;
  const mimeType = String(fileObj.mimeType || 'application/octet-stream');
  const blob = Utilities.newBlob(bytes, mimeType, finalName);
  const file = folder.createFile(blob);
  return file.getUrl();
}

function generatePrefixedId(sheet, prefix) {
  const seq = String(Math.max(1, sheet.getLastRow())).padStart(4, '0');
  const rand = Math.random().toString(36).substring(2, 6).toUpperCase();
  return prefix + seq + '-' + rand;
}

function sanitizeFileSlug(text) {
  return String(text || 'Delegate')
    .trim()
    .replace(/[^a-zA-Z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '')
    .slice(0, 40) || 'Delegate';
}

function safeCell(val) {
  const str = String(val === undefined || val === null ? '' : val).trim();
  if (/^[=@+\-\t\r]/.test(str)) {
    return "'" + str;
  }
  return str;
}

function forceTextCell(val) {
  const str = String(val === undefined || val === null ? '' : val).trim();
  return str ? "'" + str : '';
}

function sendDelegateConfirmation(data, regId) {
  try {
    const subject = '7th ICFI 2027 Registration Received — ' + regId;
    const body = [
      'Dear ' + data.fullName + ',',
      '',
      'Thank you for submitting your registration for the 7th International Conference for Faith Integration (ICFI 2027), Babcock University (July 27 – August 1, 2027).',
      '',
      'Registration Reference: ' + regId,
      'Category: ' + data.participantCategory,
      'Participation Mode: ' + data.participationMode,
      'Membership Status: ' + data.membershipStatus,
      'Applicable Fee: ' + data.applicableFee,
      'Amount Paid Reported: ' + data.amountPaid,
      'Payment Date: ' + data.paymentDate,
      '',
      'Your registration and uploaded payment receipt have been logged for verification by the Conference Organising Committee.',
      '',
      'For inquiries or accommodation arrangements (Dr. Nnenna Nwobi: +2348135388049; Registration desk: Miss Deborah Caleb, 08064007567), contact icfi@babcock.edu.ng.',
      '',
      'Warm regards,',
      '7th ICFI 2027 Secretariat'
    ].join('\n');

    MailApp.sendEmail({
      to: String(data.email).trim(),
      subject: subject,
      body: body
    });
  } catch (mailErr) {}
}

function sendMembershipConfirmation(data, memberId) {
  try {
    const subject = 'ICFI Membership Application Received — ' + memberId;
    const body = [
      'Dear ' + data.fullName + ',',
      '',
      'Thank you for applying to join the International Community for Faith Integration (ICFI).',
      '',
      'Membership Application Reference: ' + memberId,
      'Profession: ' + data.profession,
      'Institution: ' + data.institutionalAddress,
      'Registration Date: ' + data.registrationDate,
      '',
      'Your application and payment evidence have been logged for verification. Once verified, you retain membership voting rights and ICFI conference fee concessions (₦10,000 off standard conference fee).',
      '',
      'Warm regards,',
      'International Community for Faith Integration (ICFI)'
    ].join('\n');

    MailApp.sendEmail({
      to: String(data.email).trim(),
      subject: subject,
      body: body
    });
  } catch (mailErr) {}
}

function sendAdminNotification(subject, body) {
  try {
    MailApp.sendEmail({
      to: CONFIG.ADMIN_NOTIFY_EMAIL,
      subject: subject,
      body: body
    });
  } catch (e) {}
}

function jsonOutput(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
