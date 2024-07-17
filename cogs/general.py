from __future__ import annotations
import discord
from discord.ext import commands
import google.generativeai as generateai
import psutil
import sys
from typing import Union 
from utils.config import *

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="botinfo",
                           aliases=['bi'],
                           help="Get info about selfbot .")
    async def botinfo(self, ctx: commands.Context):
        ping = int(self.bot.latency * 1000)
        await ctx.reply(f"""
```yaml
Commands: {len(set(self.bot.walk_commands()))}
CPU Usage: {psutil.cpu_percent()}%
Memory Usage: {psutil.virtual_memory().percent}%
Websocket Latency: {ping} ms
Python Version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}
Discord.py Version: {discord.__version__}
```
""")
    @commands.command(aliases=["ms"], description="Show's the bot latency")
    async def ping(self, ctx: commands.Context):
      okk = await ctx.reply("Pinging ...") 
      ping = int(self.bot.latency * 1000)
      return await okk.edit(content=f"🏓 Pong: **{ping}ms**")

    @commands.command(aliases=["ri"], description="Shows information about the Role")
    async def roleinfo(self, ctx, role: discord.Role):
         msg = f"""
**Role Name:** {role.name}
**Role ID:** {role.id}
**Role Position:** {role.position}\n
**Hex code:** {str(role.color)}
**Created At:** <t:{round(role.created_at.timestamp())}:R>
**Mentionability:** {role.mentionable}
**Separated:** {role.hoist}
**Integration:** {role.is_bot_managed()}

"""
         return await ctx.reply(msg,delete_after=20)

    @commands.command(description="Shows the server icon")
    async def servericon(self, ctx):
         if ctx.guild.icon:
             return await ctx.reply(ctx.guild.icon.url)
         else:
             return await ctx.reply(f"{ctx.guild.name} does not have any icon .")
         
    @commands.command(aliases=["av"], brief="Avatar", description="Shows the avatar of user")
    async def avatar(self, ctx, member: Union[discord.Member, discord.User] = None):
        member = (
            member or ctx.author
        )
        if isinstance(member, discord.User):
            if member in ctx.guild.members:
                member = discord.utils.get(ctx.guild.members, id=member.id)
            else:
                member = member
        if not member.avatar:
            await ctx.reply(f"There is no avatar for {(member.name)}")
        return await ctx.reply(member.avatar.url)

    @commands.command(name='first-message', aliases=['firstmsg', ], description="Shows the first message of the channel .")
    async def _first_message(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel       
        msg = [match async for match in channel.history(oldest_first=True, limit=1)][0] 
        await ctx.reply(f"[{msg.content}]({msg.jump_url})")
        
    @commands.command(aliases=["mc"], description="Returns the members count for the server")
    async def membercount(self, ctx):
      await ctx.reply(f"{ctx.guild.member_count}")

    @commands.command(name="chatgpt", aliases=['cgpt', 'gpt'], description="Give you results for your query from gemini")
    async def gpt(self,ctx: commands.Context, *, prompt):
       ok = await ctx.send("Please wait while I process your request .")
       generateai.configure(api_key=gemini_key)
       model = generateai.GenerativeModel('gemini-pro',
    safety_settings=[
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]
)
       try:
         r = model.generate_content(prompt)
         return await ok.edit(content=f"```py\n{r.text}\n```")
       except:
          return await ok.edit(content="Failed to generate response. Please try again.")

async def setup(bot):
    await bot.add_cog(general(bot))
