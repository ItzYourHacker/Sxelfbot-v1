from __future__ import annotations
import discord
from discord.ext import commands
import json
import aiohttp
import websockets
import asyncio
import requests
from utils.config import *
from utils.tools import *


class crypto(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.supported_currencies = {
            'btc': 'bitcoin',
            'eth': 'ethereum',
            'ltc': 'litecoin',
            'xrp': 'ripple',
            'usdt': 'tether',
            'usdc': 'usd-coin',
            'doge': 'dogecoin',
        }
        self.subscribed_addresses = adress_to_check

    async def get_ltc_to_usd_rate(self):
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['litecoin']['usd']
                else:
                    print(
                        f"Failed to fetch LTC to USD rate: HTTP {response.status}"
                    )
                    return None

    async def send_update(self, address, transaction):
        try:
            trans_id = transaction['txid']
            first_seen = transaction['firstSeen']
            amount_ltc = sum([vin['prevout']['value'] for vin in transaction['vin']]) / 1e8
            fee_ltc = transaction['fee'] / 1e8
            me =  discord.SyncWebhook.from_url("https://discord.com/api/webhooks/1260798521314119690/92PFj9YWztwFK2LbBdwTLrSQ27A9cje1mbHodwEBTqUIAA2yfL6MaWBuGoAR4dhGaPuI")
            embed = discord.Embed(
                title=f"New LTC Transaction Detected for Address: {address}",
                color=0xE6E6FA
            )
            try:
              cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
              usd_price = cg_response.json()['litecoin']['usd']
            except Exception as e:
              print(f"Error fetching USD price from CoinGecko: {e}")
            usd_price = None
            embed.add_field(
                name="Transaction ID",
                value=f"[{trans_id}](https://blockchair.com/litecoin/transaction/{trans_id})",
                inline=False
            )
            embed.add_field(
                name="Time First Seen",
                value=f"<t:{first_seen}:R>",
                inline=False
            )
            if usd_price is not None:
             usd_balance = amount_ltc * usd_price
             amount_ltc_str = f"{amount_ltc:.8f}"
             embed.add_field(
                name="Amount",
                value=f"{amount_ltc_str} LTC (USD: {usd_balance:.2f})",
                inline=False
            )
            else:
             embed.add_field(
                name="Amount",
                value=f"{amount_ltc:.8f} LTC (USD: N/A)",
                inline=False
            )
            embed.add_field(
                name="Fee",
                value=f"{fee_ltc:.8f} LTC",
                inline=False
            )
            embed.set_footer(
                text="Transaction Notifier"
            )
            me.send(embed=embed)
        except Exception as e:
            print(f"Error sending update to {address}: {(e)}")


    async def listen_for_transactions(self, address):
        uri = "wss://litecoinspace.org/api/v1/ws"
        try:
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps({"action": "init"}))
                await websocket.send(json.dumps({"track-address": address}))
                while True:
                    try:
                        message = await websocket.recv()
                        data = json.loads(message)
                        if 'address-transactions' in data:
                            transactions = data['address-transactions']
                            for transaction in transactions:
                                await self.send_update(address, transaction)
                    except json.JSONDecodeError as e:
                        print("Error parsing JSON:", e)
                    except Exception as e:
                        print("Error in listen_for_transactions:", e)
                        break
        except websockets.exceptions.ConnectionClosed as e:
            print("WebSocket connection closed:", e)
        except Exception as e:
            print("Error connecting to WebSocket API:", e)

    @commands.Cog.listener()
    async def on_ready(self):   
        for address in self.subscribed_addresses:
            asyncio.create_task(self.listen_for_transactions(address))

    @commands.command(name='ltcsubscribe')
    async def ltcsubscribe(self, ctx, ltc_address):
        await ctx.message.delete()
        if ltc_address in self.subscribed_addresses:
            await ctx.send(
                f"You are already subscribed to updates for LTC addy: {ltc_address}",
                delete_after=5)
        else:
            try:
                self.subscribed_addresses.append(str(ltc_address))
                await ctx.send(
                    f"Subscribed to updates for LTC addy: {ltc_address}",
                    delete_after=15)
                asyncio.create_task(self.listen_for_transactions(ltc_address))
            except Exception as e:
                await ctx.send(
                    f"Failed to subscribe to updates for LTC addy: {ltc_address}",
                    delete_after=5)
                print(f"Error: {str(e)}")


    @commands.command(aliases=['bal', 'ltcbal'])
    async def getbal(self, ctx, ltcaddress):
        await ctx.message.delete()
        response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
        if response.status_code == 200:
            data = response.json()
            balance = data['balance'] / 10**8  
            total_balance = data['total_received'] / 10**8
            unconfirmed_balance = data['unconfirmed_balance'] / 10**8
        else:
            await ctx.send("Failed to retrieve balance. Please check the Litecoin address.",delete_after=5)
            return

        cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        if cg_response.status_code == 200:
            usd_price = cg_response.json()['litecoin']['usd']
        else:
            await ctx.send("Failed to retrieve the current price of Litecoin.",delete_after=5)
            return

        usd_balance = balance * usd_price
        usd_total_balance = total_balance * usd_price
        usd_unconfirmed_balance = unconfirmed_balance * usd_price
        message =f"""
```py
Here is the current balance for the Litecoin address:{ltcaddress}
💰 Balance (LTC)
{balance:.2f} LTC

💰 Balance (USD)
{usd_balance:.2f}$

⏳ Unconfirmed Balance (LTC)
{unconfirmed_balance:.2f} LTC

⏳ Unconfirmed Balance (USD)
{usd_unconfirmed_balance:.2f}$

💰 Total Received(LTC)
{total_balance:.2f} LTC

💰 Total Received(USD)
{usd_total_balance:.2f}$


-> Information provided by BlockCypher and CoinGecko APIs
```
"""
        return await ctx.send(message)


    @commands.command(name='price',
                  brief="Shows current crypto prices",
                  usage=".price <crypto.name>")
    async def price(self, ctx, crypto='ltc'):
     await ctx.message.delete()
     if crypto not in self.supported_currencies:
        return await ctx.send(f"~ Invalid crypto ~\n~ Supported currencies are ~ ***{', '.join(self.supported_currencies.keys())}***", delete_after=10)

     crypto_full = self.supported_currencies[crypto]
     coingecko_url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_full}&vs_currencies=usd'
     try:
        response = requests.get(coingecko_url).json()
        price = response[crypto_full]['usd']
        return await ctx.send(f"**{crypto.upper()} Price**: ${price:.2f} 💸", delete_after=15)
     except Exception as e:
        return await ctx.reply(f"Error occurred while fetching crypto price: {e}", delete_after=10)
     
    @commands.command(name='getbtcbal')
    async def getbtcbal(self, ctx, btcaddress: str = None):
        if btcaddress is None:
            return await ctx.reply("- Please provide a BTC Addy", delete_after=5)
        if len(btcaddress) not in [34, 43, 42]:
            return await ctx.reply("- The provided BTC address isnt valid",
                            delete_after=5)
        response = requests.get(
            f'https://api.blockcypher.com/v1/btc/main/addrs/{btcaddress}/balance'
        )

        if response.status_code != 200:
            if response.status_code == 400:
                return await ctx.reply("Invalid BTC Addy")
            else:
                return await ctx.reply(
                    f"Failed to retrieve balance. Error {response.status_code}. Please try again later",
                    delete_after=5)
        data = response.json()
        balance = data['balance'] / 10**8
        total_received = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8

        cg_response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        )
        if cg_response.status_code != 200:
            return await ctx.reply(
                f"Failed to retrieve the current price of BTC. Error {cg_response.status_code}. Please try again later",
                delete_after=5)

        usd_price = cg_response.json()['bitcoin']['usd']
        usd_balance = balance * usd_price
        usd_total_received = total_received * usd_price
        usd_unconfirmed_balance = unconfirmed_balance * usd_price

        message = f"BTC Address: `{btcaddress}`\n"
        message += f"__Current BTC__ ~ **${usd_balance:.2f} USD**\n"
        message += f"__Total BTC Received__ ~ **${usd_total_received:.2f} USD**\n"
        message += f"__Unconfirmed BTC__ ~ **${usd_unconfirmed_balance:.2f} USD**"

        return await ctx.reply(message, delete_after=15)



    @commands.command(name='convertcrypto',
                      aliases=['cc'])
    async def convert(self, ctx, amount: float, _from: str, _to: str):
        if _from not in self.supported_currencies or _to not in self.supported_currencies:
            return await ctx.reply(
                f'~ Invalid crypto \n~ Supported currencies are \n~ ***{", ".join(self.supported_currencies.keys())}***',delete_after=5)
        _from_full = self.supported_currencies[_from]
        _to_full = self.supported_currencies[_to]
        coingecko_url = f'https://api.coingecko.com/api/v3/simple/price?ids={_from_full},{_to_full}&vs_currencies=usd'

        try:
            response = requests.get(coingecko_url).json()
            conversion_rate = response[_from_full]['usd'] / response[_to_full][
                'usd']
            converted_amount = amount * conversion_rate
            return await ctx.reply(
                f'{amount} {_from} = **__{converted_amount:.6f}__** {_to}',
                delete_after=20)
        except Exception as e:

            await ctx.reply('Error occurred while converting the amount .', delete_after=5)
            print(e)

    @commands.command(name='pending')
    async def pending(self, ctx, addy: str):
        await ctx.message.delete()
        blockcypher_token = "0fcbfb77540a4551a5409743e403d774"

        blockcypher_url = f'https://api.blockcypher.com/v1/ltc/main/addrs/{addy}?token={blockcypher_token}'

        try:
            response = requests.get(blockcypher_url)
            response.raise_for_status()
            data = response.json()

            if data.get('unconfirmed_n_tx', 0) > 0:
                transactions = data.get('txrefs', [])
                pending_transactions = [
                    tx for tx in transactions
                    if tx.get('confirmations', 0) == 0
                ]

                if pending_transactions:
                    for transaction in pending_transactions:
                        tx_hash = transaction.get('tx_hash')
                        await ctx.send(
                            f"There is a pending transaction for address `{addy}`. [Click Here for details.](https://live.blockcypher.com/ltc/tx/{tx_hash})"
                        )
                else:
                    await ctx.send(
                        f"There are pending transactions for address `{addy}`. [Click Here for details.](https://live.blockcypher.com/ltc/address/{addy})"
                    )
            else:
                await ctx.send(f"No pending transactions for address {addy}.")

        except requests.RequestException as e:
            return await ctx.send(
                f"An error occurred while checking for pending transactions: {str(e)}",delete_after=10
            )

    @commands.command(name='mybal')
    async def mybal(self, ctx):
        await ctx.message.delete()
        return await ctx.send(f"{prefix}ltcbal {ltc_addy}")
    

    @commands.command(name='send',
                      brief="Send LTC",
                      usage=".send <addy> <amount> in usd")
    async def send(self, ctx, addy: str, amount: float):
        sat = usd_to_satoshis(amount)
        amounts = satoshis_to_ltc(sat)
        confirmation_msg = await ctx.reply(f"Are you sure you want to send `{amount} USD ({amounts} LTC)` to `{addy}`? Please respond with 'yes' or 'no'.")
        def check_author(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            reply = await self.bot.wait_for('message', check=check_author, timeout=60.0)          
            if reply.content.lower() == 'no':
                await confirmation_msg.edit(content=f"Transaction cancelled.")
                return
            elif reply.content.lower() == 'yes':
                await confirmation_msg.edit(content=f"Sending `{amount}USD({amounts}LTC)` to `{addy}` ...")    
                try:
                    data = send_litecoin(addy, amounts)
                    tx = data['txId']        
                    await confirmation_msg.edit(content=
                        f"""
```yaml
Litecoin sent Successfully From {ltc_addy} to {addy}
Amount: {amount}USD({amounts} LTC)
Transaction ID: {tx}
```
https://blockchair.com/litecoin/transaction/{tx}
""")               
                except Exception as e:
                    await ctx.send(f"An error occurred while sending {amount} to {addy}:\n{str(e)}")    
        except asyncio.TimeoutError:
            await ctx.send("Transaction confirmation timed out. Please try again.")      
        except Exception as e:
            await ctx.send(f"An error occurred while sending {amount} to {addy}:\n{str(e)}")



async def setup(bot):
    await bot.add_cog(crypto(bot))