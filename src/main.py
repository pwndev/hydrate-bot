import os
import discord

bot = discord.Bot()

@bot.event
async def on_ready():
  print('Connected to Discord gateway')

def main():
  print('Starting bot...')
  bot.run(os.environ['BOT_TOKEN'])
  
if __name__ == "__main__":
  main()
