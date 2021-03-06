import discord
from discord.ext import commands
from .utils.dataIO import fileIO
import random

class Zalgo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def zalgo(self, ctx):
        """Zalgo the text"""
        # first pull out the .zalgo part of the message
        raw_msg = ' '.join(ctx.message.clean_content.split(' ')[1:])
        if raw_msg == '':
            raw_msg = 'HE COMES'

        # random intensity
        intensity = random.randint(50, 150)

        # zalgo characters to fuck with
        zalgo_chrs = [chr(x) for x in range(0x0300, 0x036F + 1)]
        zalgo_chrs += [u'\u0488', u'\u0489']

        msg_array = list(raw_msg)
        for i in range(intensity):
            index = random.randint(0, len(msg_array) - 1)
            msg_array.insert(index, random.choice(zalgo_chrs))

        zalgo_msg = ''.join(msg_array)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(zalgo_msg)


def setup(bot):
    n = Zalgo(bot)
    bot.add_cog(n)

