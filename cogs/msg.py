from __future__ import annotations
import discord
from discord.ext import commands 
from utils.config import *

class dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
                       
    @commands.Cog.listener('on_message')
    async def on_hacker(self,message:discord.Message):
      await self.bot.wait_until_ready()
      if isinstance(message.channel, discord.DMChannel):
        content = message.content.lower()
        for msg, reply in dm_msg.items():
          if content.startswith(msg): 
             return await message.reply(reply)
      else:
          return 
                    
async def setup(bot):
	await bot.add_cog(dm(bot))
 