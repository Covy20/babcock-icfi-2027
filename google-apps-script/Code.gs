/**
 * 7th ICFI 2027 — Conference Registration Web App (Google Apps Script)
 * -------------------------------------------------------------------
 * Bound to Spreadsheet: "7th ICFI 2027 - Conference Registrations"
 * Spreadsheet ID: 1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q
 *
 * Deployment steps:
 *   1. Open the spreadsheet -> Extensions -> Apps Script.
 *   2. Replace Code.gs with this file and save.
 *   3. Deploy -> New deployment -> Type: Web app
 *      - Execute as: Me (your Google account)
 *      - Who has access: Anyone
 *   4. Copy the Web app URL (ends with /exec) into REGISTRATION_ENDPOINT in index.html.
 */

const CONFIG = {
  SPREADSHEET_ID: '1fcFFE9HhvhhrbAhNqyhgaSSukuKprC0aa9EDQfYq79Q',
  SHEET_NAME: 'Registrations',
  DRIVE_FOLDER_NAME: '7th ICFI 2027 - Uploaded Receipts & Proofs',
  MAX_FILE_BYTES: 10 * 1024 * 1024, // 10 MB per file (matches Google Form limit)
  SEND_CONFIRMATION_EMAIL: true,
  ADMIN_NOTIFY_EMAIL: '' // Optional: e.g. 'icfi@babcock.edu.ng'
};

function doGet() {
  return jsonOutput({
    ok: true,
    service: '7th ICFI 2027 Registration Portal API',
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

    for (let i = 0; i < required.length; i++) {
      const key = required[i];
      if (!data[key] || String(data[key]).trim() === '') {
        return jsonOutput({ ok: false, error: 'Missing required field: ' + key });
      }
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

    const ss = SpreadsheetApp.getActiveSpreadsheet() || SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    const sheet = ss.getSheetByName(CONFIG.SHEET_NAME);
    if (!sheet) {
      return jsonOutput({ ok: false, error: 'Sheet "' + CONFIG.SHEET_NAME + '" not found.' });
    }

    const regId = generateRegistrationId(sheet);
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

    const submittedAt = Utilities.formatDate(new Date(), ss.getSpreadsheetTimeZone() || 'Africa/Lagos', 'yyyy-MM-dd HH:mm:ss');
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
      sendDelegateConfirmation(data, regId, paymentReceiptUrl);
    }
    if (CONFIG.ADMIN_NOTIFY_EMAIL) {
      sendAdminNotification(data, regId, ss.getUrl(), paymentReceiptUrl);
    }

    return jsonOutput({
      ok: true,
      registrationId: regId,
      submittedAt: submittedAt,
      verificationStatus: initialStatus,
      receiptUrl: paymentReceiptUrl
    });
  } catch (err) {
    return jsonOutput({
      ok: false,
      error: err && err.message ? err.message : String(err)
    });
  } finally {
    lock.releaseLock();
  }
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

function generateRegistrationId(sheet) {
  const seq = String(Math.max(1, sheet.getLastRow())).padStart(4, '0');
  const rand = Math.random().toString(36).substring(2, 6).toUpperCase();
  return 'ICFI27-' + seq + '-' + rand;
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

function sendDelegateConfirmation(data, regId, receiptUrl) {
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
  } catch (mailErr) {
    // Non-fatal if MailApp daily quota is unavailable
  }
}

function sendAdminNotification(data, regId, sheetUrl, receiptUrl) {
  try {
    MailApp.sendEmail({
      to: CONFIG.ADMIN_NOTIFY_EMAIL,
      subject: '[ICFI 2027] New Registration: ' + data.fullName + ' (' + regId + ')',
      body: 'New registration received:\n\n'
        + 'Ref: ' + regId + '\n'
        + 'Name: ' + data.fullName + '\n'
        + 'Email: ' + data.email + '\n'
        + 'Phone: ' + data.phone + '\n'
        + 'Category: ' + data.participantCategory + ' / ' + data.participationMode + '\n'
        + 'Amount Paid: ' + data.amountPaid + '\n'
        + 'Receipt: ' + receiptUrl + '\n'
        + 'Spreadsheet: ' + sheetUrl
    });
  } catch (e) {}
}

function jsonOutput(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
