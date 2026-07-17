# 🎯 ERGO BOX — Sistema de Reservas Automáticas con Cal.com

## 📋 **Objetivo**

Sistema completo de reserva de revisiones gratuitas con:
- ✅ Calendario interactivo con disponibilidad en tiempo real
- ✅ Confirmación automática por email
- ✅ Recordatorios automáticos
- ✅ Sincronización con tu calendario (Google/Outlook)
- ✅ Gestión de cancelaciones y reprogramaciones
- ✅ Formulario pre-visita para calificar leads

**Coste: 0€/mes** (Cal.com free tier hasta 500 reservas/mes)

---

## 🚀 **Setup Paso a Paso**

### **Paso 1: Crear Cuenta Cal.com**

1. Ve a **https://cal.com** 
2. Sign up con tu email (hola@ergobox.es recomendado)
3. Plan **Free** — más que suficiente para Fase 0

### **Paso 2: Crear Event Type "Revisión Gratuita de Erg"**

**Configuración básica:**
```
Event name: Revisión Gratuita de Erg
Duration: 45 minutos
Location: In person (tu box)
Description: 

"Primera revisión completa de un erg (RowErg, BikeErg, SkiErg) sin coste.

Incluye:
✓ Revisión de cadena, raíles y monitor
✓ Limpieza básica y ajustes
✓ Informe de estado con semáforo verde/ámbar/rojo
✓ Recomendaciones de mantenimiento
✓ Presupuesto sin compromiso si necesitas algo más

Duración aproximada: 45 minutos
Zona de servicio: Málaga y alrededores"
```

**Availability:**
```
Lunes a Viernes: 9:00 - 13:00 y 17:00 - 20:00
Sábados: 10:00 - 14:00
Domingos: Cerrado

Buffer time: 30 minutos entre citas
```

**Booking questions (formulario pre-visita):**
```
1. Nombre del box (required)
2. Dirección completa (required)
3. Tipo de erg a revisar (dropdown: RowErg, BikeErg, SkiErg)
4. ¿Tienes más equipamiento que te preocupe? (textarea)
5. ¿Cuál es tu rol? (dropdown: Dueño, Manager, Head Coach, Otro)
```

### **Paso 3: Configurar Emails Automáticos**

**Confirmation email (automático):**
```
Subject: ✅ Revisión confirmada — {{event_date}} a las {{event_time}}

Hola {{name}},

Tu revisión gratuita está confirmada:

📅 Fecha: {{event_date}}
🕐 Hora: {{event_time}}
📍 Lugar: {{location}}

QUÉ ESPERAR:
- Revisaremos tu erg a fondo (45 min)
- Limpieza básica incluida
- Informe de estado con código semáforo
- Presupuesto sin compromiso si necesitas algo

PREPARA:
- Acceso al erg que quieres que revisemos
- Si hay más equipos que te preocupan, dímelo al llegar

¿Necesitas cambiar la cita? Hazlo aquí: {{reschedule_link}}

Nos vemos pronto,
Jon Ander — ERGO BOX
```

**Reminder email (24h antes):**
```
Subject: 📅 Mañana nos vemos — Revisión {{box_name}}

Hola {{name}},

Te recuerdo que mañana {{event_date}} a las {{event_time}} estaremos en {{box_name}} para la revisión gratuita de tu erg.

Si necesitas cambiar algo, hazlo cuanto antes:
{{reschedule_link}}

¡Hasta mañana!
ERGO BOX
```

### **Paso 4: Conectar tu Calendario**

1. Settings → **Connected Calendars**
2. Conectar **Google Calendar** o **Outlook**
3. Esto sincroniza tu disponibilidad real — solo aparecen huecos libres

### **Paso 5: Obtener el Embed Code**

1. En tu event type, click **"Embed"**
2. Copia el código iframe:
```html
<iframe 
  src="https://cal.com/ergobox/revision-gratuita?embed=true" 
  width="100%" 
  height="700px" 
  frameborder="0">
</iframe>
```

---

## 🔧 **Integración en la Landing Page**

Reemplazar en `index.html` el bloque `<div class="cal-embed-placeholder">` con:

```html
<!-- Cal.com Embed -->
<div class="cal-embed" style="margin-top: 48px;">
    <iframe 
        src="https://cal.com/TU-USUARIO/revision-gratuita?embed=true" 
        width="100%" 
        height="700px" 
        frameborder="0"
        style="border-radius: 8px; box-shadow: 0 8px 32px rgba(15,14,12,0.1);">
    </iframe>
</div>
```

**Estilos adicionales para el iframe:**
```css
.cal-embed iframe {
    background: white;
    border: 1px solid var(--line);
}
```

---

## 📊 **Gestión de Reservas**

### **Dashboard Cal.com:**
- **Upcoming bookings:** Todas las revisiones programadas
- **Past bookings:** Historial completo
- **Pending:** Reservas pendientes de confirmar (si activas aprobación manual)

### **Workflow recomendado:**

**Opción A — Aprobación automática (recomendada):**
1. Cliente reserva → Email automático de confirmación
2. Recordatorio 24h antes
3. Vas y haces la revisión
4. Follow-up manual post-visita

**Opción B — Aprobación manual:**
1. Cliente solicita → Recibes email de notificación
2. Confirmas o propones otra fecha
3. Email automático con la confirmación
4. Recordatorio 24h antes

---

## 🎁 **Lead Magnet Automation (Guía Gratuita)**

El formulario de la guía necesita automation. Opciones:

### **Opción 1: Formspree + Email Manual**
1. Form envía a hola@ergobox.es
2. Tú envías la guía manualmente (PDF adjunto)
3. **Pros:** Simple, control total
4. **Contras:** No es automático

