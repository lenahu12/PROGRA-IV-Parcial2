from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generar_pdf_alumno(alumno):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)

    p.drawString(100, 750, f"Ficha del Alumno")
    p.drawString(100, 720, f"Nombre: {alumno.nombre}")
    p.drawString(100, 700, f"Edad: {alumno.edad}")
    p.drawString(100, 680, f"Email: {alumno.email}")

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer