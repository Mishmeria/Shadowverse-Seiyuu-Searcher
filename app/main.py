import sys
from PySide6.QtWidgets import QApplication
from ui_component import SearchWidget

def main():
    app = QApplication(sys.argv)
    win = SearchWidget()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
