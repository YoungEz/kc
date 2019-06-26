import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import nekos
import time
import colorsys
import sys
import subprocess
from pymongo import MongoClient
import os
import pymongo
import json
import traceback
import requests
import datetime
import random
from matematica import taxa

from random import choice

prefix = ["KN!" , "Kn!","kn!", "kN!","kc!", "kC!","KC!","Kc!"]

bot = commands.Bot(prefix, owner_id=497518244165320734)

bot.remove_command("help")
bot.launch_time = datetime.datetime.utcnow()
url = os.environ.get('URL')
mongo = MongoClient(url)
print('Carregando Extensões')
startup_extensions = ["cogs.music", "cogs.userinfo", "cogs.facebook", "cogs.load", "cogs.logs.canaldeletado", "cogs.logs.canalmsgfix", "cogs.logs.canalnovo", "cogs.reload", "cogs.hentai", "cogs.roleinfo", "cogs.newmember", "cogs.antidiv", "cogs.Modulos.admin", "cogs.Modulos.cassino", "cogs.rm", "cogs.desligar","cogs.reload","cogs.unload", "cogs.eval"]
n = "Motivo não definido"

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot



@bot.event
async def on_ready():
    print("=================================")
    print("Nome: %s" % bot.user.name)
    print("ID: %s" % bot.user.id)
    print("=================================")
    while True:
        delta_uptime = datetime.datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{str(len(set(bot.get_all_members())))} Seres Humanos No Servidor Last Hotel"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Estou online há: {days} dias {hours} Horas {minutes} Minutos {seconds} Segundos"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Sou Um Bot Especial Do Servidor Last Hotel"))
        await asyncio.sleep(10)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}.{}'.format(type(e).__name__, e)
            print('falha ao carregar extensoes {} . {}'.format(extension, e))
            print(repr(e))
            
@bot.command(pass_context=True, aliases=['latency', 'pong'])
async def ping(ctx):
    '''Find the response time in milliseconds.\n`latency` `pong`'''
    ptime = time.time()
    embed = discord.Embed(Title='Ping', color=0x00FF00)
    embed.add_field(name='Pong!', value='Calculando...')
    embed.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    ping3 = await ctx.send(embed=embed)
    ping2 = time.time() - ptime
    ping1 = discord.Embed(Title='Ping', color=0x00FF00)
    ping1.add_field(name='Pong!', value='{} ms.'.format(int((round(ping2 * 1000)))))
    ping1.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    await ping3.edit(embed=ping1)           
