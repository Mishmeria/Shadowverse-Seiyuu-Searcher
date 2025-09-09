from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QListWidget, QLabel
)
import search_service

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seiyuu Search")
        self.resize(500, 400)

        layout = QVBoxLayout(self)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type card name…")
        self.input.textChanged.connect(self.on_text_changed)

        self.listbox = QListWidget()
        self.listbox.itemClicked.connect(self.on_item_clicked)

        self.result = QLabel("CV: ")
        self.result.setWordWrap(True)

        layout.addWidget(self.input)
        layout.addWidget(self.listbox)
        layout.addWidget(self.result)

    def on_text_changed(self, text):
        self.listbox.clear()
        for c in search_service.suggest_names(text):
            self.listbox.addItem(c["name_en"])

    def on_item_clicked(self, item):
        name = item.text()
        cv = search_service.get_cv(name)
        self.result.setText(f"CV: {cv or 'N/A'}")
