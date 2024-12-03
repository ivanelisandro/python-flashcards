from cards import CardCollectionFactory
from knowledge import KnowledgeTest

# stage 2:
# card = CardFactory.create()
# result = KnowledgeTest.verify(card)

# stage 3:
# cards = CardCollectionFactory.create()
# for card in cards:
#     result = KnowledgeTest.verify_with_answer(card)
#     print(result)

# stage 4:
collection = CardCollectionFactory.create_unique()
for card in collection.cards.values():
    result = KnowledgeTest.verify_with_collection(card, collection)
    print(result)
