import discord
from discord.ext import commands
from bot_token import token
from class_detection import detect_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    await ctx.send("Algılama başladı.")
    if ctx.message.attachments:
        await ctx.send("Resim kaydediliyor!")
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}" 
            await attachment.save(file_path)
            await ctx.send("Resim kaydedildi!")
            name, score = detect_class(file_path)
            await ctx.send(f"Bu bir {name.strip()}, bundan %{int(score*100)} eminim.")

    else:
        await ctx.send("Lütfen bir resim ekle")


bot.run(token)