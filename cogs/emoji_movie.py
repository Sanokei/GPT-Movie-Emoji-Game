import os
import openai
import json

# Import the required dependencies
from discord.ext import commands
from discord.ext.commands import Context

# Import the checks helper
from helpers import checks

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

# Here we name the cog and create a new class for the cog.
class Emoji_Movie(commands.Cog, name="emoji_movie"):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = os.getenv(config["openai_key"])

    @commands.hybrid_command(
        name="emojimovie",
        description="Play a emoji game"
    )
    @checks.not_blacklisted()
    @app_commands.guilds(discord.Object(id=686705358441545737))
    async def play_emoji_movie(self, ctx: Context):
        start_sequence = "\nA:"
        restart_sequence = "\n\nQ: "

        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="I explain popular movies only using emojis. \n\nQ: Baby Driver\nA: ðððķððŧðŦðĨð°\n\nQ: Lion king\nA: ðĶððððððð\n\nQ: Scar face\nA: ðĪð°ðŦðĢðĪŽðĪīðŧ\n\nQ: Braveheart\nA: ðīó §ó Ēó ģó Ģó īó ŋðĄïļðŠðŧðĨðĪšð\n\nQ: Casino\nA: ð°ð°ðĪĩðŧððŧðŦðĪðĢ\n\nQ: munich\nA: ðŪðąðĪðĪðĢðŦðģïļðĩïļââïļðĪðĪ\n\nQ: Titanic ðĒðððððĨðĒ",
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          stop=["\n"]
        )

        emoji_movie = response["choices"][0]["text"].strip().split(start_sequence)[-1]
        emoji_movie = emoji_movie.replace(restart_sequence, "\n")

        # Send the emoji movie to the channel
        await ctx.send(f"Guess the movie using only emojis: {response.choices[0].text.strip()}")
    
    @commands.hybrid_command(
        name="guess",
        description="Play a emoji game"
    )
    @checks.not_blacklisted()
    @app_commands.guilds(discord.Object(id=686705358441545737))
    async def guess(ctx: Context, *, guess: str):
        if guess.strip() in response.choices[0].text.strip():
            await ctx.send("Congratulations! You got it right!")
        else:
            await ctx.send("Sorry, that's not correct. Better luck next time!")
