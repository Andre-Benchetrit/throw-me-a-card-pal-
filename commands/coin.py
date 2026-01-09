import random
from discord.ext import commands

results = [
    "Cara", "Coroa"
]

@commands.command(name="coin", help="Sorteia uma lado da moeda.")
async def coin(ctx):
    result = random.choice(results)
    await ctx.send(f"A moeda sorteada foi: {result}")
