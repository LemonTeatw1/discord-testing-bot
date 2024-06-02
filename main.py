import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def ready():
    print("now login as" , bot.user)
    game = discord.Game('正在開發程式')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.slash_command()
async def embed(message = None, 標題 = None, 說明 = None, 內文1= None, 內文1說明 = None, 內文2 = None, 內文2說明 = None, 圖片 = None):
    title = 標題
    description = 說明
    field1_title = 內文1
    field1_value = 內文1說明
    field2_title = 內文2
    field2_value = 內文2說明
    set_image = 圖片

    embed = discord.Embed(title=title, description=description)
    embed.add_field(name=field1_title, value=field1_value, inline=False)
    embed.add_field(name=field2_title, value=field2_value, inline=False)
    embed.set_image(url=set_image)

    await message.channel.send(embed=embed)










bot.run('TOKEN')
