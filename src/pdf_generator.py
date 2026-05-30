import os
import qrcode

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from src.layouts import (
    SINGLE_LABEL_LAYOUT,
    FOUR_LINE_LAYOUT,
    FIVE_LINE_LAYOUT
)
from src.paths import resource_path

def generate_pdf_einzeln(text_vis, qr_data, output, zeilen):
        if zeilen == 4:
            layout_profile = FOUR_LINE_LAYOUT
            text_y = landscape(A4)[1] - 100 - 56.6929 - 28.3465
        else:
            layout_profile = FIVE_LINE_LAYOUT
            text_y = landscape(A4)[1] - 100 - 56.6929
        font_sizes = layout_profile["font_sizes"]
        
        border_color = colors.Color(0/255,112/255,60/255)
        pdf = canvas.Canvas(output, pagesize=landscape(A4))
        width, height = landscape(A4)

        # Rahmen
        margin = SINGLE_LABEL_LAYOUT["margin"]
        pdf.setStrokeColor(border_color)
        pdf.setLineWidth(SINGLE_LABEL_LAYOUT["border_width"])
        pdf.rect(margin, margin, width-2*margin, height-2*margin)

        # Visueller Text
        text_x = 50
        left_width = width/2-50
        lines = text_vis.split()
        for i, line in enumerate(lines):
            size = font_sizes[min(i, len(font_sizes)-1)]
            pdf.setFont("Times-Bold", size)
            tw = pdf.stringWidth(line, "Times-Bold", size)
            if zeilen == 5 and (i==len(lines)-1 or i==4):
                text_y += 28.3465
            pdf.drawString(text_x+(left_width-tw)/2, text_y, line)
            text_y -= size+22.6772

        footer_text = "Erstellt: Fabian Wiese, generiert durch Lagerplatz-QRCode-Generator Version 1.0"
        pdf.setFont("Times-Roman",12)
        pdf.drawString(50,30, footer_text)

        # QR-Code
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=1)
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        tmp_qr = "temp_qr_single.png"; qr_img.save(tmp_qr)
        qr_max = min(width/2-50, height-200)
        qr_img = Image.open(tmp_qr).resize((int(qr_max),int(qr_max)), Image.LANCZOS)
        qr_x = width/2+50-42.5197-56.6929; qr_y = (height-qr_max)/2-28.3465
        pdf.drawImage(tmp_qr, qr_x, qr_y, qr_max, qr_max)
        os.remove(tmp_qr)

        # Firmenlogo
        logo_file = resource_path("assets/IMG_0060.jpeg")
        logo_img = Image.open(logo_file)
        logo_w=qr_max*0.5; logo_h=logo_w*logo_img.size[1]/logo_img.size[0]
        logo_img=logo_img.resize((int(logo_w),int(logo_h)), Image.LANCZOS)
        tmp_logo="temp_logo_single.png"; logo_img.save(tmp_logo)
        pdf.drawImage(tmp_logo, qr_x+(qr_max-logo_w)/2, qr_y+qr_max+10, logo_w, logo_h)
        os.remove(tmp_logo)
        pdf.showPage()
        pdf.save()
