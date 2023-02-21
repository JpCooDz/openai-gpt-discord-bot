import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import openai


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configuração do OpenAI API
openai.api_key = "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"
model_engine = "text-davinci-002"
openai_prompt = "Olá, eu sou o ChatGPT. Digite sua mensagem abaixo para começar a conversar comigo!\n\nUsuário:"
openai_response_start = "\nChatGPT:"

# Evento de início do bot
@bot.event
async def on_ready():
    print(f"{bot.user} está conectado ao Discord!")

# Comando !chatgpt
@bot.command(name="chatgpt")
async def chatgpt(ctx, *, user_message):
    # Usa o OpenAI API para gerar uma resposta
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
    await ctx.send(response_text)


# inicie o bot
bot.run('MTA3NjY1MDEyMTAxMTQxMzEyMw.GQcpxv.uTM3pJIiGEm5dGX4QpJV1wXr3505alB9tcI1pI')
