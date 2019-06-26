import json
import discord, datetime
import nekos
from discord.utils import get
from discord.ext import commands
from asyncio import sleep


color = 0xff00ff


class hentai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def hentai(self, ctx):
    	if ctx.channel.is_nsfw():
    		pic = nekos.img('hentai')
    		embed = discord.Embed(color=0xFFFF00, title=f'<a:hentai05:582713620425605142> NSFW!', timestamp=datetime.datetime.utcnow())
    		embed.set_image(url=pic)
    		embed.set_footer(text=f'Comando Realizado Por {ctx.author}')
    		await ctx.send(embed=embed)
    	else:
    		await ctx.send(f'{ctx.author.mention} Para Usar Esse Comando Você Precisar Estar Em Um Canal Com A Opção NSFW Ativa!') 
    	
    @commands.command()
    async def nekogif(self, ctx):
    	if ctx.channel.is_nsfw():
    		pic = nekos.img('nsfw_neko_gif')
    		embed = discord.Embed(color=0xFFFF00, title=f'<a:hentai05:582713620425605142> NSFW!', timestamp=datetime.datetime.utcnow())
    		embed.set_image(url=pic)
    		embed.set_footer(text=f'Comando Realizado Por {ctx.author}')
    		await ctx.send(embed=embed)
    	else:
    		await ctx.send(f'{ctx.author.mention} Para Usar Esse Comando Você Precisar Estar Em Um Canal Com A Opção NSFW Ativa!')
    @commands.command()
    async def hentaigif(self, ctx):
    	if ctx.channel.is_nsfw():
    		pic = nekos.img('random_hentai_gif')
    		embed = discord.Embed(color=0xFFFF00, title=f'<a:hentai05:582713620425605142> NSFW!', timestamp=datetime.datetime.utcnow())
    		embed.set_image(url=pic)
    		embed.set_footer(text=f'Comando Realizado Por {ctx.author}')
    		await ctx.send(embed=embed)
    	else:
    		await ctx.send(f'{ctx.author.mention} Para Usar Esse Comando Você Precisar Estar Em Um Canal Com A Opção NSFW Ativa!')
		
def setup(bot):
    bot.add_cog(hentai(bot))
    print('\033[1;32mO comando \033[1;34mHENTAI\033[1;32m foi carregado com sucesso!\33[m')		
