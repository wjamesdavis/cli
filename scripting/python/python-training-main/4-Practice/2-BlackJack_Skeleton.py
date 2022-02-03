"""
Recreate a round from the card game 'Blackjack' (Also known as 21)
https://en.wikipedia.org/wiki/Blackjack

To make this easier, treat aces as always being '11', ignore suits, and ignore the dealer
"""

def getFullDeck():
    cards = []
    for i in range(52):
        num = (i % 13) + 2
        if num > 11:
            num = 10
        cards.append(num)

    return cards


def hit(deck):
    """
    Recieves a deck of cards
    On call, a single card is picked, removed from the list, and returned
    """
    # Write Code Here



if __name__ == "__main__":