import discord, random, os
print(os.listdir('images'))
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calcular(ctx, a: float, operador: str, b: float):
    if operador == "+":
        resultado = a + b
    elif operador == "-":
        resultado = a - b
    elif operador == "*":
        resultado = a * b
    elif operador == "/":
        if b == 0:
            await ctx.send("Não dá pra dividir por zero!")
            return
        resultado = a / b
    else:
        await ctx.send('Operador inválido! Digite "+", "-", "*" ou "/"')
        return

    await ctx.send(f"O resultado de {a} {operador} {b} é: **{resultado}**")

@bot.command()
async def meme(ctx):
    img-name:str = random.choice(os.listdir)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

bot.run("MTUwNjA3OTIzMzgwNDQ3MjM1MA.GDsxzo.QwXj8_82UhXdFz6O1TgSXGSRSW3hW3Rc_SgGZo")
