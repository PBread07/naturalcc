import discord
from datetime import datetime, timedelta

import re
time_regex = re.compile(r'(?P<time>[0-9]+)\s*(?P<scale>[dDhHmMsS])')


def convert_time(time_str):
    for scale in ['days', 'hours', 'minutes', 'seconds']:
        if scale.startswith(time_str):
            return scale


TOKEN = 'NTAxNzI0NDg5NTEyNjQ4NzM3.DszX7w.ovuuD0ftVr9zTL79xNeevSbavOM'
client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!userinfo'):
        user = message.author
        # -4h to convert from GMT to EST
        joined_at = datetime.strptime(
            f'{user.joined_at}', '%Y-%m-%d %H:%M:%S.%f') + timedelta(hours=-4)
        joined_at_str = datetime.strftime(
            joined_at, '%d %b %Y %I:%M%p') + ' EST'
        embed = discord.Embed(title="Information report:", color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="Disc ID", value=user.id, inline=True)
        embed.add_field(name="Joined", value=joined_at_str, inline=True)
        embed.add_field(name="Role", value=user.top_role)
        embed.set_thumbnail(url=user.avatar_url)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("!bandos in"):
        time_left = time_regex.findall(message.content.lower())
        dt = timedelta(**dict([(convert_time(s), int(t))
                               for (t, s) in time_left]))
        event_datetime = datetime.now() + dt
        event_time_GMT = datetime.strftime(
            event_datetime, '%d %b %Y %I:%M%p') + ' GMT'
        event_time_EST = datetime.strftime(
            event_datetime + timedelta(hours=-4), '%d %b %Y %I:%M%p') + ' EST'

        embed = discord.Embed(title="Bandos Clan Event:", color=0x00ff00)
        embed.add_field(
            name="Requirements & Suggested Gear:", value='70 Str', inline=False)
        embed.add_field(
            name="Ranged Tank", value='**- Rich http://prntscr.com/ltbiyt**\n**- Poor http://prntscr.com/ltbk3j**\n**- text**\n**- Requirement 4**', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url=message.author.avatar_url)
        old_msg=await client.send_message(message.channel, embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
