import tkinter as tk

from tkinter import ttk
from src.gui.release_notes_window import ReleaseNotesWindow
from src.gui.handbuch_window import HandbuchWindow
from src.gui.single_tab import build_single_tab
from src.gui.batch_tab import build_batch_tab
from src.gui.single_actions import (
    update_single_button as handle_update_single_button,
    single_save_pdf as handle_single_save_pdf,
    on_single_generate as handle_on_single_generate,
)
from src.gui.batch_actions import (
    update_batch_button as handle_update_batch_button,
    browse_batch_excel as handle_browse_batch_excel,
    save_batch_pdf as handle_save_batch_pdf,
    on_batch_generate as handle_on_batch_generate,
)
from src.gui.gui_helpers import (
    add_logo_to_frame as helper_add_logo_to_frame,
    add_handbook_button as helper_add_handbook_button,
    add_support_button as helper_add_support_button,
    add_browse_button as helper_add_browse_button,
    add_layout_combobox as helper_add_layout_combobox,
    add_create_pdf_button as helper_add_create_pdf_button,
    add_status_label as helper_add_status_label,
    add_text_entry as helper_add_text_entry,
)
from src.services import open_support_email

from src.config import (
    BG_COLOR,
    NOTEBOOK_SELECTED_TAB_COLOR,
    MAIN_WINDOW_GEOMETRY,
    SEPARATOR_COLOR,
    VERSION_LABEL_TEXT,
    FONT_TAB,
    FONT_VERSION,
    FONT_VERSION_HOVER,
    APP_WINDOW_TITLE,
    TAB_SINGLE_TITLE,
    TAB_BATCH_TITLE,
    VERSION_TEXT_COLOR,
    VERSION_HOVER_TEXT_COLOR,
    LAYOUT_OPTION_DEFAULT,
)
# ==== HAUPTFENSTER ====
class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_WINDOW_TITLE)
        self.root.geometry(MAIN_WINDOW_GEOMETRY)
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # Tabs
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background=BG_COLOR, font=FONT_TAB, padding=[16, 6])
        style.map('TNotebook.Tab', background=[('selected', NOTEBOOK_SELECTED_TAB_COLOR)])

        self.notebook = ttk.Notebook(root)
        self.tab_single = tk.Frame(self.notebook, bg=BG_COLOR)
        self.tab_batch = tk.Frame(self.notebook, bg=BG_COLOR)
        self.notebook.add(self.tab_single, text=TAB_SINGLE_TITLE)
        self.notebook.add(self.tab_batch, text=TAB_BATCH_TITLE)
        self.notebook.pack(fill="both", expand=True, padx=40, pady=28)

        # Trennstrich unter den Tabs
        separator = tk.Frame(root, bg=SEPARATOR_COLOR, height=2)
        separator.pack(fill="x", padx=30, pady=(0, 8))

        self.notebook.select(0)  # Einzelerstellung ist Standard

        self.init_single_variables()
        self.init_batch_variables()

        self.build_tab_single()
        self.build_tab_batch()
        self.build_version_label()

    # ==== VERSIONSLABEL UND RELEASE NOTES ====
    def build_version_label(self):
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.place(relx=0, rely=1.0, anchor="sw", x=12, y=-8)

        self.version_lbl = tk.Label(
            frame,
            text=VERSION_LABEL_TEXT,
            fg=VERSION_TEXT_COLOR,
            bg=BG_COLOR,
            font=FONT_VERSION,
            cursor="arrow"
        )
        self.version_lbl.pack(anchor="sw")
        self.version_lbl.bind("<Enter>", self._on_version_hover)
        self.version_lbl.bind("<Leave>", self._on_version_leave)
        self.version_lbl.bind("<Button-1>", self.show_release_notes)

    def _on_version_hover(self, event):
        self.version_lbl.config(fg=VERSION_HOVER_TEXT_COLOR, font=FONT_VERSION_HOVER, cursor="hand2")

    def _on_version_leave(self, event):
        self.version_lbl.config(fg=VERSION_TEXT_COLOR, font=FONT_VERSION, cursor="arrow")

    def show_release_notes(self, event=None):
        ReleaseNotesWindow(self.root)

    # ==== ALLGEMEINE GUI-HILFSMETHODEN ====
    def add_logo_to_frame(self, frame):
        helper_add_logo_to_frame(self, frame)

    def add_handbook_button(self, frame):
        helper_add_handbook_button(self, frame)

    def add_support_button(self, frame):
        helper_add_support_button(self, frame)

    def add_browse_button(self, frame, command, row):
        helper_add_browse_button(frame, command, row)

    def add_layout_combobox(self, frame, variable, row, pady):
        return helper_add_layout_combobox(frame, variable, row, pady)

    def add_create_pdf_button(self, frame, command):
        return helper_add_create_pdf_button(frame, command)

    def add_status_label(self, frame):
        return helper_add_status_label(frame)

    def add_text_entry(self, frame, variable, row, width):
        return helper_add_text_entry(frame, variable, row, width)

    def init_single_variables(self):
        self.single_lagerplatz = tk.StringVar()
        self.single_layout = tk.StringVar(value=LAYOUT_OPTION_DEFAULT)
        self.single_output = tk.StringVar()
        self.single_status = None
        self.single_btn_pdf = None


    # ==== EINZELERSTELLUNG ====
    def build_tab_single(self):
        build_single_tab(self)

    def update_single_button(self):
        handle_update_single_button(self)

    def single_save_pdf(self):
        handle_single_save_pdf(self)

    def on_single_generate(self):
        handle_on_single_generate(self)

    def init_batch_variables(self):
        self.batch_excel_path = tk.StringVar()
        self.batch_layout = tk.StringVar(value=LAYOUT_OPTION_DEFAULT)
        self.batch_output_path = tk.StringVar()
        self.batch_status = None
        self.batch_btn_pdf = None

    # ==== SAMMELVERARBEITUNG ====
    def build_tab_batch(self):
        build_batch_tab(self)

    def update_batch_button(self):
        handle_update_batch_button(self)

    def browse_batch_excel(self):
        handle_browse_batch_excel(self)

    def save_batch_pdf(self):
        handle_save_batch_pdf(self)

    def on_batch_generate(self):
        handle_on_batch_generate(self)

    def show_handbuch(self):
        HandbuchWindow(self.root)

    def open_email(self):
        open_support_email()

