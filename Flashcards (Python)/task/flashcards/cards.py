from logging import Logger
import json

class Card(object):
    """
    Represents a flashcard that can be used to study any subject.
    """
    def __init__(self, term:str, definition:str, mistakes:int = 0):
        self.term = term
        self.definition = definition
        self.mistakes = mistakes

    def __repr__(self):
        return "\n".join((f"Card: {self.term}", f"Definition: {self.definition}", f"Mistakes: {self.mistakes}"))

    def verify(self, answer:str):
        is_correct = self.definition == answer
        if not is_correct:
            self.mistakes += 1

        return is_correct

    def reset_errors(self):
        self.mistakes = 0


class CardCollection(object):
    """
    Represents a flashcard that can be used to study any subject.
    """
    def __init__(self, log:Logger, cards = None, definitions = None):
        self.log = log
        self.cards = {} if cards is None else cards
        self.definitions = {} if definitions is None else definitions

    def add(self, card: Card):
        self.cards[card.term] = card
        self.definitions[card.definition] = card.term

    def remove(self, term):
        if term not in self.cards:
            self.log.write(f"Can't remove \"{term}\": there is no such card.")
            return

        definition = self.cards[term].definition
        self.cards.pop(term)
        self.definitions.pop(definition)
        self.log.write("The card has been removed.")

    def term_exists(self, term:str):
        return term in self.cards

    def definition_exists(self, definition:str):
        return definition in self.definitions

    def try_create_card(self):
        self.log.write("The card:")
        term = input()
        while self.term_exists(term):
            self.log.write(f"The term \"{term}\" already exists. Try again:")
            term = input()

        self.log.write(f"The definition of the card:")
        definition = input()
        while self.definition_exists(definition):
            self.log.write(f"The definition \"{definition}\" already exists. Try again:")
            definition = input()

        self.add(Card(term, definition))
        self.log.write(f"The pair (\"{term}\":\"{definition}\") has been added.")

    def get_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def set_json(self, json_text:str):
        read_collection = CardCollection(**json.loads(json_text))
        for card_json in read_collection.cards.values():
            self.add(Card(**card_json))

        return len(read_collection.cards)

    def get_hardest(self):
        no_errors = "There are no cards with errors."

        if len(self.cards) == 0:
            return no_errors

        highest_errors = max(card.mistakes for card in self.cards.values())
        if highest_errors == 0:
            return no_errors

        hardest_cards = [f"\"{card.term}\"" for card in self.cards.values() if card.mistakes == highest_errors]

        errors_quantity = "error" if highest_errors == 1 else "errors"

        terms = ", ".join(hardest_cards)
        if len(hardest_cards) == 1:
            return f"The hardest card is {terms}. You have {highest_errors} {errors_quantity} answering it."

        return f"The hardest cards are {terms}. You have {highest_errors} {errors_quantity} answering them."

    def reset_all_errors(self):
        for card in self.cards.values():
            card.reset_errors()


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
    def create(log:Logger) -> list[Card]:
        """
        Collects user inputs for a collection of flashcards.
        :return: a collection of Cards from the user inputs.
        """
        log.write("Input the number of cards:")
        quantity = int(input())
        cards = []

        for item_number in range(1, quantity + 1):
            log.write(f"The term for card #{item_number}:")
            term = input()
            log.write(f"The definition for card #{item_number}:")
            definition = input()
            cards.append(Card(term, definition))
        return cards

    @staticmethod
    def create_unique(log:Logger) -> CardCollection:
        """
        Collects user inputs for a collection of flashcards.
        :return: a collection of Cards from the user inputs.
        """
        log.write("Input the number of cards:")
        quantity = int(input())
        collection = CardCollection(log)

        for item_number in range(1, quantity + 1):
            log.write(f"The term for card #{item_number}:")
            term = input()
            while collection.term_exists(term):
                log.write(f"The term \"{term}\" already exists. Try again:")
                term = input()

            log.write(f"The definition for card #{item_number}:")
            definition = input()
            while collection.definition_exists(definition):
                log.write(f"The definition \"{definition}\" already exists. Try again:")
                definition = input()

            collection.add(Card(term, definition))
        return collection