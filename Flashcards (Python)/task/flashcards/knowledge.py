from cards import Card


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
