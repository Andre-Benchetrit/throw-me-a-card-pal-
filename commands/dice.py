from logic.dice_logic import roll_expression

async def on_message(message):
    if message.author.bot:
        return
    
    content = message.content.lower()

    if not content.startswith("?"):
        return
    
    expr = content[1:].strip()

    result = roll_expression(expr)

    if result.is_error():
        await message.reply(
            f"⚠️ {result.error}",
            mention_author=False
        )
        return

    if not result.detalhes:
        return
    
    await message.reply(
                "🎲 **Rolagem de dados**\n"
        + "\n".join(result.detalhes)
        + f"\n\n**Total: {result.total}**",
        mention_author=False
    )