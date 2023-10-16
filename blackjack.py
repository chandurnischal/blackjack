import random
import matplotlib.pyplot as plt


class BlackJack:
    def __init__(self, deckNumber) -> None:
        self.deckNumber = deckNumber
        self.deck = dict()
        self.__setDeck()
        self.totalCards = sum(self.deck.values())

    def __setDeck(self) -> None:
        self.deck = dict.fromkeys([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4 * self.deckNumber)
        self.deck[10] = 16 * self.deckNumber

    def dealHand(self) -> list:
        hand = []
        for _ in range(2):
            card = random.choice(list(self.deck.keys()))
            hand.append(card)
            self.deck[card] -= 1

        return hand

    def __filterDeck(self) -> None:
        self.deck = {key: value for key, value in self.deck.items() if value != 0}
        currentCards = sum(self.deck.values())

        if currentCards < 0.30 * self.totalCards:
            self.__setDeck()

    def hit(self, hand: list) -> list:
        self.__filterDeck()
        card = random.choice(list(self.deck.keys()))
        self.deck[card] -= 1

        hand.append(card)
        hand = self.bestSum(hand)
        return hand

    def checkBust(self, hand: list) -> bool:
        return sum(hand) > 21

    def checkBlackJack(self, hand: list) -> bool:
        return sum(hand) == 21

    def bestSum(self, hand: list) -> list:
        for i, card in enumerate(hand):
            if card == 11 and self.checkBust(hand):
                hand[i] = 1
            else:
                hand[i] = card
        return hand
