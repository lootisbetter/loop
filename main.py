import discord
from discord.ext import commands
from webserver import keep_alive
# we have to downgrade the version if discord.py
client = commands.Bot(command_prefix=">",
                      intents=discord.Intents.all(),
                      self_bot=True)

# we have successfully logged in! gg now we have to make it 24/7


@client.event
async def on_ready():
  print("Logged in as {}".format(client.user))


keep_alive()
client.run(
  " Token ",
  bot=False)
