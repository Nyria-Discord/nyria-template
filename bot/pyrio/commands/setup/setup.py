from nextcord.ext import commands


class NyriaSetup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(NyriaSetup(bot))
