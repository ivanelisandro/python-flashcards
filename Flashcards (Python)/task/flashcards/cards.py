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


class CardCollection:
    """
    Represents a flashcard that can be used to study any subject.
    """
    def __init__(self):
        self.cards = {}
        self.definitions = {}

    def add(self, card: Card):
        self.cards[card.term] = card
        self.definitions[card.definition] = card.term

    def term_exists(self, term:str):
        return term in self.cards

    def definition_exists(self, definition:str):
        return definition in self.definitions


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


class CardCollectionFactory:
    """
    Provides methods for creating collections of flashcards to study.
    """
    @staticmethod
    def create() -> list[Card]:
        """
        Collects user inputs for a collection of flashcards.
        :return: a collection of Cards from the user inputs.
        """
        quantity = int(input("Input the number of cards:\n"))
        cards = []

        for item_number in range(1, quantity + 1):
            term = input(f"The term for card #{item_number}:\n")
            definition = input(f"The definition for card #{item_number}:\n")
            cards.append(Card(term, definition))
        return cards

    @staticmethod
    def create_unique() -> CardCollection:
        """
        Collects user inputs for a collection of flashcards.
        :return: a collection of Cards from the user inputs.
        """
        quantity = int(input("Input the number of cards:\n"))
        collection = CardCollection()

        for item_number in range(1, quantity + 1):
            term = input(f"The term for card #{item_number}:\n")
            while collection.term_exists(term):
                term = input(f"The term \"{term}\" already exists. Try again:\n")

            definition = input(f"The definition for card #{item_number}:\n")
            while collection.definition_exists(definition):
                definition = input(f"The definition \"{definition}\" already exists. Try again:\n")

            collection.add(Card(term, definition))
        return collection