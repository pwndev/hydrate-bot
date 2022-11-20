import os
import discord
from database import Database

bot = discord.Bot()
db = Database("hydrate-bot.db")

@bot.event
async def on_ready():
  print("Connected to Discord gateway!")

@bot.slash_command(description="Enable reminder notifications")
async def remindme(interaction: discord.ApplicationContext):
  try:
    db.opt_in(interaction.user.id)
    await interaction.respond("✅ You will now receive hydration reminders.", ephemeral=True)
  except:
    await interaction.respond("⚠ You already receive reminders. Use </stop:1043934491686752357> to disable notifications.", ephemeral=True)

@bot.slash_command(description="Disable reminder notifications")
async def stop(interaction: discord.ApplicationContext):
  reminders_disabled = db.get_user(interaction.user.id) == None

  if reminders_disabled:
    return await interaction.respond("⚠ You currently don't receive reminders. Use </remindme:1043934491686752356> to enable notifications.", ephemeral=True)

  db.opt_out(interaction.user.id)
  await interaction.respond("✅ You will now no longer receive hydration reminders.", ephemeral=True)

@bot.slash_command(description="Show all users that opted-in for hydration reminders.")
async def show(interaction: discord.ApplicationContext):
  users = db.get_users()
  content = "\n".join(map(lambda user_tuple: f"<@{user_tuple[0]}>", users))
  await interaction.respond(f"**All opted-in users:** *({len(users)})*\n\n" + content, ephemeral=True)

def main():
  db.create_tables()
  bot.run(os.environ["BOT_TOKEN"])
  db.connection.close()
  
if __name__ == "__main__":
  main()
