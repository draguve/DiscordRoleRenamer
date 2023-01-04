import discord
import os
from dotenv import load_dotenv
from insult_generator import hit_me
from jobtitlegenerator import get_job_title
from discord.ext import tasks, commands

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

SERVER_ID = int(os.getenv("DRAGUVE_SERVERID"))
ROLE_ID = int(os.getenv("DRAGUVE_ROLEID"))
DAN_ID = int(os.getenv("DAN_ID"))


class Renamer(commands.Cog):
    def __init__(self):
        self.index = 0
        self.renamer.start()

    def cog_unload(self):
        self.renamer.cancel()

    @tasks.loop(hours=1.0)
    async def renamer(self):
        server = client.get_guild(SERVER_ID)
        role = discord.utils.get(server.roles, id=ROLE_ID)
        role_name = f"{get_job_title()}Of Comedy"
        if role is not None:
            await role.edit(name=role_name, reason="Because I Am")
        dan_name = hit_me()
        dan = server.get_member(DAN_ID)
        # if dan is not None:
        await dan.edit(nick=dan_name)
        print(f"changed role to {role_name} and danny to {dan_name}")
        self.index += 1

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    test = Renamer()

client.run(os.getenv('TOKEN'))
