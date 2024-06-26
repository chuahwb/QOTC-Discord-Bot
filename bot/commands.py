import discord
from discord.ext import commands
import datetime
from data.storage import trade_data
from plotting.plotting import plot_data
from .state_manager import bot_state
from discord.commands import Option


def setup_commands(bot: commands.Bot):
    @bot.slash_command(description="Scan channel messages to capture trade data.")
    async def qotc_scan(ctx,
                        period: Option(str, "Choose period type", choices=["count", "days", "months"]),
                        number: Option(int, "Enter number of messages or time units")):
        """
        Scans the channel's message history based on the specified period or count to capture trade data.
        """
        await ctx.respond("Trade data has been reset. Starting new scan.")
        trade_data['buy'].clear()
        trade_data['sell'].clear()

        # Save original permissions
        everyone_role = ctx.guild.default_role
        original_overwrites = ctx.channel.overwrites.get(
            everyone_role, discord.PermissionOverwrite())

        # Set channel to read-only for @everyone
        overwrite = discord.PermissionOverwrite(send_messages=False)
        await ctx.channel.set_permissions(everyone_role, overwrite=overwrite)

        # Enable message processing
        bot_state.start_scanning()
        messages_scanned = 0

        try:
            if period == 'count':
                async for message in ctx.channel.history(limit=number):
                    await ctx.bot.on_message(message)
                    messages_scanned += 1
            elif period in ['days', 'months']:
                days = number * 30 if period == 'months' else number
                limit_date = datetime.datetime.utcnow() - datetime.timedelta(days=days)
                async for message in ctx.channel.history(limit=None, after=limit_date):
                    await ctx.bot.on_message(message)
                    messages_scanned += 1
            else:
                await ctx.send("Invalid command usage. Use '/scan count <number>' or '/scan [days|months] <number>'.")
                bot_state.failed_scanning()
                return
        finally:
            bot_state.scanned()
            bot_state.stop_scanning()

            # Restore original permissions after scanning
            await ctx.channel.set_permissions(everyone_role, overwrite=original_overwrites)
            await ctx.send(f"Scanning completed. {messages_scanned} messages scanned.")

    @bot.slash_command(description="Resets the stored trade data.")
    async def qotc_reset(ctx):
        """
        Resets the internal storage of trade data.
        """
        trade_data['buy'].clear()
        trade_data['sell'].clear()
        bot_state.not_scanned()
        await ctx.respond("Trade data has been reset.")

    @bot.slash_command(description="Generates and sends distribution histograms for buy and sell orders.")
    async def qotc_dist(ctx):
        """
        Sends the distribution charts for buy and sell orders.
        """
        buy_plot = plot_data(
            trade_data['buy'], 'Distribution of Buy Orders', 'green')
        sell_plot = plot_data(
            trade_data['sell'], 'Distribution of Sell Orders', 'red')
        if buy_plot and sell_plot:
            await ctx.respond("Generating Buy & Sell Orders Histogram")
            await ctx.send("Buy Order Distribution:", file=discord.File(buy_plot, 'buy_histogram.png'))
            await ctx.send("Sell Order Distribution:", file=discord.File(sell_plot, 'sell_histogram.png'))
        else:
            await ctx.respond("No sufficient data to generate histograms.")
