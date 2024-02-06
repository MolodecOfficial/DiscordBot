from discord.ext import commands, tasks
from general_group import GeneralGroup

import discord
import random

GUILD = discord.Object(id=1195804020103721040)


class BotHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        channel = self.get_destination()
        await channel.send("Команды, которые могут выполняться этим ботом:")
        await channel.send("!roll - бросить кубик с рандомным числом до 20")
        await channel.send("!meme - похихикать с мемов")
        await channel.send(
            "!TTT - сыграть в крестики-нолики. Чтобы сделать ход напишите !place и цифру, куда хотите поставить от 1 до 9.")
        await channel.send("Мой создатель: Moloдец, помогал LaUwUrence")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=BotHelpCommand())
bot.tree.add_command(GeneralGroup(bot), guild=GUILD)


@bot.command()
async def meme(context):
    log("> meme")
    channel = context.message.channel
    author = context.message.author
    await context.send("Вороп, увидев в новой обнове Мэри лишь в 1 рендере")
    await context.send(file=discord.File('gifs/yes.gif'))


@bot.event
async def on_ready():
    await bot.tree.sync(guild=GUILD)
    await bot.change_presence(activity=discord.Game("Doing something..."))
    log(f'{bot.user} is online!')


@bot.tree.command(description="Write message to the current channel.", guild=GUILD)
# @commands.has_permissions(administrator=True)
# @commands.is_owner()
async def write(interaction: discord.Interaction, message: str):
    await interaction.response.send_message("Message written.", ephemeral=True, delete_after=0)
    await interaction.channel.send(message)


@bot.command()
async def ask(context):
    log("> ask")
    channel = context.message.channel
    author = context.message.author
    result = random.randint(1, 2)
    if result == 1:
        await context.send(f'{context.author.mention}')
        await context.send(" Я думаю, что..")
        await context.send(file=discord.File('gifs/1.gif'))
    elif result == 2:
        await context.send(f'{context.author.mention}')
        await context.send(" Я думаю, что..")
        await context.send(file=discord.File('gifs/2.gif'))


##################################################################################

@bot.command()
async def roll(context):
    log("> roll")
    channel = context.message.channel
    author = context.message.author
    result = random.randint(1, 20)
    if result == 1:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/1.gif'))
    elif result == 2:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/2.gif'))
    elif result == 3:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/3.gif'))
    elif result == 4:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/4.gif'))
    elif result == 5:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/5.gif'))
    elif result == 6:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/6.gif'))
    elif result == 7:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/7.gif'))
    elif result == 8:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/8.gif'))
    elif result == 9:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/9.gif'))
    elif result == 10:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/10.gif'))
    elif result == 11:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/11.gif'))
    elif result == 12:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/12.gif'))
    elif result == 13:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/13.gif'))
    elif result == 14:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/14.gif'))
    elif result == 15:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/15.gif'))
    elif result == 16:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/16.gif'))
    elif result == 17:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/17.gif'))
    elif result == 18:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/18.gif'))
    elif result == 19:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/19.gif'))
    elif result == 20:
        await context.send(f'{context.author.mention}')
        await context.send(file=discord.File('gifs/20.gif'))


##################################################################################

def log(*args):
    print(*args)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@bot.command()
async def TTT(ctx, p1: discord.Member, p2: discord.Member):
    log("> TTT")
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_square_button:", ":white_square_button:", ":white_square_button:",
                 ":white_square_button:", ":white_square_button:", ":white_square_button:",
                 ":white_square_button:", ":white_square_button:", ":white_square_button:",
                 ":white_square_button:", ":white_square_button:", ":white_square_button:",
                 ":white_square_button:", ":white_square_button:", ":white_square_button:", ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Сейчас ходит <@" + str(player1.id) + ">.")
        elif num == 2:
            turn = player2
            await ctx.send("Сейчас ходит <@" + str(player2.id) + ">.")
    else:
        await ctx.send("Уже запущена игра. Закончите,сначала эту,а потом приступайте к новой.")


@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_square_button:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " Победил!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Ничья. Победила дружба!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Чтобы разместить на поле крестик или нолик, напиши !place и цифру,куда хотите поставить крестик или нолик.")
        else:
            await ctx.send("Сейчас не твой ход.")
    else:
        await ctx.send("Запустите новую игру командой TTT.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@TTT.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Упомяните два человека для использования данной команды. Пример: tictactoe @Nikoscocos @Nikoscocos API.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Упомяните нормально,по правилам. Пример: tictactoe @Nikoscocos @Nikoscocos API.")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Используй после команды place цифры только от 1 до 9 и никаких прочих символов и эмодзи.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Неправильное размещение или место на поле уже занято. Правила ходов в команде place")


bot.run('MTE5NTgwNDAyMDEwMzcyMTA0MA.G0KQnP.Ioyr0QNZmsbVD4zy-BvYdi6bUZX0H1JROVDdzI')
