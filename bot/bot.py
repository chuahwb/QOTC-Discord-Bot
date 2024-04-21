import discord
from discord.ext import commands
from .commands import setup_commands


def setup_bot():

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix="/", intents=intents)

    setup_commands(bot)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        from .utils import process_message
        from .state_manager import bot_state

        # Custom processing logic
        guild_id = str(message.guild.id)
        if bot_state.first_scan.get(guild_id) == None:
            bot_state.failed_scanning(guild_id=guild_id)
        if bot_state.first_scan[guild_id] and not message.content.startswith('/'):
            process_message(message)

        # Process commands regardless of the scanned status
        if not bot_state.active_scanning:
            await bot.process_commands(message)

    return bot
