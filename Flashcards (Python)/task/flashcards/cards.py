import json

class Card(object):
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


class CardCollection(object):
    """
    Represents a flashcard that can be used to study any subject.
    """
    def __init__(self, cards = None, definitions = None):
        self.cards = {} if cards is None else cards
        self.definitions = {} if definitions is None else definitions

    def add(self, card: Card):
        self.cards[card.term] = card
        self.definitions[card.definition] = card.term

    def remove(self, term):
        if term not in self.cards:
            print(f"Can't remove \"{term}\": there is no such card.")
            return

        definition = self.cards[term].definition
        self.cards.pop(term)
        self.definitions.pop(definition)
        print("The card has been removed.")

    def term_exists(self, term:str):
        return term in self.cards

    def definition_exists(self, definition:str):
        return definition in self.definitions

    def try_create_card(self):
        term = input(f"The card:\n")
        while self.term_exists(term):
            term = input(f"The term \"{term}\" already exists. Try again:\n")

        definition = input(f"The definition of the card:\n")
        while self.definition_exists(definition):
            definition = input(f"The definition \"{definition}\" already exists. Try again:\n")

        self.add(Card(term, definition))
        print(f"The pair (\"{term}\":\"{definition}\") has been added.")

    def get_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def set_json(self, json_text:str):
        read_collection = CardCollection(**json.loads(json_text))
        for card_json in read_collection.cards.values():
            self.add(Card(**card_json))

        return len(read_collection.cards)


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