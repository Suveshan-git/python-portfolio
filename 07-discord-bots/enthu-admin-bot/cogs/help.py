from discord.ext import commands
import discord

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # Store bot instance for later use

    @commands.command(name="help", help="Displays bot features and what's coming soon.")
    async def help_command(self, ctx):
        embed = discord.Embed(
            title="📖 Admin Bot Help",
            description="Here's what I can do now and in the future!",
            color=discord.Color.blurple()
        )
        embed.add_field(
            name="✅ Current Features",
            value="`!help` - Show this help message",
            inline=False
        )
        embed.add_field(
            name="🛠️ Coming Soon",
            value="""
            `!play tictactoe` - Play Tic-Tac-Toe against the Bot
            `!play tictactoe @user` - Play Tic-Tac-Toe against another user
            """,
            inline=False
        )
        await ctx.send(embed=embed)

# Required setup function for loading the cog
async def setup(bot):
    await bot.add_cog(HelpCog(bot))
