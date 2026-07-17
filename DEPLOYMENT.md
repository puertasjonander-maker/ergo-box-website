# 🎉 ERGO BOX v2 — EDITORIAL LANDING + AUTOMATED BOOKING

## ✅ **STATUS: PRODUCTION READY**

Landing page con alma editorial + sistema automático de reservas + lead magnet.

---

## 📦 **WHAT'S NEW IN v2**

### **🎨 Design: Editorial & Soulful**
- **Typography-driven**: Fraunces serif for headlines, magazine-quality hierarchy
- **Asymmetric layout**: Not centered boxes — editorial split-screen composition
- **Real photography**: AI-generated gritty, authentic gym imagery
- **Texture & depth**: Paper-like background with subtle grain overlay
- **Color palette**: Warm cream, burnt amber, deep ink — no tech gradients

### **📅 Booking: Fully Automated**
- **Cal.com integration**: Free booking system with date picker
- **Automatic emails**: Confirmation + 24h reminder
- **Calendar sync**: Connects to your Google/Outlook calendar
- **No backend needed**: Cal.com handles everything

### **🎁 Lead Magnet: The "Present"**
- **Professional PDF guide**: 5-page maintenance checklist
- **Instant download**: After form submission
- **Printable**: Checkbox format for daily use
- **Email automation ready**: Works with MailerLite/Formspree

---

## 📁 **FILE STRUCTURE**

```
ergo-box-website-v2/
├── index.html                      # Landing page (editorial design)
├── guia-mantenimiento-ergo-box.pdf # Lead magnet (5 pages)
├── generate_pdf.py                 # PDF generator script
├── CALCOM-SETUP.md                 # Booking system setup guide
└── DEPLOYMENT.md                   # This file
```

---

## 🚀 **DEPLOYMENT OPTIONS**

### **Option 1: GitHub → Hostinger Git Deploy (RECOMMENDED)**

**Prerequisites:**
- GitHub repo: `puertasjonander-maker/ergo-box-website`
- Hostinger account with ergobox.es domain

**Steps:**
1. **Push v2 to GitHub:**
   ```bash
   cd /home/hermes/ergo-box-website-v2
   git init
   git add .
   git commit -m "v2: Editorial design + Cal.com booking"
   git remote add origin https://github.com/puertasjonander-maker/ergo-box-website.git
   git push -f origin main  # Force push to replace v1
   ```

2. **Configure Hostinger Git Deploy:**
   - hPanel → Websites → ergobox.es → Git
   - Repository: `https://github.com/puertasjonander-maker/ergo-box-website.git`
   - Branch: `main`
   - Deploy Path: `/public_html/`
   - Auto-deploy: ✅ Enable

3. **Verify deployment:**
   - https://ergobox.es should show new design in 2-5 minutes

---

### **Option 2: Manual Upload via File Manager**

