from cards import CardCollection
from knowledge import KnowledgeTest
import os.path
import random


class DeckManager:
    """
    Provides a menu with access to all required functions to use the flashcards as a study method.
    Functions available:
    - add a card to your study deck;
    - remove a card by "term";
    - import a file with cards;
    - export current cards to a file;
    - keep asking for random cards to study for a number of "n" times;
    - exit the application;
    """
    def __init__(self):
        self.collection = CardCollection()
        self.actions = { "add": self.add_card,
                         "remove": self.remove_card,
                         "import": self.import_file,
                         "export": self.export_file,
                         "ask": self.test_random_cards}

    def navigate(self):
        """
        Starts the menu of the application with all available functions.
        Ends the application loop if you type "exit".
        Ignores typed actions if they do not exist.
        """
        actions_list = ', '.join((*self.actions.keys(), "exit"))
        while True:
            action = input(f"Input the action ({actions_list}):\n")
            if action == "exit":
                print("Bye bye!")
                return

            if action in self.actions:
                self.actions[action]()

    def add_card(self):
        """
        Prompts the user with information for creating a card.
        """
        self.collection.try_create_card()

    def remove_card(self):
        """
        Removes a card by a specified "term".
        """
        term = input("Which card?\n")
        self.collection.remove(term)

    def import_file(self):
        """
        Imports a card collection from a file, keeping the existent ones.
        Definitions for existent cards are updated.
        """
        file_name = input("File name:\n")
        if not os.path.isfile(file_name):
            print("File not found.")
            return

        with open(file_name, "r", encoding='utf8') as file:
            json_data = file.read()
            cards_count = self.collection.set_json(json_data)
            print(f"{cards_count} cards have been loaded.")

    def export_file(self):
        """
        Exports the current card collection to a file.
        """
        file_name = input("File name:\n")
        with open(file_name, "w", encoding='utf8') as file:
            file.write(self.collection.get_json())
            print(f"{len(self.collection.cards)} cards have been saved.")

    def test_random_cards(self):
        """
        Tests a random selection of cards with the number of repetitions selected by the user.
        """
        repetitions = int(input(f"How many times to ask?\n"))
        while repetitions > 0:
            random_card = random.choice(list(self.collection.cards.values()))
            result = KnowledgeTest.verify_with_collection(random_card, self.collection)
            print(result)
            repetitions -= 1
