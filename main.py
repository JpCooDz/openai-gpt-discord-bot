import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

 # CHATGPT HELP

load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

# Configuração do OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"
openai_prompt = "Olá, eu sou o ChatGPT. Digite sua mensagem abaixo para começar a conversar comigo!\n\nUsuário:"
openai_response_start = "\nChatGPT:"

# Evento de início do bot
@bot.event
async def on_ready():
    print(f'{bot.user} está conectado ao Discord!')

# Evento de recebimento de mensagem
@bot.event
async def on_message(message):
    # Verifica se a mensagem foi enviada pelo próprio bot
    if message.author == bot.user:
        return

    # Verifica se a mensagem contém o comando "/chatgpt"
    if "/chatgpt" in message.content:
        # Separa a mensagem do usuário do comando "/chatgpt"
        user_message = message.content.replace("/chatgpt", "").strip()

        # Usa o OpenAI API para gerar uma resposta
        openai.api_key = 'OPENAI_API_KEY'
        response = openai.Completion.create(
            engine=model_engine,
            prompt=openai_prompt + user_message,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extrai a resposta gerada pelo OpenAI API
        response_text = response.choices[0].text
        response_text = response_text.replace(openai_response_start, "").strip()

        # Envia a resposta para o canal do Discord
        await message.channel.send(response_text)


bot.run('DISCORD_BOT_TOKEN')