@bot.group(aliases=['shop'])
async def loja(ctx):
	if ctx.invoked_subcommand is None:
		member = ctx.message.author
		help_p = discord.Embed(title='Loja Last Hotel 🏨', description='**Caixas** - <:basica:581838984351580180> \n**Itens** - <:boitemystere:589076157107011605>\n**Badges** -  <:Icon_Monthly_VIP_Badge:581844119979032596>\n**Pets** -<:pet_hi:589416489959030785>', color = 0xff00ab)
		msg = await ctx.send(embed=help_p)
		await msg.add_reaction(':basica:581838984351580180')
		caixa = ":basica:581838984351580180"
		await msg.add_reaction('<:boitemystere:589076157107011605>')	
		await msg.add_reaction('<:Icon_Monthly_VIP_Badge:581844119979032596>')
		await msg.add_reaction(':pet_hi:589416489959030785')
	try:
		while True:
			reaction, user = await bot.wait_for("reaction_add", timeout=360, check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id)
			emoji = str(reaction.emoji)
			ra = str(reaction.message.author.id)
			if emoji == '<:basica:581838984351580180>':

				await msg.delete()
				embed_help = discord.Embed(description="<:basica:581838984351580180>┃**Loja** - `Caixas`", color=0xff00ab)
				embed_help.add_field(name = '<:basica:581838984351580180> ┃Básica',value ='**Valor:** `700`',inline = False)
				embed_help.add_field(name = '<:media:581838910754127894>┃Media',value ='**Valor:** `2000`',inline = False)
				embed_help.add_field(name = '<:epica:581839027687260164>┃Epica',value ='**Valor:** `4500`',inline = False)
				embed_help.add_field(name = '<:lendaria:581839194004127764>┃Lendária',value ='**Valor:** `7500`',inline = False)
				embed_help.add_field(name = 'Caixas Especiais',value ='Nenhum Evento Acontecendo',inline = False)
				msg = await ctx.send(embed=embed_help)
				await msg.add_reaction('⬅')
			if emoji == '<:Icon_Monthly_VIP_Badge:581844119979032596>':
				await msg.delete()
				embed_help = discord.Embed(title="<:Icon_Monthly_VIP_Badge:581844119979032596>┃Badges", description="s!comprar badge <item>", color = 0xff00AA)
				embed_help.add_field(name = '<:ZabuzaMomochi:589411111955202058>┃Demonio Oculto',value ='**Valor:** `5000`',inline = False)
				embed_help.add_field(name = '<a:loli:538707278724071435> Rei Do Porão',value ='**Valor:** `6500`',inline = False)
				embed_help.add_field(name = '<a:9197_HotelMarioMeme:589422561276854292> | Rei Do Cassino',value ='**Valor:**`7500`',inline = False)

			
				msg = await ctx.send(embed=embed_help)
				
				await msg.add_reaction('⬅')
			if emoji == '<:boitemystere:589076157107011605>':
					await msg.delete()
					embed_help = discord.Embed(description="<:boitemystere:589076157107011605>┃Itens", color=0xff00ab)
					embed_help.add_field(name = 'Em Breve',value ='Em Breve',inline = False)
					embed_help.add_field(name = 'Em Breve',value ='Em Breve',inline = False)
					msg = await ctx.send(embed=embed_help)
					await msg.add_reaction('⬅')

			if emoji == '<:pet_hi:589416489959030785>':
					await msg.delete()
					embed_help = discord.Embed(title="<:pet_hi:589416489959030785>┃**Pets**", description="para comprar algo digite `s!comprar pet <NomeDoPet>`", color=0xff00ab)
					embed_help.add_field(name = '<a:dog:589481224351776779> **Pituchinho**',value ='**Valor:**`13000`',inline = False)
					embed_help.add_field(name = '<a:ghostrobot:589492786584354816> **Pooky**',value ='**Valor:** `5000`',inline = False)

					msg = await ctx.send(embed=embed_help)
					await msg.add_reaction('⬅')							
			if emoji == '⬅':
				await msg.delete()
				msg = await ctx.send(embed=help_p)
				await msg.add_reaction(':boitemystere:589076157107011605')
				await msg.add_reaction(':boitemystere:589076157107011605')
				await msg.add_reaction(':basica:581838984351580180')
				await msg.add_reaction(':pet_hi:589416489959030785')
				await msg.add_reaction(':Icon_Monthly_VIP_Badge:581844119979032596')
	except asyncio.TimeoutError:
		await msg.delete() #deletar mensagem após um tempo sem resposta dos reactions
	except Exception as e:
		await ctx.send(repr(e))    
    
 
 
 
@bot.command(pass_context=True, aliases=['bi'])
async def botinfo(ctx):
	embed = discord.Embed(title="Minhas Informações", color=0x00ffba)
	delta_uptime = datetime.datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)	
	embed.add_field(name="**=====Principais Informações=====**", value=f"📆 **Criado Em:** `18:16 25/05/19`\n<:programador:582173369722601522> **Criador:** {ctx.guild.owner} \n<:programando:582173138448547843> **Linguagem Usada:** Python\n<a:discordlove:582176157609492490> **Versão Discord.py:** {discord.__version__}\n❓ **Prefixo:** `kn!`\n<:uptime:582708017049632768> **Estou Online Há: **`{days}` **Dias** `{hours}` **Horas** `{minutes}` **Minutos** `{seconds}` **Segundos**")

	await ctx.send(embed=embed) 
 
