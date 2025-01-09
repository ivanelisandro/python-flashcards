from cards import Card, CardCollection

class KnowledgeTest:
    """
    Provides methods for testing your knowledge with previously defined cards.
    """
    @staticmethod
    def verify(card:Card):
        """
        Asks the user the answer for a card.
        :param card: The card to verify the answer for.
        :return: A text explaining if the user answer was correct or not.
        """
        answer = input()

        if card.verify(answer):
            return "Your answer is right!"

        return "Your answer is wrong..."

    @staticmethod
    def verify_with_answer(card: Card):
        """
        Asks the user the answer for a card.
        :param card: The card to verify the answer for.
        :return: A text explaining if the user answer was correct or not.
        """
        answer = input(f"Print the definition of \"{card.term}\":\n")

        if card.verify(answer):
            return "Correct!"

        return f"Wrong. The right answer is \"{card.definition}\"."

    @staticmethod
    def verify_with_collection(card: Card, card_collection: CardCollection):
        """
        Asks the user the answer for a card.
        :param card: The card to verify the answer for.
        :param card_collection: The collection of cards to take other existent definitions into account.
        :return: A text explaining if the user answer was correct or not.
        """
        answer = input()

        if card.verify(answer):
            return "Correct!"

        alternative_response = ""
        if card_collection.definition_exists(answer):
            alternative_term = card_collection.definitions[answer]
            alternative_response = f", but your definition is correct for \"{alternative_term}\""

        return f"Wrong. The right answer is \"{card.definition}\"{alternative_response}."



