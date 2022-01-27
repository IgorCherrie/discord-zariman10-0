import discord
from discord.ext import commands
import os, sqlite3

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} on the server'.format(client))


# 809366883014803478 - channel_maker_test
# 809366952060387338 - category_voice_test

# 936002680655077376 - channel_maker_main
# 936002679405154335 - category_voice_main



@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        if after.channel.id ==936002680655077376: # channel
            maincategory = discord.utils.get(member.guild.categories, id=936002679405154335) # category
            channel = await member.guild.create_voice_channel(name=f'{member.display_name}s room', category=maincategory)

            await channel.set_permissions(member, connect=True, mute_members=False, move_members=True,
                                          manage_channels=True)

            await member.move_to(channel)

            def check(x, y, z):
                return len(channel.members) == 0

            await client.wait_for('voice_state_update', check=check)
            await channel.delete()


client.run('ODc5OTk2ODgxMDQ3MDIzNjU3.YSX29Q.KEhIRVccMQ7DgsNqEKyrKlbmgBQ')