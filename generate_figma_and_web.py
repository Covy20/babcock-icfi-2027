import os

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 6120" width="1440" height="6120" fill="none">
  <defs>
    <linearGradient id="bg_hero_grad" x1="0" y1="0" x2="1440" y2="980" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#040D1A"/>
      <stop offset="50%" stop-color="#091D38"/>
      <stop offset="100%" stop-color="#051122"/>
    </linearGradient>
    <linearGradient id="gold_grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="50%" stop-color="#FBBF24"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <linearGradient id="card_grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0E2547"/>
      <stop offset="100%" stop-color="#08172E"/>
    </linearGradient>
    <linearGradient id="card_elevated_grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#173768"/>
      <stop offset="100%" stop-color="#0B1F3F"/>
    </linearGradient>
    <linearGradient id="blue_banner_grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0F2D59"/>
      <stop offset="100%" stop-color="#081832"/>
    </linearGradient>
  </defs>

  <!-- MASTER CANVAS BACKGROUND -->
  <rect id="Master_Background" x="0" y="0" width="1440" height="6120" fill="#051020"/>

  <!-- ================================================================= -->
  <!-- 1. TOP ANNOUNCEMENT BAR & NAVBAR (y = 0..116)                     -->
  <!-- ================================================================= -->
  <g id="01_Header_Navigation">
    <rect id="Top_Announcement_Bar" x="0" y="0" width="1440" height="36" fill="url(#gold_grad)"/>
    <text x="720" y="23" fill="#040D1A" font-family="Inter, sans-serif" font-size="12" font-weight="800" text-anchor="middle" letter-spacing="1.2">★ OFFICIAL CALL FOR PAPERS &amp; PARTICIPATION • 7TH BIENNIAL CONFERENCE • HYBRID FORMAT (PHYSICAL &amp; ONLINE) ★</text>

    <rect id="Navbar_Surface" x="0" y="36" width="1440" height="80" fill="#071529" stroke="#1E3A5F" stroke-width="1"/>
    
    <!-- Dual Institutional Logos -->
    <rect id="PHOTO_LOGO_ICFI" x="64" y="52" width="48" height="48" rx="24" fill="#102A4C" stroke="#F59E0B" stroke-width="2"/>
    <rect id="PHOTO_LOGO_BU" x="122" y="54" width="46" height="44" rx="8" fill="#102A4C" stroke="#334155" stroke-width="1"/>
    <text x="180" y="72" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="0.8">ICFI 2027 • 7TH EDITION</text>
    <text x="180" y="90" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="500">Babcock University, Nigeria</text>

    <!-- Nav Menu Items -->
    <g id="Navbar_Links">
      <text x="450" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">About</text>
      <text x="515" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">8 Fields</text>
      <text x="595" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">Speakers</text>
      <text x="682" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">Schedule</text>
      <text x="768" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">Pricing</text>
      <text x="840" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">IJFI Journal</text>
      <text x="942" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">Papers</text>
      <text x="1012" y="81" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="13" font-weight="600">Gallery</text>
    </g>

    <!-- Nav CTA Buttons -->
    <rect id="Btn_Nav_Abstract" x="1090" y="56" width="130" height="40" rx="10" fill="#0D2240" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="1155" y="81" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Submit Abstract</text>

    <rect id="Btn_Nav_Register" x="1232" y="56" width="144" height="40" rx="10" fill="url(#gold_grad)"/>
    <text x="1304" y="81" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Reserve A Seat →</text>
  </g>

  <!-- ================================================================= -->
  <!-- 2. PINTEREST-INSPIRED SPLIT HERO & COUNTDOWN (y = 116..980)       -->
  <!-- ================================================================= -->
  <g id="02_Hero_Section">
    <rect id="Hero_Backdrop" x="0" y="116" width="1440" height="864" fill="url(#bg_hero_grad)"/>
    <rect id="PHOTO_HERO_BG" x="0" y="116" width="1440" height="864" fill="#091D38" opacity="0.22"/>

    <!-- Left Column: Headline, Theme, Logistics, CTAs -->
    <g id="Hero_Left_Column">
      <rect x="64" y="168" width="430" height="34" rx="17" fill="#112A4E" stroke="#F59E0B" stroke-width="1.2"/>
      <circle cx="84" cy="185" r="5" fill="#FBBF24"/>
      <text x="98" y="190" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" letter-spacing="1">OFFICIAL CALL FOR PAPERS &amp; PARTICIPATION</text>

      <text x="64" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="56" font-weight="900" letter-spacing="-1">7TH INTERNATIONAL</text>
      <text x="64" y="334" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="56" font-weight="900" letter-spacing="-1">CONFERENCE FOR</text>
      <text x="64" y="400" fill="#FBBF24" font-family="Inter, sans-serif" font-size="56" font-weight="900" letter-spacing="-1">FAITH INTEGRATION</text>

      <!-- Theme Card -->
      <rect id="Hero_Theme_Box" x="64" y="432" width="660" height="120" rx="18" fill="#0B2140" stroke="#F59E0B" stroke-width="1.5"/>
      <rect x="64" y="432" width="8" height="120" rx="4" fill="#F59E0B"/>
      <text x="92" y="464" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" letter-spacing="1.5">CONFERENCE THEME</text>
      <text x="92" y="496" fill="#FFFFFF" font-family="Georgia, serif" font-size="22" font-weight="700">“Driving a Sustainable Faith-Based Ecosystem</text>
      <text x="92" y="526" fill="#FFFFFF" font-family="Georgia, serif" font-size="22" font-weight="700">in a Changing World”</text>

      <!-- Event Logistics Pills -->
      <rect x="64" y="576" width="210" height="42" rx="10" fill="#0E2547" stroke="#264673" stroke-width="1"/>
      <text x="82" y="602" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800">DATE:</text>
      <text x="126" y="602" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="12" font-weight="600">July 27 – Aug 1, 2027</text>

      <rect x="286" y="576" width="210" height="42" rx="10" fill="#0E2547" stroke="#264673" stroke-width="1"/>
      <text x="304" y="602" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800">MODE:</text>
      <text x="352" y="602" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="12" font-weight="600">Hybrid (In-Person/Online)</text>

      <rect x="508" y="576" width="216" height="42" rx="10" fill="#0E2547" stroke="#264673" stroke-width="1"/>
      <text x="524" y="602" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800">VENUE:</text>
      <text x="576" y="602" fill="#F8FAFC" font-family="Inter, sans-serif" font-size="12" font-weight="600">Babcock Univ., Nigeria</text>

      <!-- Hero CTA Buttons -->
      <rect id="Hero_CTA_Primary" x="64" y="644" width="240" height="56" rx="14" fill="url(#gold_grad)"/>
      <text x="184" y="677" fill="#051020" font-family="Inter, sans-serif" font-size="15" font-weight="800" text-anchor="middle">Reserve Your Seat →</text>

      <rect id="Hero_CTA_Secondary" x="320" y="644" width="404" height="56" rx="14" fill="#0B2140" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="522" y="677" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Submit Abstract: icfi@babcock.edu.ng</text>

      <!-- Pinterest-Style Live Countdown Timer Bar -->
      <rect id="Countdown_Container" x="64" y="732" width="660" height="112" rx="18" fill="#081933" stroke="#1E3A5F" stroke-width="1.5"/>
      <text x="92" y="762" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="700" letter-spacing="1.2">COUNTDOWN TO CONFERENCE OPENING (JULY 27, 2027)</text>
      
      <rect x="92" y="776" width="136" height="52" rx="10" fill="#0D2547" stroke="#F59E0B" stroke-width="1"/>
      <text x="142" y="809" fill="#FBBF24" font-family="Inter, sans-serif" font-size="24" font-weight="900" text-anchor="middle">253</text>
      <text x="192" y="807" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="700">DAYS</text>

      <rect x="244" y="776" width="136" height="52" rx="10" fill="#0D2547" stroke="#264673" stroke-width="1"/>
      <text x="292" y="809" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="900" text-anchor="middle">14</text>
      <text x="338" y="807" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="700">HRS</text>

      <rect x="396" y="776" width="136" height="52" rx="10" fill="#0D2547" stroke="#264673" stroke-width="1"/>
      <text x="444" y="809" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="900" text-anchor="middle">48</text>
      <text x="490" y="807" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="700">MINS</text>

      <rect x="548" y="776" width="148" height="52" rx="10" fill="#0D2547" stroke="#264673" stroke-width="1"/>
      <text x="596" y="809" fill="#FBBF24" font-family="Inter, sans-serif" font-size="24" font-weight="900" text-anchor="middle">35</text>
      <text x="646" y="807" fill="#94A3B8" font-family="Inter, sans-serif" font-size="11" font-weight="700">SECS</text>

      <!-- Social Proof Micro-Strip -->
      <text x="64" y="886" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="600">✓ Free IJFI Peer-Reviewed Publication   •   ✓ ₦10,000 Off for Registered Community Members</text>
    </g>

    <!-- Right Column: Bento Photo & Highlights Showcase -->
    <g id="Hero_Right_Bento">
      <rect id="Hero_Photo_Card_Frame" x="764" y="168" width="612" height="460" rx="24" fill="#0B2140" stroke="#F59E0B" stroke-width="2"/>
      <rect id="PHOTO_GROUP_DELEGATION" x="780" y="184" width="580" height="376" rx="16" fill="#102A4C"/>
      <rect x="780" y="572" width="580" height="40" rx="10" fill="#061325"/>
      <text x="1070" y="597" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">THE INTERNATIONAL COMMUNITY FOR FAITH INTEGRATION • BABCOCK UNIVERSITY</text>

      <!-- Two Bento Metric Cards Below Photo -->
      <rect id="Hero_Bento_Card_1" x="764" y="648" width="296" height="196" rx="20" fill="url(#card_grad)" stroke="#264673" stroke-width="1.5"/>
      <text x="792" y="692" fill="#FBBF24" font-family="Inter, sans-serif" font-size="36" font-weight="900">8 FIELDS</text>
      <text x="792" y="724" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="700">Multidisciplinary Tracks</text>
      <text x="792" y="754" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Science, Arts, Tech, Leadership,</text>
      <text x="792" y="776" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Business, Institutions, Religion</text>
      <text x="792" y="798" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">&amp; Public Policy.</text>

      <rect id="Hero_Bento_Card_2" x="1080" y="648" width="296" height="196" rx="20" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="1108" y="692" fill="#FBBF24" font-family="Inter, sans-serif" font-size="36" font-weight="900">IJFI FREE</text>
      <text x="1108" y="724" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="700">Journal Publication</text>
      <text x="1108" y="754" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">Accepted papers are published</text>
      <text x="1108" y="776" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">free in the International Journal</text>
      <text x="1108" y="798" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">for Faith Integration.</text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 3. PINTEREST-STYLE GOLD MARQUEE RIBBON (y = 980..1036)            -->
  <!-- ================================================================= -->
  <g id="03_Marquee_Ticker_Ribbon">
    <rect x="0" y="980" width="1440" height="56" fill="url(#gold_grad)"/>
    <text x="720" y="1014" fill="#051020" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle" letter-spacing="2">★ SCIENCE ★ ARTS &amp; HUMANITIES ★ TECHNOLOGY ★ LEADERSHIP ★ BUSINESS ★ INSTITUTIONS ★ RELIGION ★ POLITICS &amp; POLICY ★</text>
  </g>

  <!-- ================================================================= -->
  <!-- 4. ABOUT THE CONFERENCE & INSTITUTIONAL PILLARS (y = 1036..1740)  -->
  <!-- ================================================================= -->
  <g id="04_About_And_Vision_Section">
    <rect x="0" y="1036" width="1440" height="704" fill="#071529"/>

    <text x="64" y="1108" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="2">// ABOUT THE CONFERENCE &amp; INSTITUTIONAL MANDATE</text>
    <text x="64" y="1152" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="36" font-weight="900">Holistic Development of Human Capacity Through Faith</text>
    
    <text x="64" y="1196" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="15" font-weight="400">The International Conference for Faith Integration is organized by the Institute for Faith Integration, domiciled in the Office</text>
    <text x="64" y="1222" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="15" font-weight="400">of Institutional Effectiveness at Babcock University. As a Seventh-day Adventist institution with a unique educational perspective,</text>
    <text x="64" y="1248" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="15" font-weight="400">integrating biblical truth across every academic discipline and profession fulfills the prophetic mandate of Isaiah 58:12.</text>

    <!-- 3 Institutional Pillar Cards (Vision, Mission, Core Values) -->
    <rect id="Card_Vision" x="64" y="1288" width="400" height="184" rx="18" fill="url(#card_grad)" stroke="#1E3A5F" stroke-width="1.5"/>
    <rect x="88" y="1312" width="140" height="26" rx="6" fill="#112A4E"/>
    <text x="158" y="1329" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">VISION STATEMENT</text>
    <text x="88" y="1368" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="700">First-Class Adventist Institution</text>
    <text x="88" y="1398" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">“A first-class Seventh-day Adventist</text>
    <text x="88" y="1420" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">institution, building servant-leaders</text>
    <text x="88" y="1442" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">for a better world.”</text>

    <rect id="Card_Mission" x="484" y="1288" width="400" height="184" rx="18" fill="url(#card_grad)" stroke="#1E3A5F" stroke-width="1.5"/>
    <rect x="508" y="1312" width="148" height="26" rx="6" fill="#112A4E"/>
    <text x="582" y="1329" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">MISSION STATEMENT</text>
    <text x="508" y="1368" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="700">Transforming Lives &amp; Society</text>
    <text x="508" y="1398" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Building leadership through Christian</text>
    <text x="508" y="1420" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">education; excellence in teaching,</text>
    <text x="508" y="1442" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">research programs, and Christ-like service.</text>

    <!-- Core Values Strip -->
    <rect id="Card_Core_Values" x="64" y="1496" width="820" height="180" rx="18" fill="#0B2140" stroke="#264673" stroke-width="1.5"/>
    <text x="92" y="1534" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.5">BABCOCK UNIVERSITY CORE VALUES</text>
    <text x="92" y="1570" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">• Excellence (Our Culture)      • Integrity (Our Promise)      • Accountability (Our Moral)</text>
    <text x="92" y="1602" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">• Team Spirit (Our Strength)   • Servant Leadership (Our Dignity)</text>
    <text x="92" y="1634" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="700">• Autonomy &amp; Responsibility (Our Passion)   • Adventist Heritage (Our Commitment!)</text>

    <!-- Right Convener Spotlight Card -->
    <rect id="Convener_Spotlight_Card" x="912" y="1108" width="464" height="568" rx="24" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="2"/>
    <rect id="PHOTO_CONVENER_ABOUT" x="944" y="1140" width="400" height="280" rx="16" fill="#102A4C"/>
    <rect x="944" y="1440" width="190" height="28" rx="14" fill="url(#gold_grad)"/>
    <text x="1039" y="1458" fill="#051020" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">ORGANIZER &amp; CONVENER</text>
    <text x="944" y="1498" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="800">Prof. Constance C. Nwosu</text>
    <text x="944" y="1524" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="600">Associate Vice President, Institutional Effectiveness</text>
    <text x="944" y="1558" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="400">“Through this conference, where participants are drawn</text>
    <text x="944" y="1580" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="400">from within and outside the country, we advance the</text>
    <text x="944" y="1602" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="400">frontiers of faith-based ecosystems globally.”</text>
    <text x="944" y="1644" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="700">Direct Lines: +(234) 8064638207 • +(234) 8058299031</text>
  </g>

  <!-- ================================================================= -->
  <!-- 5. EXPLORE EIGHT FIELDS OF FAITH INTEGRATION (y = 1740..2420)     -->
  <!-- ================================================================= -->
  <g id="05_Eight_Fields_Of_Faith_Integration">
    <rect x="0" y="1740" width="1440" height="680" fill="#051020"/>
    
    <line x1="280" y1="1808" x2="440" y2="1808" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="720" y="1813" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="2.5">EXPLORE EIGHT FIELDS OF FAITH INTEGRATION</text>
    <line x1="1000" y1="1808" x2="1160" y2="1808" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="720" y="1852" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="34" font-weight="900" text-anchor="middle">Interdisciplinary Conference Tracks &amp; Sub-Themes</text>

    <!-- Row 1 of 4 Track Cards -->
    <!-- Track 1: SCIENCE -->
    <g id="Track_01_Science">
      <rect x="64" y="1896" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="64" y="1924" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="92" y="1920" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="114" y="1941" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">01</text>
      <text x="92" y="1984" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">SCIENCE</text>
      <text x="92" y="2016" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Creation care, environmental</text>
      <text x="92" y="2038" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">stewardship, bioethics, medical</text>
      <text x="92" y="2060" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">practice &amp; empirical inquiry.</text>
    </g>

    <!-- Track 2: ARTS & HUMANITIES -->
    <g id="Track_02_Arts">
      <rect x="396" y="1896" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="396" y="1924" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="424" y="1920" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="446" y="1941" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">02</text>
      <text x="424" y="1984" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">ARTS &amp; HUMANITIES</text>
      <text x="424" y="2016" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Literature, history, reading</text>
      <text x="424" y="2038" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">culture, communication, music</text>
      <text x="424" y="2060" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">&amp; cultural heritage.</text>
    </g>

    <!-- Track 3: TECHNOLOGY -->
    <g id="Track_03_Technology">
      <rect x="728" y="1896" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="728" y="1924" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="756" y="1920" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="778" y="1941" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">03</text>
      <text x="756" y="1984" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">TECHNOLOGY</text>
      <text x="756" y="2016" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Artificial Intelligence, social</text>
      <text x="756" y="2038" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">media ethics, digital innovation</text>
      <text x="756" y="2060" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">&amp; cyber responsibility.</text>
    </g>

    <!-- Track 4: LEADERSHIP -->
    <g id="Track_04_Leadership">
      <rect x="1060" y="1896" width="316" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="1060" y="1924" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="1088" y="1920" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="1110" y="1941" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">04</text>
      <text x="1088" y="1984" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">LEADERSHIP</text>
      <text x="1088" y="2016" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Servant leadership, ethical</text>
      <text x="1088" y="2038" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">administration, mentorship &amp;</text>
      <text x="1088" y="2060" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">capacity building.</text>
    </g>

    <!-- Row 2 of 4 Track Cards -->
    <!-- Track 5: BUSINESS -->
    <g id="Track_05_Business">
      <rect x="64" y="2136" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="64" y="2164" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="92" y="2160" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="114" y="2181" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">05</text>
      <text x="92" y="2224" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">BUSINESS</text>
      <text x="92" y="2256" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Entrepreneurial innovation,</text>
      <text x="92" y="2278" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">economic growth, internal audit</text>
      <text x="92" y="2300" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">&amp; Christian stewardship.</text>
    </g>

    <!-- Track 6: INSTITUTIONS -->
    <g id="Track_06_Institutions">
      <rect x="396" y="2136" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="396" y="2164" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="424" y="2160" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="446" y="2181" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">06</text>
      <text x="424" y="2224" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">INSTITUTIONS</text>
      <text x="424" y="2256" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Innovative quality education</text>
      <text x="424" y="2278" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">management, curriculum design</text>
      <text x="424" y="2300" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">&amp; compliance functions.</text>
    </g>

    <!-- Track 7: RELIGION -->
    <g id="Track_07_Religion">
      <rect x="728" y="2136" width="312" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="728" y="2164" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="756" y="2160" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="778" y="2181" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">07</text>
      <text x="756" y="2224" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">RELIGION</text>
      <text x="756" y="2256" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Multicultural evangelism, faith</text>
      <text x="756" y="2278" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">traditions, biblical ethics &amp;</text>
      <text x="756" y="2300" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">discipleship in modern society.</text>
    </g>

    <!-- Track 8: POLITICS & POLICY -->
    <g id="Track_08_Politics">
      <rect x="1060" y="2136" width="316" height="216" rx="18" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="1060" y="2164" width="8" height="48" rx="4" fill="#F59E0B"/>
      <rect x="1088" y="2160" width="44" height="32" rx="8" fill="#14325C"/>
      <text x="1110" y="2181" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">08</text>
      <text x="1088" y="2224" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="19" font-weight="800">POLITICS &amp; POLICY</text>
      <text x="1088" y="2256" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Faith-driven governance, social</text>
      <text x="1088" y="2278" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">justice, relational principles &amp;</text>
      <text x="1088" y="2300" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">nation building.</text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 6. HOSTS, CHIEF HOST & KEYNOTE SPEAKERS (y = 2420..3460)          -->
  <!-- ================================================================= -->
  <g id="06_Speakers_And_Leadership_Showcase">
    <rect x="0" y="2420" width="1440" height="1040" fill="#071529"/>

    <text x="720" y="2484" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" text-anchor="middle" letter-spacing="2">// CONFERENCE LEADERSHIP &amp; DISTINGUISHED KEYNOTE SPEAKERS</text>
    <text x="720" y="2528" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="36" font-weight="900" text-anchor="middle">Chief Host, Host, Convener &amp; Featured Speakers</text>

    <!-- Row 1: 3 Executive Host Cards -->
    <!-- Chief Host: Prof. Ademola Tayo -->
    <g id="Speaker_Chief_Host_Tayo">
      <rect x="64" y="2568" width="416" height="410" rx="22" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="2"/>
      <rect id="PHOTO_SPEAKER_VC" x="88" y="2592" width="368" height="250" rx="14" fill="#102A4C"/>
      <rect x="88" y="2860" width="124" height="26" rx="13" fill="url(#gold_grad)"/>
      <text x="150" y="2877" fill="#051020" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">CHIEF HOST</text>
      <text x="88" y="2914" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="22" font-weight="800">Prof. Ademola Tayo</text>
      <text x="88" y="2940" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="600">President / Vice Chancellor</text>
      <text x="88" y="2962" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Babcock University, Ilishan-Remo, Nigeria</text>
    </g>

    <!-- Host: Prof. Philemon Amanze -->
    <g id="Speaker_Host_Amanze">
      <rect x="512" y="2568" width="416" height="410" rx="22" fill="url(#card_grad)" stroke="#264673" stroke-width="1.5"/>
      <rect id="PHOTO_SPEAKER_AMANZE" x="536" y="2592" width="368" height="250" rx="14" fill="#102A4C"/>
      <rect x="536" y="2860" width="90" height="26" rx="13" fill="#14325C" stroke="#F59E0B" stroke-width="1"/>
      <text x="581" y="2877" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">HOST</text>
      <text x="536" y="2914" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="22" font-weight="800">Prof. Philemon Amanze</text>
      <text x="536" y="2940" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="600">Senior Vice President</text>
      <text x="536" y="2962" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Babcock University, Ilishan-Remo, Nigeria</text>
    </g>

    <!-- Convener: Prof. Constance C. Nwosu -->
    <g id="Speaker_Convener_Nwosu">
      <rect x="960" y="2568" width="416" height="410" rx="22" fill="url(#card_grad)" stroke="#264673" stroke-width="1.5"/>
      <rect id="PHOTO_SPEAKER_NWOSU" x="984" y="2592" width="368" height="250" rx="14" fill="#102A4C"/>
      <rect x="984" y="2860" width="184" height="26" rx="13" fill="#14325C" stroke="#F59E0B" stroke-width="1"/>
      <text x="1076" y="2877" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">ORGANIZER / CONVENER</text>
      <text x="984" y="2914" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="22" font-weight="800">Prof. Constance C. Nwosu</text>
      <text x="984" y="2940" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="600">AVP, Institutional Effectiveness</text>
      <text x="984" y="2962" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Institute for Faith Integration, Babcock University</text>
    </g>

    <!-- Row 2: 4 International Keynote & Invited Speakers -->
    <!-- Speaker 4: Prof. John Wesley Taylor V -->
    <g id="Speaker_Keynote_Taylor">
      <rect x="64" y="3010" width="312" height="390" rx="20" fill="url(#card_grad)" stroke="#F59E0B" stroke-width="1.2"/>
      <rect id="PHOTO_SPEAKER_TAYLOR" x="84" y="3030" width="272" height="210" rx="12" fill="#102A4C"/>
      <rect x="84" y="3256" width="144" height="24" rx="12" fill="url(#gold_grad)"/>
      <text x="156" y="3272" fill="#051020" font-family="Inter, sans-serif" font-size="10" font-weight="800" text-anchor="middle">KEYNOTE SPEAKER</text>
      <text x="84" y="3304" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="17" font-weight="800">Prof. John Wesley Taylor V</text>
      <text x="84" y="3328" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="500">Associate Director of Education,</text>
      <text x="84" y="3348" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">General Conference of SDA (USA)</text>
    </g>

    <!-- Speaker 5: Dr. Juvenal Balisasa -->
    <g id="Speaker_Invited_Balisasa">
      <rect x="396" y="3010" width="312" height="390" rx="20" fill="url(#card_grad)" stroke="#264673" stroke-width="1.2"/>
      <rect id="PHOTO_SPEAKER_BALISASA" x="416" y="3030" width="272" height="210" rx="12" fill="#102A4C"/>
      <rect x="416" y="3256" width="136" height="24" rx="12" fill="#14325C"/>
      <text x="484" y="3272" fill="#FBBF24" font-family="Inter, sans-serif" font-size="10" font-weight="800" text-anchor="middle">INVITED SPEAKER</text>
      <text x="416" y="3304" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="17" font-weight="800">Dr. Juvenal Balisasa, Ph.D</text>
      <text x="416" y="3328" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="500">Education Director, West-Central</text>
      <text x="416" y="3348" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Africa Division (Côte d'Ivoire)</text>
    </g>

    <!-- Speaker 6: Mrs. Barbara Fisher -->
    <g id="Speaker_Invited_Barbara">
      <rect x="728" y="3010" width="312" height="390" rx="20" fill="url(#card_grad)" stroke="#264673" stroke-width="1.2"/>
      <rect id="PHOTO_SPEAKER_BARBARA" x="748" y="3030" width="272" height="210" rx="12" fill="#102A4C"/>
      <rect x="748" y="3256" width="136" height="24" rx="12" fill="#14325C"/>
      <text x="816" y="3272" fill="#FBBF24" font-family="Inter, sans-serif" font-size="10" font-weight="800" text-anchor="middle">INVITED SPEAKER</text>
      <text x="748" y="3304" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="17" font-weight="800">Mrs. Barbara Fisher</text>
      <text x="748" y="3328" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="500">IFL &amp; Bible Curriculum Specialist,</text>
      <text x="748" y="3348" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Adventist Education (Australia)</text>
    </g>

    <!-- Speaker 7: Dr. Oluwole A. Oyedeji -->
    <g id="Speaker_Invited_Oyedeji">
      <rect x="1060" y="3010" width="316" height="390" rx="20" fill="url(#card_grad)" stroke="#264673" stroke-width="1.2"/>
      <rect id="PHOTO_SPEAKER_OYEDEJI" x="1080" y="3030" width="276" height="210" rx="12" fill="#102A4C"/>
      <rect x="1080" y="3256" width="136" height="24" rx="12" fill="#14325C"/>
      <text x="1148" y="3272" fill="#FBBF24" font-family="Inter, sans-serif" font-size="10" font-weight="800" text-anchor="middle">INVITED SPEAKER</text>
      <text x="1080" y="3304" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="17" font-weight="800">Dr. Oluwole A. Oyedeji</text>
      <text x="1080" y="3328" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="500">Consultant Geoscientist &amp;</text>
      <text x="1080" y="3348" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Faith-Science Scholar (Abuja, Nigeria)</text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 7. INTERACTIVE AGENDA & KEY DATES ROADMAP (y = 3460..4180)        -->
  <!-- ================================================================= -->
  <g id="07_Schedule_And_Key_Dates">
    <rect x="0" y="3460" width="1440" height="720" fill="#051020"/>

    <text x="64" y="3524" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="2">// CONFERENCE PROGRAM &amp; MILESTONE DATES</text>
    <text x="64" y="3566" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="34" font-weight="900">6-Day Hybrid Schedule &amp; Deadlines</text>

    <!-- Left Column: Pinterest-Style Tabbed Schedule (x = 64..840) -->
    <g id="Program_Schedule_Left">
      <rect x="64" y="3596" width="136" height="38" rx="10" fill="url(#gold_grad)"/>
      <text x="132" y="3620" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="800" text-anchor="middle">Tue, July 27</text>

      <rect x="212" y="3596" width="136" height="38" rx="10" fill="#0D2240" stroke="#264673" stroke-width="1"/>
      <text x="280" y="3620" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Wed, July 28</text>

      <rect x="360" y="3596" width="136" height="38" rx="10" fill="#0D2240" stroke="#264673" stroke-width="1"/>
      <text x="428" y="3620" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Thu, July 29</text>

      <rect x="508" y="3596" width="136" height="38" rx="10" fill="#0D2240" stroke="#264673" stroke-width="1"/>
      <text x="576" y="3620" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Fri, July 30</text>

      <rect x="656" y="3596" width="184" height="38" rx="10" fill="#0D2240" stroke="#264673" stroke-width="1"/>
      <text x="748" y="3620" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Sat–Sun, Jul 31–Aug 1</text>

      <!-- Schedule Rows -->
      <rect x="64" y="3654" width="776" height="96" rx="16" fill="#0B2140" stroke="#1E3A5F" stroke-width="1.2"/>
      <rect x="88" y="3676" width="144" height="28" rx="8" fill="#14325C"/>
      <text x="160" y="3695" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">09:00 AM – 01:00 PM</text>
      <text x="252" y="3694" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="800">Arrival, Physical &amp; Virtual Delegate Accreditation</text>
      <text x="252" y="3720" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Collection of Conference Materials &amp; Hybrid Zoom Access Onboarding</text>

      <rect x="64" y="3766" width="776" height="96" rx="16" fill="#0B2140" stroke="#F59E0B" stroke-width="1.2"/>
      <rect x="88" y="3788" width="144" height="28" rx="8" fill="url(#gold_grad)"/>
      <text x="160" y="3807" fill="#051020" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">02:00 PM – 05:00 PM</text>
      <text x="252" y="3806" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="800">Opening Ceremony &amp; Keynote Address: Sustainable Faith Ecosystems</text>
      <text x="252" y="3832" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="600">Chief Host: Prof. Ademola Tayo • Convener: Prof. Constance C. Nwosu</text>

      <rect x="64" y="3878" width="776" height="96" rx="16" fill="#0B2140" stroke="#1E3A5F" stroke-width="1.2"/>
      <rect x="88" y="3900" width="144" height="28" rx="8" fill="#14325C"/>
      <text x="160" y="3919" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">DAY 2 – DAY 4</text>
      <text x="252" y="3918" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="800">Plenary Sessions &amp; Parallel Paper Presentations (8 Fields)</text>
      <text x="252" y="3944" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Science, Arts, Technology, Leadership, Business, Institutions, Religion &amp; Policy</text>

      <rect x="64" y="3990" width="776" height="96" rx="16" fill="#0B2140" stroke="#1E3A5F" stroke-width="1.2"/>
      <rect x="88" y="4012" width="144" height="28" rx="8" fill="#14325C"/>
      <text x="160" y="4031" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800" text-anchor="middle">SAT–SUN, AUG 1</text>
      <text x="252" y="4030" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="800">Sabbath Worship, Communiqué, Awards &amp; Official Departure</text>
      <text x="252" y="4056" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">Certificate Issuance &amp; IJFI Peer-Review Publication Fast-Track</text>
    </g>

    <!-- Right Column: Official Flyer Key Dates Card (x = 872..1376) -->
    <g id="Key_Dates_Roadmap_Right">
      <rect x="872" y="3596" width="504" height="490" rx="24" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="2"/>
      <text x="908" y="3642" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="900" letter-spacing="1.5">KEY DATES &amp; DEADLINES</text>
      <line x1="908" y1="3658" x2="1340" y2="3658" stroke="#264673" stroke-width="1"/>

      <!-- 5 Dates from Flyer -->
      <rect x="908" y="3680" width="432" height="54" rx="12" fill="#08172E" stroke="#1E3A5F" stroke-width="1"/>
      <text x="928" y="3712" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">Registration Opens</text>
      <rect x="1188" y="3691" width="136" height="32" rx="8" fill="url(#gold_grad)"/>
      <text x="1256" y="3712" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="900" text-anchor="middle">02 NOV 2026</text>

      <rect x="908" y="3748" width="432" height="54" rx="12" fill="#08172E" stroke="#1E3A5F" stroke-width="1"/>
      <text x="928" y="3780" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">Abstract Deadline</text>
      <rect x="1188" y="3759" width="136" height="32" rx="8" fill="url(#gold_grad)"/>
      <text x="1256" y="3780" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="900" text-anchor="middle">24 MARCH 2027</text>

      <rect x="908" y="3816" width="432" height="54" rx="12" fill="#08172E" stroke="#1E3A5F" stroke-width="1"/>
      <text x="928" y="3848" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">Early Bird Closes</text>
      <rect x="1188" y="3827" width="136" height="32" rx="8" fill="url(#gold_grad)"/>
      <text x="1256" y="3848" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="900" text-anchor="middle">23 APRIL 2027</text>

      <rect x="908" y="3884" width="432" height="54" rx="12" fill="#08172E" stroke="#1E3A5F" stroke-width="1"/>
      <text x="928" y="3916" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">Full Paper Deadline</text>
      <rect x="1188" y="3895" width="136" height="32" rx="8" fill="url(#gold_grad)"/>
      <text x="1256" y="3916" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="900" text-anchor="middle">09 MAY 2027</text>

      <rect x="908" y="3952" width="432" height="54" rx="12" fill="#08172E" stroke="#1E3A5F" stroke-width="1"/>
      <text x="928" y="3984" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14" font-weight="700">Seat Reservation Deadline</text>
      <rect x="1188" y="3963" width="136" height="32" rx="8" fill="url(#gold_grad)"/>
      <text x="1256" y="3984" fill="#051020" font-family="Inter, sans-serif" font-size="12" font-weight="900" text-anchor="middle">31 MAY 2027</text>

      <text x="908" y="4042" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="600">Abstracts (max 250 words, Times New Roman 12pt) to:</text>
      <text x="908" y="4064" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="800">icfi@babcock.edu.ng • Dr. O. Olomojobi (08082334427)</text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- 8. 3-TIER REGISTRATION PRICING & BANKING PORTAL (y = 4180..4920)  -->
  <!-- ================================================================= -->
  <g id="08_Registration_Pricing_And_Payment">
    <rect x="0" y="4180" width="1440" height="740" fill="#071529"/>

    <text x="720" y="4242" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" text-anchor="middle" letter-spacing="2">// CHOOSE YOUR CONFERENCE PASS</text>
    <text x="720" y="4286" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="36" font-weight="900" text-anchor="middle">Registration Fees &amp; Banking Channels</text>

    <!-- Card 1: Standard In-Person -->
    <g id="Pricing_Card_Standard">
      <rect x="64" y="4326" width="412" height="360" rx="22" fill="url(#card_grad)" stroke="#264673" stroke-width="1.5"/>
      <text x="96" y="4372" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">IN-PERSON DELEGATE</text>
      <text x="96" y="4404" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="800">Standard Conference Fee</text>
      <text x="96" y="4456" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="38" font-weight="900">₦50,000</text>
      <text x="276" y="4456" fill="#FBBF24" font-family="Inter, sans-serif" font-size="22" font-weight="800">/ $100 USD</text>
      <text x="96" y="4502" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Full Physical Access to All Plenaries &amp; Tracks</text>
      <text x="96" y="4530" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Official Conference Materials &amp; Delegate Kit</text>
      <text x="96" y="4558" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Daily Lunch &amp; Networking Refreshments</text>
      <text x="96" y="4586" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Free IJFI Publication (Subject to Peer Review)</text>
      <rect x="96" y="4616" width="348" height="46" rx="12" fill="#112A4E" stroke="#F59E0B" stroke-width="1.2"/>
      <text x="270" y="4644" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Select Standard Pass</text>
    </g>

    <!-- Card 2: Early Bird (Elevated Center Highlight) -->
    <g id="Pricing_Card_EarlyBird">
      <rect x="504" y="4310" width="432" height="392" rx="24" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="2.5"/>
      <rect x="596" y="4296" width="248" height="28" rx="14" fill="url(#gold_grad)"/>
      <text x="720" y="4315" fill="#051020" font-family="Inter, sans-serif" font-size="11" font-weight="900" text-anchor="middle">★ EARLY BIRD &amp; COMMUNITY RATE ★</text>
      <text x="536" y="4366" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">BEST VALUE • UNTIL APRIL 23, 2027</text>
      <text x="536" y="4398" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="26" font-weight="900">Early Bird Registration</text>
      <text x="536" y="4452" fill="#FBBF24" font-family="Inter, sans-serif" font-size="42" font-weight="900">₦40,000</text>
      <text x="730" y="4452" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="800">/ $80 USD</text>
      <text x="536" y="4496" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="13" font-weight="600">✓ Paper Presentation &amp; Certificate of Participation</text>
      <text x="536" y="4524" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="13" font-weight="600">✓ Free Publication in IJFI Journal (Peer-Reviewed)</text>
      <text x="536" y="4552" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="13" font-weight="600">✓ Conference Materials &amp; Daily Lunch Included</text>
      <text x="536" y="4580" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="700">✓ ₦10,000 Off for Registered Community Members</text>
      <text x="536" y="4606" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="12" font-weight="500">* Members retain Early Bird rates after April 23.</text>
      <rect x="536" y="4630" width="368" height="48" rx="12" fill="url(#gold_grad)"/>
      <text x="720" y="4659" fill="#051020" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">Claim Early Bird Pass →</text>
    </g>

    <!-- Card 3: Online / Virtual -->
    <g id="Pricing_Card_Virtual">
      <rect x="964" y="4326" width="412" height="360" rx="22" fill="url(#card_grad)" stroke="#264673" stroke-width="1.5"/>
      <text x="996" y="4372" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">REMOTE GLOBAL ACCESS</text>
      <text x="996" y="4404" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="800">Online / Virtual Pass</text>
      <text x="996" y="4456" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="38" font-weight="900">₦25,000</text>
      <text x="1176" y="4456" fill="#FBBF24" font-family="Inter, sans-serif" font-size="22" font-weight="800">/ $50 USD</text>
      <text x="996" y="4502" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Live HD Hybrid Streaming of All Sessions</text>
      <text x="996" y="4530" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Virtual Paper Presentation Slot &amp; Q&amp;A</text>
      <text x="996" y="4558" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Free IJFI Publication (Subject to Peer Review)</text>
      <text x="996" y="4586" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">✓ Digital Book of Abstracts &amp; E-Certificate</text>
      <rect x="996" y="4616" width="348" height="46" rx="12" fill="#112A4E" stroke="#F59E0B" stroke-width="1.2"/>
      <text x="1170" y="4644" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Select Virtual Pass</text>
    </g>

    <!-- Official Bank Accounts Bar -->
    <rect x="64" y="4724" width="636" height="148" rx="18" fill="#0B2140" stroke="#264673" stroke-width="1.5"/>
    <text x="96" y="4760" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">LOCAL PARTICIPANTS BANK ACCOUNT (NGN ₦)</text>
    <text x="96" y="4794" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" font-weight="800">UBA Plc  •  Acct No: 1020069501</text>
    <text x="96" y="4824" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="14" font-weight="600">Account Name: Babcock MFB</text>
    <text x="96" y="4850" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Registration Info: Miss Deborah Caleb (08064007567)</text>

    <rect x="740" y="4724" width="636" height="148" rx="18" fill="#0B2140" stroke="#264673" stroke-width="1.5"/>
    <text x="772" y="4760" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.2">INTERNATIONAL PARTICIPANTS BANK ACCOUNT (USD $)</text>
    <text x="772" y="4794" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" font-weight="800">GTBank  •  Acct No: 0829898610</text>
    <text x="772" y="4824" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="14" font-weight="600">Account Name: B.U-Op./Inst. For Faith Integr</text>
    <text x="772" y="4850" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Public Relations: Dr. Chinaka Emmanuel (07089324791)</text>
  </g>

  <!-- ================================================================= -->
  <!-- 9. IJFI JOURNAL & PAST CONFERENCE PAPERS REPOSITORY (y=4920..5440)-->
  <!-- ================================================================= -->
  <g id="09_IJFI_Journal_And_Papers_Archive">
    <rect x="0" y="4920" width="1440" height="520" fill="#051020"/>

    <text x="64" y="4984" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="2">// SCHOLARLY PUBLICATIONS &amp; ARCHIVE</text>
    <text x="64" y="5026" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="34" font-weight="900">International Journal for Faith Integration (IJFI) &amp; Past Papers</text>

    <!-- Left Card: IJFI Call for Papers -->
    <rect x="64" y="5056" width="580" height="336" rx="22" fill="url(#blue_banner_grad)" stroke="#F59E0B" stroke-width="2"/>
    <rect x="96" y="5088" width="220" height="28" rx="14" fill="url(#gold_grad)"/>
    <text x="206" y="5106" fill="#051020" font-family="Inter, sans-serif" font-size="11" font-weight="900" text-anchor="middle">BI-ANNUAL PEER-REVIEWED JOURNAL</text>
    <text x="96" y="5148" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="24" font-weight="900">International Journal for Faith</text>
    <text x="96" y="5180" fill="#FBBF24" font-family="Inter, sans-serif" font-size="24" font-weight="900">Integration (IJFI)</text>
    <text x="96" y="5218" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">An official double-blind peer-reviewed publication of the Institute</text>
    <text x="96" y="5240" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">for Faith Integration, Babcock University. Bestrides learning, life,</text>
    <text x="96" y="5262" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="13" font-weight="500">and service with practical biblical integration.</text>
    <text x="96" y="5300" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="700">Core Values: Originality • Bible-Based • Integrity • Excellence</text>
    <rect x="96" y="5324" width="240" height="44" rx="10" fill="#FFFFFF"/>
    <text x="216" y="5351" fill="#051020" font-family="Inter, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Explore IJFI Journal →</text>

    <!-- Right Grid: 4 Downloadable Research Papers from FIPP Conference folder -->
    <rect x="676" y="5056" width="336" height="158" rx="16" fill="#0B2140" stroke="#264673" stroke-width="1.2"/>
    <text x="700" y="5088" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800">PDF PAPER • SOCIAL WORK</text>
    <text x="700" y="5116" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Integrating Faith into Learning:</text>
    <text x="700" y="5138" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Social Work Class Experiences</text>
    <text x="700" y="5166" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Babcock University Case Study</text>
    <text x="700" y="5194" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700">Download PDF ↓</text>

    <rect x="1036" y="5056" width="340" height="158" rx="16" fill="#0B2140" stroke="#264673" stroke-width="1.2"/>
    <text x="1060" y="5088" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800">PDF PAPER • AUDIT &amp; GOVERNANCE</text>
    <text x="1060" y="5116" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Faith Integration in Internal Audit</text>
    <text x="1060" y="5138" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">&amp; Compliance Functions</text>
    <text x="1060" y="5166" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Private Universities in Nigeria</text>
    <text x="1060" y="5194" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700">Download PDF ↓</text>

    <rect x="676" y="5234" width="336" height="158" rx="16" fill="#0B2140" stroke="#264673" stroke-width="1.2"/>
    <text x="700" y="5266" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800">PDF PAPER • EDUCATION MGMT</text>
    <text x="700" y="5294" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Integration of Faith in Innovative</text>
    <text x="700" y="5316" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Quality Education Management</text>
    <text x="700" y="5344" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">ICFI Archive Proceedings</text>
    <text x="700" y="5372" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700">Download PDF ↓</text>

    <rect x="1036" y="5234" width="340" height="158" rx="16" fill="#0B2140" stroke="#264673" stroke-width="1.2"/>
    <text x="1060" y="5266" fill="#FBBF24" font-family="Inter, sans-serif" font-size="11" font-weight="800">PDF PAPER • BIBLICAL MODELS</text>
    <text x="1060" y="5294" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Biblical Graph Representation of</text>
    <text x="1060" y="5316" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="15" font-weight="700">Matthew 22:34–40 in Nigeria</text>
    <text x="1060" y="5344" fill="#94A3B8" font-family="Inter, sans-serif" font-size="12" font-weight="500">Relational Principles Study</text>
    <text x="1060" y="5372" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="700">Download PDF ↓</text>
  </g>

  <!-- ================================================================= -->
  <!-- 10. PAST CONFERENCES GALLERY & FOOTER (y = 5440..6120)            -->
  <!-- ================================================================= -->
  <g id="10_Gallery_Accommodation_And_Footer">
    <rect x="0" y="5440" width="1440" height="680" fill="#071529"/>

    <text x="64" y="5496" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="2">// CONFERENCE SNAPSHOTS &amp; ACCOMMODATION</text>
    <text x="64" y="5536" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="32" font-weight="900">Moments from Past Editions (2017 – 2025)</text>

    <!-- 6 Gallery Photo Frames from images2019 & images2 -->
    <rect id="PHOTO_GAL_1" x="64" y="5564" width="204" height="160" rx="14" fill="#102A4C" stroke="#F59E0B" stroke-width="1.2"/>
    <rect id="PHOTO_GAL_2" x="284" y="5564" width="204" height="160" rx="14" fill="#102A4C" stroke="#264673" stroke-width="1.2"/>
    <rect id="PHOTO_GAL_3" x="504" y="5564" width="204" height="160" rx="14" fill="#102A4C" stroke="#264673" stroke-width="1.2"/>
    <rect id="PHOTO_GAL_4" x="724" y="5564" width="204" height="160" rx="14" fill="#102A4C" stroke="#264673" stroke-width="1.2"/>
    <rect id="PHOTO_GAL_5" x="944" y="5564" width="204" height="160" rx="14" fill="#102A4C" stroke="#264673" stroke-width="1.2"/>
    <rect id="PHOTO_GAL_6" x="1164" y="5564" width="212" height="160" rx="14" fill="#102A4C" stroke="#F59E0B" stroke-width="1.2"/>

    <!-- Campus Accommodation & CTA Banner -->
    <rect x="64" y="5754" width="1312" height="164" rx="22" fill="url(#card_elevated_grad)" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="100" y="5796" fill="#FBBF24" font-family="Inter, sans-serif" font-size="12" font-weight="800" letter-spacing="1.5">CAMPUS ACCOMMODATION &amp; RESERVATIONS</text>
    <text x="100" y="5830" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="22" font-weight="800">Babcock Guest House (BGH) • Havillah Cottage • Royal Cream Suite</text>
    <text x="100" y="5862" fill="#CBD5E1" font-family="Inter, sans-serif" font-size="14" font-weight="500">Accommodation is available on campus for an additional fee. Contact Dr. Nnenna Nwobi at +234 813 538 8049 for arrangements.</text>
    <text x="100" y="5890" fill="#FBBF24" font-family="Inter, sans-serif" font-size="13" font-weight="700">Reserve a seat now to get full conference benefits!</text>

    <rect x="1012" y="5786" width="328" height="52" rx="12" fill="url(#gold_grad)"/>
    <text x="1176" y="5817" fill="#051020" font-family="Inter, sans-serif" font-size="14" font-weight="900" text-anchor="middle">Submit Abstract: icfi@babcock.edu.ng</text>

    <rect x="1012" y="5848" width="328" height="44" rx="10" fill="#FFFFFF"/>
    <text x="1176" y="5875" fill="#051020" font-family="Inter, sans-serif" font-size="13" font-weight="800" text-anchor="middle">Register via Google Form →</text>

    <!-- Bottom Footer Bar -->
    <rect x="0" y="5956" width="1440" height="164" fill="#030914"/>
    <line x1="64" y1="5956" x2="1376" y2="5956" stroke="#1E3A5F" stroke-width="1"/>
    <text x="64" y="6012" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16" font-weight="800">THE INTERNATIONAL COMMUNITY FOR FAITH INTEGRATION (ICFI)</text>
    <text x="64" y="6038" fill="#94A3B8" font-family="Inter, sans-serif" font-size="13" font-weight="500">In Collaboration with Babcock University • Office of Institutional Effectiveness, Ilishan-Remo, Ogun State, Nigeria</text>
    <text x="64" y="6068" fill="#64748B" font-family="Inter, sans-serif" font-size="12" font-weight="500">© 2027 International Conference for Faith Integration. All rights reserved.</text>
    <text x="1376" y="6038" fill="#FBBF24" font-family="Inter, sans-serif" font-size="14" font-weight="800" text-anchor="end">icfi@babcock.edu.ng  •  +234 806 463 8207</text>
  </g>
</svg>
'''

with open('icfi_7th_figma_design.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Generated icfi_7th_figma_design.svg:', os.path.getsize('icfi_7th_figma_design.svg'), 'bytes')
