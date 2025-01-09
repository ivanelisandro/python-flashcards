from cards import CardCollection
from knowledge import KnowledgeTest
from logging import Logger
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
        self.log = Logger()
        self.collection = CardCollection(self.log)
        self.actions = { "add": self.add_card,
                         "remove": self.remove_card,
                         "import": self.import_file,
                         "export": self.export_file,
                         "ask": self.test_random_cards,
                         "exit": self.finish,
                         "log": self.save_log,
                         "hardest card": self.print_hardest_card,
                         "reset stats": self.reset_statistics }

    def navigate(self):
        """
        Starts the menu of the application with all available functions.
        Ends the application loop if you type "exit".
        Ignores typed actions if they do not exist.
        """
        actions_list = ', '.join(self.actions.keys())
        while True:
            self.log.write(f"Input the action ({actions_list}):")
            action = input()

            if action in self.actions:
                self.actions[action]()

            if action == "exit":
                return

    def finish(self):
        """
        Prints a finalization message.
        """
        self.log.write("Bye bye!")

    def add_card(self):
        """
        Prompts the user with information for creating a card.
        """
        self.collection.try_create_card()

    def remove_card(self):
        """
        Removes a card by a specified "term".
        """
        self.log.write("Which card?")
        term = input()
        self.collection.remove(term)

    def import_file(self):
        """
        Imports a card collection from a file, keeping the existent ones.
        Definitions for existent cards are updated.
        """
        self.log.write("File name:")
        file_name = input()
        if not os.path.isfile(file_name):
            self.log.write("File not found.")
            return

        with open(file_name, "r", encoding='utf8') as file:
            json_data = file.read()
            cards_count = self.collection.set_json(json_data)
            self.log.write(f"{cards_count} cards have been loaded.")

    def export_file(self):
        """
        Exports the current card collection to a file.
        """
        self.log.write("File name:")
        file_name = input()
        with open(file_name, "w", encoding='utf8') as file:
            file.write(self.collection.get_json())
            self.log.write(f"{len(self.collection.cards)} cards have been saved.")

    def test_random_cards(self):
        """
        Tests a random selection of cards with the number of repetitions selected by the user.
        """
        self.log.write(f"How many times to ask?")
        repetitions = int(input())
        while repetitions > 0:
            random_card = random.choice(list(self.collection.cards.values()))
            self.log.write(f"Print the definition of \"{random_card.term}\":")
            result = KnowledgeTest.verify_with_collection(random_card, self.collection)
            self.log.write(result)
            repetitions -= 1

    def save_log(self):
        """
        Exports the current console output to a file.
        """
        self.log.write("File name:")
        file_name = input()
        with open(file_name, "w", encoding='utf8') as file:
            file.write(self.log.get_content())
            self.log.write("The log has been saved.")

    def print_hardest_card(self):
        """
        Prints information about the hardest card.
        """
        self.log.write(self.collection.get_hardest())

    def reset_statistics(self):
        """
        Resets all statistics for the collection.
        """
        self.collection.reset_all_errors()
        self.log.write("Card statistics have been reset.")