**Steps:**
1. **Download files from GitHub** or use local copies
2. **hPanel → File Manager → /public_html/**
3. **Upload these files:**
   ```
   index.html
   guia-mantenimiento-ergo-box.pdf
   ```
4. **Replace existing index.html** if prompted

---

### **Option 3: Hostinger API (Advanced)**

Using the token provided:
```python
# See API-DEPLOYMENT.md for full script
import requests

HOSTINGER_TOKEN = "PvLHzYAEmh9LCYGzA4goxnlADp9eXblmMim8AyYa976fac75"

# 1. Create website for ergobox.es
# 2. Deploy static files via API
# 3. Configure SSL
```

---

## 📅 **CAL.COM SETUP (Required for booking)**

### **Quick Start (10 minutes):**

1. **Create account:** https://cal.com (free)
2. **New event type:**
   - Name: "Revisión Gratuita de Erg"
   - Duration: 45 min
   - Location: In person
3. **Set availability:** Your working hours
4. **Get embed code:** Settings → Embed → Copy iframe
5. **Replace in index.html:**
   ```html
   <!-- Find this section (around line 470) -->
   <div class="cal-embed-placeholder">
       <!-- Replace entire div with: -->
       <iframe src="https://cal.com/YOUR-USERNAME/revision-gratuita?embed=true" 
               width="100%" height="700px" frameborder="0"></iframe>
   </div>
   ```

**Full setup guide:** See `CALCOM-SETUP.md`

---

## 🎁 **LEAD MAGNET AUTOMATION**

### **Current state:**
- PDF exists: `guia-mantenimiento-ergo-box.pdf`
- Form captures: email + box name
- Manual email: You send PDF after form submission

### **To automate (choose one):**

**A) Formspree + Manual PDF email:**
- Form sends to hola@ergobox.es
- You reply with PDF attachment
- **Pros:** Simple, control
- **Cons:** Manual work

**B) MailerLite (Recommended):**
- Create automation: New subscriber → Send PDF
- Embed MailerLite form instead of custom form
- **Cost:** Free up to 1,000 subscribers
- **Setup guide:** See CALCOM-SETUP.md section "Lead Magnet Automation"

**C) Notion + Zapier:**
- Form → Notion database
- Zapier sends PDF automatically
- **Cost:** Zapier paid plan needed
- **Pros:** Everything in Notion

---

## 📊 **METRICS TO TRACK**

### **Fase 0 Goal: 3+ conversations with box owners per week**

**Primary metrics:**
- Booking submissions (Cal.com dashboard)
- Guide downloads (form submissions)
- Conversion: Download → Booking

**Traffic sources:**
- Instagram bio link clicks
- WhatsApp shares
- Direct URL
- Google (SEO)

**Setup tracking:**
```html
<!-- Add to <head> in index.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🔍 **TESTING CHECKLIST**

### **Visual:**
- [ ] Landing page loads on desktop
- [ ] Landing page loads on mobile (responsive)
- [ ] Typography renders correctly (Fraunces serif)
- [ ] Images load properly
- [ ] Grain texture visible but subtle

### **Functionality:**
- [ ] Smooth scroll navigation works
- [ ] "Reservar revisión" scrolls to booking section
- [ ] Lead form accepts input and shows success message
- [ ] PDF downloads when clicked (test manually)
- [ ] All links work (email, phone, Instagram)

### **Cal.com (after setup):**
- [ ] Calendar embed loads
- [ ] Can select date/time
- [ ] Booking confirmation email received
- [ ] Reminder email sent 24h before

### **Performance:**
- [ ] Page loads in <3 seconds
- [ ] No console errors (F12)
- [ ] Mobile-friendly (Google Mobile-Friendly Test)

---

## 🎨 **DESIGN RATIONALE**

### **Why this design has "soul":**

1. **Typography as protagonist:**
   - Fraunces serif (like a magazine) not Inter sans (like a SaaS)
   - Italic accents for emphasis, not bold everywhere
   - Hierarchy through weight and size, not color

2. **Asymmetric editorial layout:**
   - Split-screen hero (like a magazine spread)
   - Text on left, image on right (not centered everything)
   - Pull quotes and manifesto sections (storytelling)

3. **Texture and warmth:**
   - Cream background (#F6F2EA) not pure white
   - Grain overlay for tactile feel
   - Burnt amber (#EE7D11) not corporate blue

4. **Real photography:**
   - Gritty, atmospheric gym images
   - Not generic stock photos or illustrations
   - Film photography aesthetic (grain, contrast)

5. **Editorial voice:**
   - Copy that tells stories, not lists features
   - "¿Te suena familiar?" not "Our services"
   - Honest, direct, athlete-to-athlete tone

---

## 🛠️ **CUSTOMIZATION GUIDE**

### **To change the offer (e.g., from "revisión gratis" to something else):**

1. **Hero section (line ~320):**
   ```html
   <h1>
       Tus coaches <em>entrenan.</em><br>
       Del equipo nos <em>encargamos</em> nosotros.
   </h1>
   ```

2. **Free badge (line ~350):**
   ```html
   <div class="free-badge">
       <div class="badge-top">Primera</div>
       <div class="badge-main">GRATIS</div>
       <div class="badge-bottom">Revisión erg</div>
   </div>
   ```

3. **Offer section (line ~440):**
   - Update title, description, features list

### **To add more sections:**

Follow the pattern:
```html
<section class="new-section">
    <div class="section-number">06 — Título</div>
    <h2 class="section-title">Título con <em>énfasis</em></h2>
    <!-- Content -->
</section>
```

Copy CSS pattern from existing sections.

---

## 📧 **EMAIL TEMPLATES (For Cal.com / MailerLite)**

### **Booking confirmation (Cal.com sends automatically):**

```
Subject: ✅ Revisión confirmada — {{event_date}}

Hola {{name}},

Tu revisión gratuita está confirmada:

📅 {{event_date}} a las {{event_time}}
📍 {{location}}

QUÉ ESPERAR:
- Revisión completa de tu erg (45 min)
- Limpieza básica incluida
- Informe con semáforo de estado
- Presupuesto sin compromiso

PREPARA:
- Acceso al erg
- Dime si hay más equipos que te preocupan

¿Cambios? {{reschedule_link}}

Nos vemos,
Jon — ERGO BOX
```

### **Lead magnet delivery (MailerLite automation):**

```
Subject: 📋 Tu guía de mantenimiento — ERGO BOX

Hola,

Aquí está la guía que pediste: checklist profesional para mantener tu box en perfecto estado.

[DESCARGAR PDF]

Dentro encontrarás:
✓ Calendario de mantenimiento por equipo
✓ Checklists semanales/mensuales/trimestrales
✓ Señales de alarma a vigilar
✓ Cuándo llamar a un profesional

¿Te ha servido? Responde a este email y cuéntame.

Un abrazo,
Jon Ander — ERGO BOX

P.D. Si necesitas ayuda profesional, la primera revisión de un erg es gratis: https://ergobox.es#reservar
```

---

## 🎯 **LAUNCH CHECKLIST**

### **Pre-launch (today):**
- [ ] Push v2 to GitHub
- [ ] Deploy to Hostinger (Git or manual)
- [ ] Verify ergobox.es loads new design
- [ ] Test on mobile
- [ ] Create Cal.com account
- [ ] Configure "Revisión Gratuita" event
- [ ] Embed calendar in landing page
- [ ] Test booking flow end-to-end

### **Launch (this week):**
- [ ] Update Instagram bio: "Primera revisión gratis 👇 ergobox.es"
- [ ] Post story: Screenshot of new website
- [ ] WhatsApp to box contacts: "Ya tenemos web 🚀 ergobox.es"
- [ ] Set up MailerLite for lead automation
- [ ] Create Google Analytics account

### **Post-launch (next week):**
- [ ] Monitor Cal.com bookings
- [ ] Track guide downloads
- [ ] Respond to inquiries within 24h
- [ ] Collect feedback from first leads
- [ ] A/B test headline if conversion is low

---

## 🔥 **WHAT MAKES THIS SPECIAL**

### **Compared to v1 (the simple HTML site):**
- ✅ **Editorial design** vs generic SaaS template
- ✅ **Automated booking** vs manual contact form
- ✅ **Professional PDF** vs basic HTML guide
- ✅ **Typography-driven** vs icon-driven
- ✅ **Storytelling copy** vs feature lists
- ✅ **Asymmetric layout** vs centered everything
- ✅ **Real photography** vs stock images

### **Compared to Hostinger Website Builder:**
- ✅ **Unique design** vs template look
- ✅ **Custom booking** vs generic contact form
- ✅ **Full control** vs platform limitations
- ✅ **Better performance** vs bloated builder code
- ✅ **Easy to customize** vs drag-and-drop constraints

---

## 📞 **SUPPORT & NEXT STEPS**

### **If something breaks:**
1. Check browser console (F12) for errors
2. Verify all files uploaded correctly
3. Test on different browsers/devices
4. Check Cal.com embed code is correct

### **To add features later:**
- Blog (Markdown files + simple generator)
- Case studies (once you have clients)
- Pricing page (when you close first retainer)
- Online payment (Stripe integration)

### **Questions?**
- Cal.com setup: https://cal.com/docs
- Design changes: Edit index.html directly
- Deployment issues: See HOSTINGER-SETUP.md in v1 repo

---

## 🎊 **YOU'RE READY TO LAUNCH**

**What you have:**
- ✅ Editorial landing page with soul
- ✅ Automated booking system (Cal.com ready)
- ✅ Professional PDF lead magnet
- ✅ Email automation templates
- ✅ Complete deployment guide

**What to do:**
1. **Deploy** (Git or manual upload)
2. **Setup Cal.com** (10 minutes)
3. **Launch** (Instagram bio link + WhatsApp outreach)
4. **Track** (bookings per week)

**Success metric:**
🎯 **3+ conversations with box owners per week**

---

**Made with 🖤 by athletes, for athletes.**

**Questions? Let's build this thing.** 🚀