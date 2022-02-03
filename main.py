import discord
import os
import nltk
from dotenv import load_dotenv
from neuralintents import GenericAssistant

load_dotenv()

client = discord.Client()

chattrap = GenericAssistant('intents.json')
chattrap.train_model()
chattrap.save_model()

TOKEN = os.getenv('TOKEN')
# TOKEN = 'OTM4MDU4ODE0ODc0MzI1MDAy.YfkxWQ.UtjEUio2s51g20lb2JouxkkxvLE'

@client.event
async def on_connect():
    print("Olá? Olá olá? Acho que dormi demais")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ct'):
        responses = chattrap.request(message.content[3:])
        await message.channel.send(responses)


client.run(TOKEN)