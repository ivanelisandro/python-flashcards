class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return "\n".join((f"Card: {self.term}", f"Definition: {self.definition}"))


class CardFactory:
    @staticmethod
    def create():
        term = input("Card:\n")
        print(term)
        definition = input("Definition:\n")
        print(definition)
        return Card(term, definition)


CardFactory.create()
