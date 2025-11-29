import requests
from django.core.mail import EmailMessage
from bs4 import BeautifulSoup
from django.conf import settings
def hacer_scraping(keyword):
    url = f"https://es.wikipedia.org/wiki/{keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    resultados = []
    for i, p in enumerate(soup.select('p'), start=1):
        texto = p.get_text(strip=True)
        if texto:
            resultados.append({'id': i, 'contenido': texto})
        if len(resultados) >= 5:
            break
    print("✅ Resultados extraídos:", resultados)
    return resultados

def enviar_resultados_por_mail(resultados, destinatario):
    cuerpo = "Resultados del scraping:\n\n"
    for r in resultados:
        cuerpo += f"{r['id']}. {r['contenido']}\n\n"

    try:
        email = EmailMessage(
            subject="Resultados del scraping educativo",
            body=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[destinatario],
            
        )
        email.send(fail_silently=False)
    except Exception as e:
        print(f"Error al enviar resultados por correo: {e}")