### **Opción 2: Mailchimp/MailerLite (Recomendada)**
1. **Crear lista** "Leads — Guía Mantenimiento"
2. **Setup automation:**
   - Trigger: Nuevo suscriptor
   - Email 1 (inmediato): "Aquí está tu guía" + PDF adjunto
   - Email 2 (+3 días): "¿Te ha servido? Primera revisión gratis"
   - Email 3 (+7 días): "Caso de estudio" o consejo extra
3. **Embed form** en la landing page

**Coste:** Gratis hasta 1,000 suscriptores (MailerLite)

### **Opción 3: Notion + Zapier (Más compleja)**
1. Form → Notion database
2. Zapier envía email con PDF
3. **Pros:** Todo en Notion
4. **Contras:** Requiere Zapier paid para volumen

---

## 📈 **Métricas a Trackear**

### **Cal.com Dashboard:**
- Reservas por semana (objetivo: 3+)
- Tasa de cancelación
- Horarios más solicitados
- Tipo de erg más común

### **Conversiones Landing:**
- Visitas → Clic en "Reservar"
- Visitas → Descarga guía
- Descarga guía → Reserva revisión (lead nurturing)

### **Business:**
- Revisión gratuita → Cliente de pago
- Tiempo medio: primera visita → propuesta aceptada

---

## 🔄 **Post-Revisión: Email Follow-up**

**24h después de la revisión (manual o automatizado):**

```
Subject: ¿Qué tal la revisión? — Tu informe ERGO BOX

Hola {{name}},

Gracias por dejarnos revisar tu erg ayer. Adjunto el informe completo con el estado de tu equipo.

RESUMEN:
🟢 En perfecto estado: X componentes
🟡 Necesita atención: Y componentes
🔴 Urgente: Z componentes

PRÓXIMOS PASOS:
[Si todo OK] "Todo en orden. Te avisaremos cuando toque la próxima revisión."
[Si necesita trabajo] "Te preparé un presupuesto sin compromiso para dejarlo todo a punto."

¿Alguna duda? Responde a este email o escríbeme por WhatsApp: 600 000 000

Un abrazo,
Jon Ander — ERGO BOX

P.D. Si te ha gustado cómo trabajamos, nos ayudaría mucho una reseña en Google.
```

---

## 🛠️ **Archivos Necesarios**

### **1. index.html** (actualizado)
- Cal.com embed integrado
- Formulario lead magnet → Formspree/MailerLite

### **2. guia-mantenimiento.pdf** (crear)
- Versión PDF descargable de la guía
- Diseño coherente con la landing
- Checklist imprimible

### **3. email-templates/** (crear)
- confirmation.html
- reminder.html
- follow-up.html

---

## ✅ **Checklist de Implementación**

### **Esta semana:**
- [ ] Crear cuenta Cal.com
- [ ] Configurar event type "Revisión Gratuita"
- [ ] Conectar Google Calendar
- [ ] Obtener embed code
- [ ] Integrar en landing page
- [ ] Crear cuenta MailerLite/Formspree
- [ ] Diseñar PDF de la guía
- [ ] Setup automation de email

### **Testing:**
- [ ] Hacer una reserva de prueba
- [ ] Verificar email de confirmación
- [ ] Verificar recordatorio 24h
- [ ] Rellenar form de guía
- [ ] Verificar recepción del PDF

### **Launch:**
- [ ] Deploy a Hostinger
- [ ] Actualizar Instagram bio con link
- [ ] Compartir en WhatsApp a contacts de boxes
- [ ] Post anunciando el nuevo sistema

---

## 💡 **Tips Pro**

### **Cal.com:**
- **Bloquea tiempo para ti:** Si tienes otro trabajo, marca esos huecos como "unavailable" en tu calendario conectado
- **Buffer time:** 30 min entre citas para desplazamientos
- **Location:** Usa "In person" y pide dirección en el formulario
- **Cancellation policy:** 24h de antelación (configurar en settings)

### **Lead Magnet:**
- **PDF de calidad:** Invierte 2h en diseño. Es tu carta de presentación
- **Interactive checklist:** Considera una versión Notion también
- **Follow-up sequence:** No vendas en el primer email. Da valor primero

### **Conversión:**
- **Urgencia:** "Solo 3 huecos gratuitos por semana" (aunque sea mentira piadosa, funciona)
- **Prueba social:** Cuando tengas clientes, añade logos/testimonios
- **Remarketing:** Pixel de Facebook/Instagram para ads futuros

---

## 🎯 **Resultado Final Esperado**

**Flujo completo automatizado:**

1. **Cliente potencial** llega a ergobox.es (desde Instagram, WhatsApp, Google)
2. **Ve la oferta** "Primera revisión gratis" → Clic en CTA
3. **Elige fecha/hora** en Cal.com embed → Confirma reserva
4. **Recibe email** automático de confirmación
5. **Recibe recordatorio** 24h antes
6. **Tú haces la revisión** (informe + presupuesto si aplica)
7. **Email follow-up** 24h después con informe
8. **Cliente potencial** se convierte en **cliente de pago** o queda en nurturing

**Todo esto sin que tú tengas que hacer nada manual excepto la revisión física.**

---

## 📞 **Soporte**

Si tienes dudas con:
- **Cal.com setup:** https://cal.com/docs
- **MailerLite automation:** https://www.mailerlite.com/help
- **Embed issues:** Revisa la consola del navegador (F12)

**¿Listo para implementar?** Te ayudo con cualquier paso específico. 🚀