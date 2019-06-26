import discord
from discord.ext import commands

	   

class antidiv(commands.Cog):
   def __init__(self, bot):
       self.bot = bot




   @commands.Cog.listener()
   async def on_message(self, message):  	
	   if "discord.gg" in message.content.lower():

	   		await message.delete()
	   		await message.channel.send(f'**{message.author.mention} Você não pode divulgar servidores aqui!**')
	   if "porra" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')
	   if "fdp" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "filha da puta" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "puta" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "se foder" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "piranha" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "fds" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "foda se" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "vai tomar no cu" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "vtnc" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')
	   if "vtmnc" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   if "buceta" in message.content.lower():
	   	await message.delete()
	   	await message.channel.send(f'**{message.author.mention} Você não pode falar palavras de baixo calão neste servidor.**')	   	
	   	
	   	
                    

def setup(bot):
    print("[Andtidiv] Carregado")
    bot.add_cog(antidiv(bot))