@bot.command(pass_context=True)
@commands.cooldown(1, 5.0, commands.BucketType.user)
async def setcargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    if not member:
    	return await ctx.send('{} Você não especificou o usuário.'.format(ctx.message.author.mention))

    	return await ctx.send(embed=rcat)
  
    if not role:
        await ctx.send('{} Você Precisa Mencionar Um Cargo Para Adicionar'.format(ctx.message.author.mention))
    else:
        await member.add_roles(role)
    embed = discord.Embed(title='Ação | Adicionar Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
    
    await ctx.send(embed=embed)

  	


@bot.command(pass_context=True)
@commands.cooldown(1, 5.0, commands.BucketType.user)
async def removercargo(ctx, role: discord.Role=None, member: discord.Member=None, *, motivo: str=None):
    if not member:
    	return await ctx.send('{} Você não especificou o usuário.'.format(ctx.message.author.mention))

    	return await ctx.send(embed=rcat)
    if not role:
        await ctx.send('{} Você Precisa Mencionar Um Cargo Para Remover'.format(ctx.message.author.mention))
    else:
        await member.remove_roles(role)
    embed = discord.Embed(title='Ação | Remover Cargo', color=0xff0000)
    embed.add_field(name='👮 Autor', value=ctx.message.author)
    embed.add_field(name='💻 Id', value=ctx.message.author.id)
    embed.add_field(name='👥 Usuário', value=member)
    embed.add_field(name='💻 Id', value=member.id)
      
    await ctx.send(embed=embed) 
@bot.command(pass_context = True)

@commands.cooldown(1, 5.0, commands.BucketType.user)
async def kick(ctx, user: discord.User=None, *, motivo: str = None):
    motivo = motivo or n
    if not user:
        return await ctx.send('{} Você não especificou o usuário. Exemplo: ``s!kick <@usuário> <motivo>``'.format(ctx.message.author.mention))
    if not ctx.author.guild_permissions.kick_members:
    	rcat = discord.Embed(title='Erro', description='Você Não Tem Permissão Para Executar Esse Comando.', color=0xFF0000)
    	rcat.set_author(name=f'{ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
    	return await ctx.send(embed=rcat)        
    else:
        await ctx.guild.kick(user)
        embed = discord.Embed(title='Ação | Kick!', description='{} usuário expulso com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
        embed.add_field(name='👮 Autor', value=ctx.message.author)
        embed.add_field(name='👥 usuário', value=user)
        embed.add_field(name='💻 Id', value=user.id)
        embed.add_field(name='📝 Motivo', value=motivo)
        embed.set_footer(text='Comando Realizado Por: {}| Shiryu Bot ★'.format(ctx.message.author.name))
        await ctx.send(embed=embed)
        embedpv = discord.Embed(title='Ação | Kick'.format(ctx.message.author.mention), color=0xff0Ab)
        embedpv.add_field(name='👮 Executor', value=ctx.message.author)
        embedpv.add_field(name='💻 Servidor', value=ctx.message.guild.name)
        embedpv.add_field(name='💻 id', value=ctx.message.author.id)
        embedpv.add_field(name='📝 Motivo', value=motivo)
        embedpv.set_thumbnail(url=ctx.message.guild.icon_url)
        await user.send(embed=embedpv)
        
@bot.group()
async def comprar(ctx):
	if ctx.invoked_subcommand is None:
		await ctx.send(f'{ctx.author.mention}, Você deve indicar uma categoria [item,badge,pet,caixa]')
	


@bot.listen("on_command_error")
async def error_handler(ctx, error):
    error = getattr(error, 'original', error)
    cmd_name = ctx.message.content.split()[0]  #pegar nome do cmd com prefixo

    if isinstance(error, commands.CommandOnCooldown):
        s = error.retry_after
        s = round(s, 2)
        h, r = divmod(int(s), 3600)
        m, s = divmod(r, 60)
        return await ctx.send(
            f'{ctx.author.mention} Você terá que aguardar **{str(h) + "h: " if h != 0 else ""}{str(m) + "m: " if m != 0 else ""}{str(s) + "s" if s != 0 else ""}** para usar este comando novamente.')

    if isinstance(error, commands.MissingPermissions):
        perms = "\n".join(error.missing_perms)
        return await ctx.send(f"{ctx.message.author.mention} Você precisa das permissões:\n{perms}\n para usar esse comando")

    if isinstance(error, commands.BotMissingPermissions):
        perms = "\n".join(error.missing_perms)
        return await ctx.send(f"Não tenho as seguintes permissões:\n{perms}")

    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(f"{ctx.message.author.mention} O comando `{cmd_name}` não foi encontrado em meu sistema. para ver meus comandos digite `kn!ajuda`.")



    # Demais erros vão aparecer apenas no console
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    
@bot.event
async def on_raw_reaction_add(payload):

    if payload.message_id != 592825496950013952:
        return

    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)

    #ignorar reactions de bots
    if user.bot:
        return

    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    #adicionar emojis na msg (caso não tenha)
    emoji_list = ["👩", "👨", "❓", "🔞", "🌠", "💍", "😍", "🚶", "👉", "🌈", "✅"]
    for emoji in emoji_list:
        if not emoji in [str(reaction.emoji) for reaction in message.reactions]:
            await message.add_reaction(emoji)

    #o payload.emoji deve estar como str para evitar problemas com custom emoji
    if str(payload.emoji) == "👩":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009312975192085)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)

    #para add mais reaction por cargo abaixo, deixe como "elif" ao invés de "if".
    elif str(payload.emoji) == "👨":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009331086327848)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)

    #evitar adição de novos emojis na mensagem (opcional)
    else:
        await message.remove_reaction(payload.emoji, member=user)
    if str(payload.emoji) == "❓":
        await message.remove_reaction(payload.emoji, member=user)
        
        role = guild.get_role(588009222155927582)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)  
    if str(payload.emoji) == "✅":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588315269269684255)
        role2 = guild.get_role(588314393046155264)
        await user.add_roles(role)
        await user.remove_roles(role2)
        await user.send(f"Parabens! Você concluiu seu registro")
    if str(payload.emoji) == "🔞":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009350635978753)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)                  
    if str(payload.emoji) == "🌠":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009366066692106)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)                                    
    if str(payload.emoji) == "💍":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009241340542987)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)                                                      
    if str(payload.emoji) == "😍":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009296826990613)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)                                                                        
    if str(payload.emoji) == "🚶":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588009262882488358)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)
            
    if str(payload.emoji) == "🌈":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588706925039058964)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)
    if str(payload.emoji) == "👉":
        await message.remove_reaction(payload.emoji, member=user)
        role = guild.get_role(588706876535996446)
        if role in user.roles:
            await user.remove_roles(role)
            await user.send(f"Cargo [{role.name}] removido!", delete_after=20)
        else:
            await user.add_roles(role)
            await user.send(f"Cargo [{role.name}] adicionado!", delete_after=20)                 
                       
@bot.command(pass_context=True)
async def i(ctx, cargo: discord.Role):
	await ctx.send(f'{cargo.id}')	
	
@bot.command(pass_context=True, aliases=['tm', 'tempm', 'tmute'])
async def tempmute(ctx, user: discord.Member, temp: int=None):
	role = discord.utils.find(lambda r: r.name == "👮 | Moderador",ctx.author.guild.roles)
		
	if role in ctx.author.roles:
		mt = ctx.guild.get_role(589047230606999553)
		await user.add_roles(mt)		
		s = temp
		s = round(s, 2)
		h, r = divmod(int(s), 3600)
		m, s = divmod(r, 60)
		return await ctx.send(f'{ctx.author.mention} Você silenciou {user.mention} por **{str(h) + "h: " if h != 0 else ""}{str(m) + "m: " if m != 0 else ""}{str(s) + "s" if s != 0 else ""}** com sucesso!')
		await asyncio.sleep(temp)
		await user.remove_roles(mt)
		await user.send('Você aprendeu a falar novamente!')
		
	else:
		await ctx.send(f'{ctx.author.mention} Você precisa do cargo {role.name} para poder usar esse comando')
           
			
                            

bot.run(str(os.environ.get('BOT_TOKEN')))
