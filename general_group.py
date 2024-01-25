import discord

from discord import app_commands as apc

class GeneralGroup(apc.Group):

    def __init__(self, bot:discord.ext.commands.Bot):
        super().__init__()
        self.bot = bot