import random
from collections import defaultdict
cards = [
    "A ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥",
    "A ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦",
    "A ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣",
    "A ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠",
    "Joker!"
]

special_cards = [
    "Joker!"
]

def normalize_card_name(card: str) -> str:
    return (
        card.lower()
        .replace(" ", "_")
        .replace("♠", "spades")
        .replace("♥", "hearts")
        .replace("♦", "diamonds")
        .replace("♣", "clubs")
    )

deck = defaultdict(list)

def card_throw(server_id):
    
    if not deck[server_id]:
        deck[server_id] = cards.copy()
        random.shuffle(deck[server_id])

    card = deck[server_id].pop()
    is_special = card in special_cards

    return card, len(deck[server_id]), is_special

def card_shuffle(server_id) -> int:
    deck[server_id].clear()
    deck[server_id].extend(cards)
    random.shuffle(deck[server_id])
    return len(deck[server_id])