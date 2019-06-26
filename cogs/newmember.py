import json
import discord
import asyncio
from random import choice
from discord.ext import commands
from discord.utils import get

color = 0xff00ab

semdesc= "Este usuário não possui descrição. para adicionar uma descrição digite `s!sobre <descrição>`"
nobadg = "Este usuário não possui badges"
novp = "Este usuário não é vip"
nott = "Nenhuma frase adicionada. Use `s!frase <frase>` para adicionar"
nosp = "Solteiro(a)"


class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
    	try:
    		to_send = discord.Embed(
    		
    		color=color,
    		description="<a:feelsrainbow:588690500505042944> {}, Eu sou o BOT oficial do(a) {}, qualquer coisa digite ``kn!ajuda`` que eu irei ajudar você!".format(member.name, member.guild))
    		to_send.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
    		to_send.set_thumbnail(url="{}".format(member.avatar_url))
    		to_send.set_footer(text="Kanna-Chan ® Todos os direitos reservados.")
    		channel = self.bot.get_channel(587755161938558988)
    		await member.send(embed=to_send)
    		await channel.send(f'<a:aRainbowCatGlitch:588690400420691979> {member.mention} Seja bem vindo ao servidor,respeite as regras para não ser punido! <a:catrainbow:588690947609591810>')
    		channel_ = self.bot.get_channel(587755161938558988)
    		role = discord.utils.find(lambda r: r.name == "❌ | Não registrado",member.guild.roles)
    		await member.add_roles(role)
    		numbers = ['<:0_:578615675182907402>','<:1_:578615669487304704>', '<:2_:578615674109165568>','<:3_:578615683424976916>', '<:4_:578615679406833685>', '<:5_:578615684708171787>','<:6_:578617070309343281>', '<:7_:578615679041798144>', '<:8_:578617071521497088>','<:9_:578617070317469708>']
    		text = str(member.guild.member_count)
    		list_ = list()
    		for l in text:
    			list_.append(numbers[int(l)])
    			await asyncio.sleep(50)
    			await channel_.edit(topic="<a:caralho:525105064873033764> **Membros No Servidor:** " + str(list_))
    	except Exception as e:
    			print(f"[Erro] {e}")
           

def setup(bot):
    bot.add_cog(OnMemberJoin(bot))
    print('\033[1;32mO evento \033[1;34mMEMBER_JOIN\033[1;32m foi carregado com sucesso!\33[m')
