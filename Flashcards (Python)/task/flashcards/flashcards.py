from cards import CardFactory
from knowledge import KnowledgeTest

card = CardFactory.create()
result = KnowledgeTest.verify(card)
print(result)
