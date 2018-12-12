# Work with Python 3.6
import discord
from datetime import datetime, timedelta

import re
time_regex = re.compile(r'(?P<time>[0-9]+)\s*(?P<scale>[dDhHmMsS])')


def convert_time(time_str):
    for scale in ['days', 'hours', 'minutes', 'seconds']:
        if scale.startswith(time_str):
            return scale


TOKEN = 'NTAxNzI0NDg5NTEyNjQ4NzM3.DvMNRQ.kLi_CsXaH60sD57LT4q-6oF8E0s'
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
        embed.set_thumbnail(url=message.author.avatar_url)
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

        embed = discord.Embed(title="__**Bandos Clan Event:**__", color=0x00ff00)
        embed.add_field(
            name="**Requirements:**", value='- Completion of Death Plateau and start of Troll Stronghold to the point where you defeat Dad.\n- One rope is required to access the dungeon for the first time.\n- Level 70 Strength is required to enter Bandos Stronghold (cannot be boosted).\n- At least 43 Prayer for access to the protection prayers.\n-A hammer\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/b/b8/General_Graardor.png/revision/latest?cb=20160325023339')

        embed.add_field(
            name="**Recommended Levels:**", value='80+ Hitpoints\n80+ Attack\n80+ Strength\n70+ Defence (90+ if Tank)\n80+ Range\n75+ Magic\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/b/b8/General_Graardor.png/revision/latest?cb=20160325023339')

        embed.add_field(
            name="**Suggested Gear:**", value='Bandos Basic Tank: http://prntscr.com/lu5tlb\nBandos Advanced Tank: http://prntscr.com/lu5twd\nBandos Melee Attacker: http://prntscr.com/lu5ubt\nBandos Ranged Attacker: http://prntscr.com/lu5uoi\nBandos Blowpipe Attacker: http://prntscr.com/lu7xo5\n*If using a blowpipe take addy/better darts\n*If using a crossbow use Diamond bolts (e) & Ruby bolts (e)\n *Spec weapons best to worst DWH>BGS or alternatively Crystal Halberd(i)>Dragon Halberd', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/b/b8/General_Graardor.png/revision/latest?cb=20160325023339')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Melee Inv: http://prntscr.com/lu6xno\nRanged Inv: http://prntscr.com/lu6xdm\nAdvanced Inv: http://prntscr.com/lu6xwa\n*Taking alchs allows you to hold more loot\n*Taking Bones to Peaches allows you to have a stackable food source\n*Full Guthans switch on the remaining mage, range and melee can extend kills per a trip', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/b/b8/General_Graardor.png/revision/latest?cb=20160325023339')
        old_msg=await client.send_message(message.channel, embed=embed)



    elif message.content.startswith("!corp in"):
        time_left = time_regex.findall(message.content.lower())
        dt = timedelta(**dict([(convert_time(s), int(t))
                               for (t, s) in time_left]))
        event_datetime = datetime.now() + dt
        event_time_GMT = datetime.strftime(
            event_datetime, '%d %b %Y %I:%M%p') + ' GMT'
        event_time_EST = datetime.strftime(
            event_datetime + timedelta(hours=-4), '%d %b %Y %I:%M%p') + ' EST'

        embed = discord.Embed(title="__**Corporeal Beast Clan Event:**__", color=0x00ff00)
        embed.add_field(
            name="**Requirements:**", value='A bunch of Games Necklaces and Ring of Duelings or a Friend with a Ornate Rejuvenation Pool and Ornate jewellery Box in thier Player Owned House\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')

        embed.add_field(
            name="**Recommended Levels:**", value='75+ Hitpoints\n75+ Attack\75+ Strength\n75+ Defence\n85+ Range\n75+ Magic\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')

        embed.add_field(
            name="**Suggested Gear:**", value='Melee Non-Void: http://prntscr.com/lu8g2p\nRange Non-Void: http://prntscr.com/lu8g8p\nVoid Melee (Meta): http://prntscr.com/lu8gsl', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Void Melee Inv: http://prntscr.com/lu8mwl\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')
        old_msg=await client.send_message(message.channel, embed=embed)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
