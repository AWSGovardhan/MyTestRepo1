# Tight coupling between Python classes will look like :
class Saver:
    def __init__(self, file):
        self.filename = file

    def save(self, text):
        with open(self.filename, 'w') as file:
            file.write(text)


class DataFlow:
    def __init__(self, file):
        self.saver = Saver()
        self.filename = file
        self.text = ""

    def load(self):
        with open(self.filename, 'r') as file:
            self.text = file.read()


class Processor:
    def __init__(self, letter, filename):
        self.letter_to_remove = letter
        self.loader = DataFlow(filename)

    def process_text(self):
        self.loader.load()
        text = self.loader.text
        filtered_text = ""
        for char in text:
            if char == self.letter_to_remove:
                continue
            filtered_text += char
        self.loader.saver.save(filtered_text)
