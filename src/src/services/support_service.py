import urllib.parse
import webbrowser


def open_support_email():
    empfaenger = "fabian.wiese@schnellecke.com"
    betreff = "Supportanfrage für QR-Code Generator"
    body = (
        "Name:\n"
        "Vorname:\n"
        "Telefonnummer (optional):\n"
        "E-Mail-Adresse:\n"
        "Beschreibung / Verbesserungsvorschlag:\n\n"
        "Falls möglich, bitte ein Screenshot-Bild vom Fehler mit anhängen."
    )

    mailto_link = (
        f"mailto:{empfaenger}"
        f"?subject={urllib.parse.quote(betreff)}"
        f"&body={urllib.parse.quote(body)}"
    )

    webbrowser.open(mailto_link)