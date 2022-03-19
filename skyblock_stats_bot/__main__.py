from config import GUILD_ID, TOKEN
from discord import app_commands
import discord


intents = discord.Intents.all()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}. Syncing commands..')
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print('Synced commands.')

@tree.command(guild=discord.Object(id=GUILD_ID))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong', ephemeral=True)


client.run(TOKEN)
