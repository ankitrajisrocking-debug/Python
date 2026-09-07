import tkinter as tk

from database import create_tables
from gui import LibraryGUI


def main():
    create_tables()

    root = tk.Tk()
    LibraryGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()

