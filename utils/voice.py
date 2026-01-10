import discord

async def play_audio(ctx_or_message, path):
    voice = getattr(ctx_or_message.author, "voice", None)
    if not voice:
        return

    channel = voice.channel
    vc = channel.guild.voice_client
    if not vc:
        vc = await channel.connect()

    vc.play(discord.FFmpegPCMAudio(path))