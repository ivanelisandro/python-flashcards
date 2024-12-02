from cards import CardFactory
from knowledge import KnowledgeTest

# stage 2:
# card = CardFactory.create()
# result = KnowledgeTest.verify(card)

# stage 3:
cards = CardFactory.create_collection()
for card in cards:
    result = KnowledgeTest.verify_with_answer(card)
    print(result)
