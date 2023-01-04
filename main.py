import discord
import os
from dotenv import load_dotenv
from insult_generator import hit_me
from jobtitlegenerator import get_job_title

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

SERVER_ID = int(os.getenv("DRAGUVE_SERVERID"))
ROLE_ID =  int(os.getenv("DRAGUVE_ROLEID"))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    server = client.get_guild(SERVER_ID)
    role = discord.utils.get(server.roles, id=ROLE_ID)
    await role.edit(name = f"{get_job_title()} Of Comedy", reason="Because I Am")

client.run(os.getenv('TOKEN'))
