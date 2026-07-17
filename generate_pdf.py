#!/usr/bin/env python3
"""Generate ERGO BOX Maintenance Guide PDF"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
import os

# Brand colors
INK = HexColor('#1A1C20')
PAPER = HexColor('#F6F2EA')
AMBER = HexColor('#EE7D11')
GREEN = HexColor('#1E9E57')
RED = HexColor('#D64545')
STEEL = HexColor('#42474F')
LIGHT_LINE = HexColor('#d4cdc0')

def draw_checkbox(c, x, y, size=4*mm):
    """Draw a checkbox"""
    c.setStrokeColor(STEEL)
    c.setLineWidth(0.5)
    c.rect(x, y, size, size)

def draw_section_header(c, text, y, page_width):
    """Draw a section header"""
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20*mm, y, text)
    
    # Underline
    c.setStrokeColor(AMBER)
    c.setLineWidth(2)
    c.line(20*mm, y-2*mm, 20*mm + 40*mm, y-2*mm)

def draw_checklist_item(c, text, y, x_start=25*mm):
    """Draw a checklist item with checkbox"""
    draw_checkbox(c, x_start, y-1*mm)
    c.setFillColor(INK)
    c.setFont("Helvetica", 10)
    c.drawString(x_start + 7*mm, y, text)

def draw_status_legend(c, y):
    """Draw the semaphore status legend"""
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(INK)
    c.drawString(20*mm, y, "Sistema de evaluación:")
    
    y -= 8*mm
    
    # Green
    c.setFillColor(GREEN)
    c.circle(25*mm, y+1.5*mm, 2*mm, fill=1)
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    c.drawString(30*mm, y, "VERDE — Perfecto estado, mantenimiento al día")
    
    y -= 6*mm
    
    # Amber
    c.setFillColor(AMBER)
    c.circle(25*mm, y+1.5*mm, 2*mm, fill=1)
    c.setFillColor(INK)
    c.drawString(30*mm, y, "ÁMBAR — Atención requerida en 2-4 semanas")
    
    y -= 6*mm
    
    # Red
    c.setFillColor(RED)
    c.circle(25*mm, y+1.5*mm, 2*mm, fill=1)
    c.setFillColor(INK)
    c.drawString(30*mm, y, "ROJO — Intervención urgente, suspender uso")

def create_pdf():
    c = canvas.Canvas("/home/hermes/ergo-box-website/guia-mantenimiento-ergo-box.pdf", pagesize=A4)
    width, height = A4
    
    # PAGE 1: Cover + Introduction
    # Background
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1)
    
    # Logo/Header
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(20*mm, height-40*mm, "ERGO BOX")
    
    c.setFillColor(AMBER)
    c.setFont("Helvetica", 12)
    c.drawString(20*mm, height-48*mm, "Mantenimiento especializado · Málaga")
    
    # Title
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(20*mm, height-80*mm, "Guía de Mantenimiento")
    c.drawString(20*mm, height-92*mm, "para Boxes de CrossFit")
    
    # Subtitle
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 14)
    c.drawString(20*mm, height-108*mm, "Checklist profesional para cuidar tu equipamiento")
    
    # Status legend
    y = height - 140*mm
    draw_status_legend(c, y)
    
    # Introduction text
    y = height - 180*mm
    c.setFillColor(INK)
    c.setFont("Helvetica", 11)
    
    intro_lines = [
        "Esta guía te ayuda a mantener tu equipamiento en perfecto estado y detectar",
        "problemas antes de que se conviertan en averías costosas.",
        "",
        "Cada equipo tiene su frecuencia de revisión: semanal, mensual o trimestral.",
        "Usa el sistema semáforo para evaluar el estado y priorizar acciones.",
        "",
        "Cuando dudes, mejor prevenir. Un mantenimiento a tiempo evita lesiones,",
        "quejas de atletas y gastos de reemplazo prematuros."
    ]
    
    for line in intro_lines:
        c.drawString(20*mm, y, line)
        y -= 7*mm
    
    # Footer
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "© 2026 ERGO BOX · hola@ergobox.es · @ergobox.es")
    
    c.showPage()
    
    # PAGE 2: RowErgs
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1)
    
    y = height - 30*mm
    draw_section_header(c, "1. RowErgs / Concept2", y, width)
    
    # Weekly
    y -= 20*mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "SEMANAL")
    y -= 8*mm
    
    weekly_items = [
        "Limpiar asiento, manillar y reposapiés con paño húmedo",
        "Aspirar el ventilador y eliminar acumulación de polvo",
        "Comprobar que la cadena se mueve suavemente",
        "Verificar que el monitor se enciende correctamente",
        "Revisar que no hay ruidos extraños al remar"
    ]
    
    for item in weekly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Monthly
    y -= 10*mm
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "MENSUAL")
    y -= 8*mm
    
    monthly_items = [
        "Limpiar los raíles con paño seco y lubricar ligeramente",
        "Comprobar tensión de la cadena (debe tener algo de juego)",
        "Limpiar la carcasa del ventilador por dentro",
        "Verificar que el asiento se desliza suavemente",
        "Comprobar estabilidad de la máquina"
    ]
    
    for item in monthly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Quarterly
    y -= 10*mm
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "TRIMESTRAL")
    y -= 8*mm
    
    quarterly_items = [
        "Desmontar y limpiar completamente el ventilador",
        "Cambiar las pilas del monitor si es necesario",
        "Revisar tornillería y apretar si es necesario",
        "Comprobar el estado de los cables internos"
    ]
    
    for item in quarterly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Warning box
    y -= 15*mm
    c.setFillColor(HexColor('#fff3cd'))
    c.rect(20*mm, y-45*mm, width-40*mm, 45*mm, fill=1)
    
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y-8*mm, "⚠ SEÑALES DE ALARMA")
    
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    warnings = [
        "• Chirridos → Cadena o raíles necesitan lubricación",
        "• Asiento que se atasca → Raíles sucios o desalineados",
        "• Monitor que se apaga → Batería baja o conexión defectuosa",
        "• Vibración excesiva → Ventilador desbalanceado o tornillos flojos"
    ]
    
    wy = y - 15*mm
    for warning in warnings:
        c.drawString(25*mm, wy, warning)
        wy -= 5*mm
    
    # Footer
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "© 2026 ERGO BOX · Página 2 de 5")
    
    c.showPage()
    
    # PAGE 3: Barbells
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1)
    
    y = height - 30*mm
    draw_section_header(c, "2. Barras Olímpicas", y, width)
    
    # Weekly
    y -= 20*mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "SEMANAL")
    y -= 8*mm
    
    weekly_items = [
        "Limpiar con cepillo de cerdas duras para mantener el knurling",
        "Secar completamente después de cada uso intenso",
        "Inspeccionar visualmente en busca de óxido o daños",
        "Comprobar que giran correctamente los extremos"
    ]
    
    for item in weekly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Monthly
    y -= 10*mm
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "MENSUAL")
    y -= 8*mm
    
    monthly_items = [
        "Aplicar aceite protector en las zonas sin knurling",
        "Desmontar collares si es posible y limpiar roscas",
        "Comprobar rectitud de la barra (rodar sobre superficie plana)",
        "Revisar estado de los rodamientos internos"
    ]
    
    for item in monthly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Danger box
    y -= 15*mm
    c.setFillColor(HexColor('#f8d7da'))
    c.rect(20*mm, y-55*mm, width-40*mm, 55*mm, fill=1)
    
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(25*mm, y-8*mm, "🚨 PELIGROS CRÍTICOS EN BARRAS")
    
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    dangers = [
        "• Óxido avanzado → Compromete la resistencia estructural",
        "• Barra torcida → Riesgo de lesiones por desequilibrio",
        "• Knurling gastado → Pérdida de agarre, peligroso en levantamientos",
        "• Extremos que no giran → Estrés excesivo en muñecas y antebrazos"
    ]
    
    dy = y - 15*mm
    for danger in dangers:
        c.drawString(25*mm, dy, danger)
        dy -= 6*mm
    
    # Footer
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "© 2026 ERGO BOX · Página 3 de 5")
    
    c.showPage()
    
    # PAGE 4: BikeErg & SkiErg
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1)
    
    y = height - 30*mm
    draw_section_header(c, "3. BikeErg", y, width)
    
    # Weekly
    y -= 20*mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "SEMANAL")
    y -= 8*mm
    
    weekly_items = [
        "Limpiar el exterior del ventilador con paño seco",
        "Comprobar que los pedales giran sin juego excesivo",
        "Verificar que el monitor se enciende correctamente",
        "Escuchar: ruidos de roce = algo se ha movido"
    ]
    
    for item in weekly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Monthly
    y -= 10*mm
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "MENSUAL")
    y -= 8*mm
    
    monthly_items = [
        "Abrir la carcasa y aspirar el polvo del ventilador",
        "Comprobar tensión de la cadena y lubricar si chirría",
        "Revisar estado de la batería del monitor",
        "Apretar pedales y bielas si hay holgura"
    ]
    
    for item in monthly_items:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # SkiErg section
    y -= 15*mm
    draw_section_header(c, "4. SkiErg", y, width)
    
    # Weekly
    y -= 20*mm
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(20*mm, y, "SEMANAL")
    y -= 8*mm
    
    sk_weekly = [
        "Limpiar las cuerdas con paño ligeramente húmedo",
        "Comprobar que las poleas giran suave y sin ruido",
        "Verificar que el monitor registra bien cada tirón",
        "Revisar que los agarres no tienen grietas"
    ]
    
    for item in sk_weekly:
        draw_checklist_item(c, item, y)
        y -= 7*mm
    
    # Footer
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "© 2026 ERGO BOX · Página 4 de 5")
    
    c.showPage()
    
    # PAGE 5: Calendar + Contact
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1)
    
    y = height - 30*mm
    draw_section_header(c, "Calendario de Mantenimiento", y, width)
    
    # Table header
    y -= 20*mm
    c.setFillColor(INK)
    c.rect(20*mm, y-8*mm, width-40*mm, 10*mm, fill=1)
    
    c.setFillColor(PAPER)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm, y-4*mm, "EQUIPAMIENTO")
    c.drawString(80*mm, y-4*mm, "SEMANAL")
    c.drawString(115*mm, y-4*mm, "MENSUAL")
    c.drawString(150*mm, y-4*mm, "TRIMESTRAL")
    
    # Table rows
    y -= 15*mm
    table_data = [
        ("RowErg", "Limpieza básica", "Cadena y raíles", "Revisión completa"),
        ("Barras", "Cepillado", "Aceite protector", "Rodamientos"),
        ("BikeErg", "Ventilador", "Cadena y batería", "Revisión completa"),
        ("SkiErg", "Cuerdas y poleas", "Tensión cuerda", "—")
    ]
    
    c.setFillColor(INK)
    c.setFont("Helvetica", 9)
    
    for equipment, weekly, monthly, quarterly in table_data:
        # Alternating row background
        if table_data.index((equipment, weekly, monthly, quarterly)) % 2 == 0:
            c.setFillColor(HexColor('#f9f9f9'))
            c.rect(20*mm, y-6*mm, width-40*mm, 8*mm, fill=1)
        
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(25*mm, y, equipment)
        c.setFont("Helvetica", 8)
        c.drawString(80*mm, y, weekly)
        c.drawString(115*mm, y, monthly)
        c.drawString(150*mm, y, quarterly)
        
        y -= 8*mm
    
    # Contact box
    y -= 30*mm
    c.setFillColor(INK)
    c.rect(20*mm, y-70*mm, width-40*mm, 70*mm, fill=1)
    
    c.setFillColor(AMBER)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30*mm, y-12*mm, "¿Necesitas ayuda profesional?")
    
    c.setFillColor(PAPER)
    c.setFont("Helvetica", 11)
    contact_lines = [
        "En ERGO BOX somos especialistas en mantenimiento de boxes de CrossFit.",
        "",
        "PRIMERA REVISIÓN DE UN ERG COMPLETAMENTE GRATIS",
        "",
        "📧 hola@ergobox.es",
        "📱 634 440 253",
        "💬 WhatsApp · wa.me/34634440253",
        "📍 Málaga y alrededores",
        "📷 @ergobox.es",
        "",
        "\"Tus coaches entrenan. Del equipo nos encargamos nosotros.\""
    ]
    
    cy = y - 20*mm
    for line in contact_lines:
        if "PRIMERA REVISIÓN" in line:
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(AMBER)
        elif line.startswith("\""):
            c.setFont("Helvetica-Oblique", 10)
            c.setFillColor(PAPER)
        else:
            c.setFont("Helvetica", 10)
            c.setFillColor(PAPER)
        
        c.drawString(30*mm, cy, line)
        cy -= 6*mm
    
    # Footer
    c.setFillColor(STEEL)
    c.setFont("Helvetica", 9)
    c.drawString(20*mm, 20*mm, "© 2026 ERGO BOX · Página 5 de 5 · ergobox.es")
    
    c.save()
    print("✅ PDF generated: /home/hermes/ergo-box-website/guia-mantenimiento-ergo-box.pdf")

if __name__ == "__main__":
    create_pdf()
