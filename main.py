import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

SERVER_ID = int(os.getenv("DRAGUVE_SERVERID"))
ROLE_ID =  int(os.getenv("DRAGUVE_ROLEID"))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    server = client.get_guild(SERVER_ID)
    print(server)
    role = discord.utils.get(server.roles, id=ROLE_ID)
    print(role)
    # This will get the role you want to edit
    # await role.edit(color=0x008000, reason="The reason")
    # role = discord.utils.get(guild.roles, id=os.getenv("DRAGUVE_ROLEID"))
    # print(role.members)
    # print(role.name)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
