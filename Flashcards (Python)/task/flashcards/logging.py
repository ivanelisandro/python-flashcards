from io import StringIO

class Logger:
    def __init__(self):
        self.log = StringIO()

    def write(self, content:str):
        print(content)
        print(content, file=self.log)

    def get_content(self):
        return self.log.getvalue()