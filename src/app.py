import tkinter as tk

from src.gui.main_window import QRCodeGeneratorApp


def main():
    root = tk.Tk()
    QRCodeGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
