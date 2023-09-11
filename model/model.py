import json
from datetime import datetime


class NotesApp:
    def __init__(self, path: str = 'phones.json'):
        self.notes: dict = {}
        self.path = path

    def get(self, index: int | None = None):
        if index:
            return self.notes.get(index)
        return self.notes

    def open(self):
        try:
            with open(self.path, 'r', encoding="UTF-8") as f:
                self.notes = json.load(f)
            return True
        except:
            return False

    def save(self):
        try:
            with open(self.path, 'w', encoding="UTF-8") as f:
                json.dump(self.notes, f, indent=4, ensure_ascii=False)
            return True
        except:
            return False

    def find(self, word: str) -> dict[int:dict[str, str, datetime]]:
        result = {}
        for index, note in self.notes.items():
            if word.lower() in ''.join(note.values()).lower():
                result[index] = note
                return result

