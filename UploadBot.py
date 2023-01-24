import os
import random
import string
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#')

@bot.command()
async def upload(ctx, category_id: int, number_of_files: int=None): # Can limit the amount of files sent from each subfolder, but also decide which category to send them in, in this case the file amount is optional
    log_channel_id =  # Replace this with the ID of the channel where you want to send embeds
    category = ctx.guild.get_channel(category_id)
    for folder in os.listdir('media'): # name of the folder where subfolders filled with files are gonna be 
        channel = discord.utils.get(ctx.guild.text_channels, name=folder)
        if channel is None:
            channel = await ctx.guild.create_text_channel(folder, category=category)
        log_channel = ctx.guild.get_channel(log_channel_id)
        files = os.listdir(os.path.join('media', folder))
        if files:
            file = random.choice(files)
            file_path = os.path.join('media', folder, file)
            filename, extension = os.path.splitext(file)
            # Send the file to the channel first
            message = await channel.send(file=discord.File(file_path, filename=f'uploadedthankstokazu{extension}'))
            # Get the URL of the file from the message
            file_url = message.attachments[0].url
            # Create the embed
            embed = discord.Embed(title="A New channel has been created", color=16711888, description="Change me")
            embed.set_author(name='Replace Me')
            # Set the image of the embed to be the file we just sent
            embed.set_image(url=file_url)
            embed.set_footer(text="Any Footer Text You Want")
            embed.add_field(name="Channel Name :", value=channel.mention) #mentions the channel in the embed as a field
            # Send the embed to the log channel
            await log_channel.send(embed=embed)
        else: # In case the file can't be shown in the embed 
            embed = discord.Embed(title="A New channel has been created", color=16711888, description="Change me")
            embed.set_footer(text="Any Footer Text You Want")
            # Send the embed to the log channel
            await log_channel.send(embed=embed)
        i = 0
        for file in os.listdir(os.path.join('media', folder)):
            file_path = os.path.join('media', folder, file)
            if number_of_files is not None:
                if i >= number_of_files:
                    break
            if os.path.getsize(file_path) <= 104857600:  # 100MB in bytes, change it to 8mb in bytes if you don't have a lvl 3 server
                filename, extension = os.path.splitext(file)
                await channel.send(file=discord.File(file_path, filename=f'uploadedthankstokazu{extension}')) #Renames the file before upload, change it to whatever you want if you go through the code ofc
                i += 1
                os.remove(file_path)
                
bot.run('insert-bot-token-here')
