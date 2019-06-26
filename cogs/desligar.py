import json
import discord

from discord.ext import commands

color=0xff00ab

class LogoutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()     
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.command(hidden=True)
    async def logout(self, ctx, *, reason: str = None):
        if reason is None:
            return await ctx.send(':erro:581791491467378699│**DIGA UM MOTIVO PARA ME DESLIGAR!**')

        embed = discord.Embed(
            color=color,
            description=f'<a:correct:588329506763440138>│**Logging out...**')
        await ctx.send(embed=embed)
        await self.bot.logout()


def setup(bot):
    bot.add_cog(LogoutCog(bot))
    print('\033[1;32mO comando \033[1;34mLOGOUT\033[1;32m foi carregado com sucesso!\33[m')
