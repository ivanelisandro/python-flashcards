class Card:
    """
    Represents a flashcard that can be used to study any subject.
    """
    def __init__(self, term:str, definition:str):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return "\n".join((f"Card: {self.term}", f"Definition: {self.definition}"))

    def verify(self, answer:str):
        return self.definition == answer


class CardFactory:
    """
    Provides methods for creating flashcards to study.
    """
    @staticmethod
    def create():
        """
        Collects user inputs for a flashcard.
        :return: a new instance of Card from the user inputs.
        """
        term = input()
        definition = input()
        return Card(term, definition)