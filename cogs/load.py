import discord
import asyncio
from discord.ext import commands

class LoadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden=True)
    async def load(self, ctx, cog):
    	if ctx.author.id == 497518244165320734:
    		try:
    			self.bot.load_extension('cogs.{}'.format(cog))
    			embed = discord.Embed(
    			color=0xffff00,
    			description=f'<:confirmado:519896822072999937>│Extenção **{cog}**, carregada com sucesso!')
    			await ctx.send(embed=embed)
    		except ModuleNotFoundError as e:
    			embed = discord.Embed(color=0xffff00,description=f'<:oc_status:519896814225457152>│Falha ao carregar a extenção **{cog}**. \n```{e}```')
    			await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(LoadCog(bot))
    print('\033[1;32mO comando \033[1;34mLOAD\033[1;32m foi carregado com sucesso!\33[m')
