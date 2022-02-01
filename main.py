import discord
import datetime
from discord.ext import tasks
import utilities

client = discord.Client()

TOKEN = utilities.load_token()


@client.event
async def on_ready():
    print("Online")
    actualizar_hora.start()


@tasks.loop(minutes=15)
async def actualizar_hora():
    channel = client.get_channel(937786586463084565)
    hora = "Hora servidor: " + datetime.datetime.now().strftime("%H:%M")
    await channel.edit(name=hora)

client.run(TOKEN)
