from __future__ import annotations
import discord
import requests
import datetime
from discord.ext import commands
import aiohttp
import datetime


class nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(name="4k")
    async def _4k(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/4k")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)


    @commands.command(name="pussy")
    async def _pussy(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/pussy")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)


    @commands.command(name="boobs")
    async def _boobs(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/boobs")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)
    
    
    @commands.command(name="lewd")
    async def _lewd(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/lewd")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)

    
    
    @commands.command(name="lesbian")
    async def _lesbian(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/lesbian")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)

    
    
    @commands.command(name="blowjob")
    async def _blowjob(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/blowjob")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)

    
    
    @commands.command(name="cum")
    async def _cum(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/cum")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)
    
    @commands.command(name="gasm")
    async def _gasm(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/gasm")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)
    
    
    @commands.command(name="hentai")
    async def _hentai(self, ctx):
        ok = requests.get("http://api.nekos.fun:8080/api/hentai")
        data = ok.json()
        image = data["image"]
        await ctx.reply(image)

    @commands.command(name="anal")
    async def anal(self, ctx):
        """To get Random Anal"""
        url = "https://nekobot.xyz/api/image"
        params = {"type": "anal"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return
        img = res["message"]
        await ctx.reply(img)

    @commands.command(name="gonewild")
    async def gonewild(self, ctx):
        """
        To get Random GoneWild
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "gonewild"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]
        await ctx.reply(img)

    @commands.command(name="hanal")
    async def hanal(self, ctx):
        """To get Random Hentai Anal"""
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hanal"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="holo")
    async def holo(self, ctx):
        """
        To get Random Holo
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "holo"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="neko")
    async def neko(self, ctx):
        """
        To get Random Neko
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "neko"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="hneko")
    async def hneko(self, ctx):
        """
        To get Random Hneko
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hneko"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="hkitsune")
    async def hkitsune(self, ctx):
        """
        To get Random Hkitsune
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hkitsune"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="kemonomimi")
    async def kemonomimi(self, ctx):
        """
        To get Random Kemonomimi
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "kemonomimi"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="pgif")
    async def pgif(self, ctx):
        """
        To get Random PornGif
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "pgif"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="kanna")
    @commands.is_nsfw()
    @commands.bot_has_permissions(embed_links=True)
    async def kanna(self, ctx):
        """
        To get Random Kanna
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "kanna"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="thigh")
    @commands.is_nsfw()
    @commands.bot_has_permissions(embed_links=True)
    async def thigh(self, ctx):
        """
        To get Random Thigh
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "thigh"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="hthigh")
    async def hthigh(self, ctx):
        """
        To get Random Hentai Thigh
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hthigh"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="paizuri")
    async def paizuri(self, ctx):
        """
        To get Random Paizuri
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "paizuri"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="tentacle")
    async def tentacle(self, ctx):
        """
        To get Random Tentacle Porn
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "tentacle"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="hboobs")
    async def hboobs(self, ctx):
        """
        To get Random Hentai Boobs
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hboobs"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="yaoi")
    async def yaoi(self, ctx):
        """
        To get Random Yaoi
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "yaoi"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)

    @commands.command(name="hmidriff")
    async def hmidriff(self, ctx):
        """
        To get Random Hmidriff
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hmidriff"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]
        await ctx.reply(img)

    @commands.command(name="hass")
    async def hass(self, ctx):
        """
        To get Random Hentai Ass
        """
        url = "https://nekobot.xyz/api/image"
        params = {"type": "hass"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["message"]

        await ctx.reply(img)


    @commands.command()
    async def n(self, ctx):
        """
        Best command I guess. It return random ^^
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    "https://scathach.redsplit.org/v3/nsfw/gif/") as r:
                if r.status == 200:
                    res = await r.json()
                else:
                    return

        img = res["url"]

        await ctx.reply(img)

async def setup(bot):
    await bot.add_cog(nsfw(bot))
