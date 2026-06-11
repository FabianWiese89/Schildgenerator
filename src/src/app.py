import tkinter as tk

from src.gui import QRCodeGeneratorApp

def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()