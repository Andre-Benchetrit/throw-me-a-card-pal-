from discord.ext import commands
from logic.card_logic import card_throw, card_shuffle, normalize_card_name
from utils.voice import play_audio
@commands.command(name="card", help="Sorteia uma carta aleatória.")
async def card(ctx):
    drawn_card, cards_left, is_special = card_throw()

    await ctx.send(f"A carta sorteada foi: {drawn_card}\nCartas restantes no baralho: {cards_left}")
    if is_special:
        filename = normalize_card_name(drawn_card)
        await play_audio(ctx, f"music/{filename}.mp3")

@commands.command(name="shuffle", help="Embaralha o baralho.")
async def shuffle(ctx):
    from logic.card_logic import deck, cards
    deck.clear()
    deck.extend(cards)
    import random
    random.shuffle(deck)
    await ctx.send(f"O baralho foi embaralhado. Total de cartas no baralho: {len(deck)}")