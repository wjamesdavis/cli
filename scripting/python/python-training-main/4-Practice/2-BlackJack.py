"""
Recreate a round from the card game 'Blackjack' (Also known as 21)
https://en.wikipedia.org/wiki/Blackjack

To make this easier, aces are always '11', ignore suits, and ignore the dealer. 
If you are feeling up to it, add support for a 2nd player, or for aces to be 1/11
"""

def getFullDeck():
    """
    This function returns 
    """
    cards = []
    for i in range(52):
        num = (i % 13) + 2
        if num > 11:
            num = 10
        cards.append(num)

    return cards
