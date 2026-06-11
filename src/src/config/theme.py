BG_COLOR = "#9d9d9d"
BUTTON_COLOR = "#00703c"
BUTTON_TEXT_COLOR = "black"
NOTEBOOK_SELECTED_TAB_COLOR = "#bdbdbd"

ENTRY_TEXT_COLOR = "black"
ENTRY_CURSOR_COLOR = "black"

GUI_LOGO_PATH = "assets/Logo_trans.png"
GUI_LOGO_WIDTH = 250
GUI_LOGO_HEIGHT = 80
GUI_LOGO_RELX = 1.0
GUI_LOGO_RELY = 0.0
GUI_LOGO_ANCHOR = "ne"
MAIN_WINDOW_GEOMETRY = "810x600"
SEPARATOR_COLOR = "#6e6e6e"
VERSION_LABEL_TEXT = "© Fabian Wiese – Version 1.0 ⓘ"
FONT_TAB = ("Arial", 11, "bold")
FONT_TITLE = ("Arial", 12, "bold")
FONT_LABEL = ("Arial", 10)
FONT_VERSION = ("Arial", 10, "normal")
FONT_VERSION_HOVER = ("Arial", 10, "underline")
FONT_HINT = ("Arial", 9)
HINT_TEXT_COLOR = "darkblue"
APP_WINDOW_TITLE = "Lagerplatz-QRCode-Generator Version 1.0"
TAB_SINGLE_TITLE = "Einzelerstellung"
TAB_BATCH_TITLE = "Sammelverarbeitung"
STATUS_TEXT_COLOR = "blue"
VERSION_TEXT_COLOR = "black"
VERSION_HOVER_TEXT_COLOR = "white"

LAYOUT_OPTION_DEFAULT = "Bitte wählen..."
LAYOUT_OPTION_4_LINES = "4 Zeilen pro PDF-Seite"
LAYOUT_OPTION_5_LINES = "5 Zeilen pro PDF-Seite"

LAYOUT_OPTIONS = [
    LAYOUT_OPTION_DEFAULT,
    LAYOUT_OPTION_4_LINES,
    LAYOUT_OPTION_5_LINES,
]

VALID_LAYOUT_OPTIONS = [
    LAYOUT_OPTION_4_LINES,
    LAYOUT_OPTION_5_LINES,
]

SINGLE_TAB_TITLE_TEXT = "Ein einzelnes Lagerplatzschild generieren"
SINGLE_LAYOUT_LABEL_TEXT = "Wie viele Zeilen Text soll dein Lagerplatzetikett enthalten?"
SINGLE_STORAGE_LABEL_TEXT = "Lagerplatz (systemisch, mit Bindestrichen):"
SINGLE_OUTPUT_LABEL_TEXT = "Speicherort für das PDF:"

BATCH_TAB_TITLE_TEXT = "Lagerplatz-Schilder aus Excel-Datei generieren."
BATCH_LAYOUT_LABEL_TEXT = "Wie viele Zeilen Text soll dein Lagerplatzetikett enthalten?"
BATCH_EXCEL_LABEL_TEXT = "Excel-Datei auswählen:"
BATCH_OUTPUT_LABEL_TEXT = "Speicherort für die kombinierte PDF:"

BUTTON_BROWSE_TEXT = "Durchsuchen"
BUTTON_CREATE_PDF_TEXT = "PDF erstellen"
BUTTON_SUPPORT_TEXT = "Kontakt / Support"
BUTTON_MANUAL_TEXT = "Handbuch"
BUTTON_TEXT_SIGN_TEST_TEXT = "Textschild Test"

STATUS_READY_TEXT = "Bereit"
STATUS_CREATING_PDF_TEXT = "PDF wird erstellt..."
STATUS_DONE_TEXT = "Fertig"
MESSAGEBOX_DONE_TITLE = "Fertig"
MESSAGEBOX_PDF_CREATED_TEXT = "PDF erfolgreich erstellt:"

PDF_DEFAULT_EXTENSION = ".pdf"
PDF_FILE_TYPE_LABEL = "PDF-Dateien"
PDF_FILE_PATTERN = "*.pdf"

EXCEL_DIALOG_TITLE = "Excel-Datei wählen"
EXCEL_FILE_TYPE_LABEL = "Excel-Dateien"
EXCEL_FILE_PATTERN = "*.xlsx"

BATCH_HINT_NO_HEADER_TEXT = "• Es muss eine .xlsx-Datei ohne Überschrift verwendet werden."
BATCH_HINT_COLUMN_A_TEXT = "• Spalte A: Lagerplatz mit Leerzeichen (z. B. 05 H2 11 093 L)"
BATCH_HINT_COLUMN_B_TEXT = "• Spalte B: Lagerplatz mit Bindestrichen (z. B. 05-H2-11-093-L)"

SHOW_TEXT_SIGN_TEST_BUTTON = True