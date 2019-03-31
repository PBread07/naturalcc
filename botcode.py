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


    elif message.content.startswith("!zammy in"):
        time_left = time_regex.findall(message.content.lower())
        dt = timedelta(**dict([(convert_time(s), int(t))
                               for (t, s) in time_left]))
        event_datetime = datetime.now() + dt
        event_time_GMT = datetime.strftime(
            event_datetime, '%d %b %Y %I:%M%p') + ' GMT'
        event_time_EST = datetime.strftime(
            event_datetime + timedelta(hours=-4), '%d %b %Y %I:%M%p') + ' EST'

        embed = discord.Embed(title="__**Zamorak God Wars Event:**__", color=0x00ff00)
        embed.add_field(
            name="**Requirements:**", value='- Completion of Death Plateau and start of Troll Stronghold to the point where you defeat Dad.\n- One rope is required to access the dungeon for the first time.\n- Level 70 Hitpoints is required to enter Zamoraks Stronghold (cannot be boosted).\n- At least 43 Prayer for access to the protection prayers.\n- Your prayer will be drained when you enter the Zamorakian area of the dungeon\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/2/2f/K%27ril_Tsutsaroth.png/revision/latest?cb=20150922225829')

        embed.add_field(
            name="**Recommended Levels:**", value='80+ Hitpoints\n80+ Attack\n80+ Strength\n70+ Defence (90+ if Tank)\n80+ Range\n75+ Magic\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/2/2f/K%27ril_Tsutsaroth.png/revision/latest?cb=20150922225829')

        embed.add_field(
            name="**Suggested Gear:**", value='Ranged Attacker: http://prntscr.com/n591ud\nMelee Attaker: http://prntscr.com/n592oh\nZamorak Tank: http://prntscr.com/n597ju\n*If using a blowpipe take addy/better darts\n*If using a crossbow use Diamond bolts (e) & Ruby bolts (e)\n *Spec weapons best to worst DWH>BGS or alternatively Crystal Halberd(i)>Dragon Halberd', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/2/2f/K%27ril_Tsutsaroth.png/revision/latest?cb=20150922225829')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Range Inv: http://prntscr.com/n5965w\nMelee Inv: http://prntscr.com/n595jk\nTank Inv: http://prntscr.com/n596mb\n*Taking alchs allows you to hold more loot\n*Full Guthans switch on the remaining mage, range and melee can extend kills per a trip/n*The boss can hit up to 49 - the tank needs to pay attention, and should never attempt a kill without food. He can drain Prayer and can sometimes hit through protection prayers. Kril Tsutsaroth can also inflict poison damage which starts at 16, so it is advised to wear a Serpentine helm if you are tanking./nAttackers will not be poisoned unless they pull boss aggro off of the tank. Its recommended to bring an antipoison as an attacker as a precaution, especially if you are ranging. If you attack too quickly with your blowpipe, you will draw aggro', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/2/2f/K%27ril_Tsutsaroth.png/revision/latest?cb=20150922225829')
        old_msg=await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("!sara in"):
        time_left = time_regex.findall(message.content.lower())
        dt = timedelta(**dict([(convert_time(s), int(t))
                               for (t, s) in time_left]))
        event_datetime = datetime.now() + dt
        event_time_GMT = datetime.strftime(
            event_datetime, '%d %b %Y %I:%M%p') + ' GMT'
        event_time_EST = datetime.strftime(
            event_datetime + timedelta(hours=-4), '%d %b %Y %I:%M%p') + ' EST'

        embed = discord.Embed(title="__**Saradomin God Wars Event:**__", color=0x00ff00)
        embed.add_field(
            name="**Requirements:**", value='- Completion of Death Plateau and start of Troll Stronghold to the point where you defeat Dad.\n- One rope is required to access the dungeon for the first time.\n- Level 70 Agility is required to enter Saradomins Stronghold (cannot be boosted).\n- At least 43 Prayer for access to the protection prayers.\n- A mithril grapple is required to access the Armadyl encampment.\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fb/Commander_Zilyana.png/revision/latest?cb=20160804022807')

        embed.add_field(
            name="**Recommended Levels:**", value='85+ Hitpoints\n45+ Defence\n85+ Range\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fb/Commander_Zilyana.png/revision/latest?cb=20160804022807')

        embed.add_field(
            name="**Suggested Gear:**", value='Ranged Attacker: http://prntscr.com/n590ar\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fb/Commander_Zilyana.png/revision/latest?cb=20160804022807')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Range Inv: https://prnt.sc/n594p1\n*This boss is killed using a kiting method. While the boss is aggro on you, run away to avoid its melee attacks. While the boss is aggro on another member of the team, you can stand still and attack it/n*Taking alchs allows you to hold more loot./n*Taking Bones to Peaches allows you to have a stackable food source./n*Guthans armor set is generally not useful for this boss. You wont take much damage here..', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fb/Commander_Zilyana.png/revision/latest?cb=20160804022807')
        old_msg=await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("!arma in"):
        time_left = time_regex.findall(message.content.lower())
        dt = timedelta(**dict([(convert_time(s), int(t))
                               for (t, s) in time_left]))
        event_datetime = datetime.now() + dt
        event_time_GMT = datetime.strftime(
            event_datetime, '%d %b %Y %I:%M%p') + ' GMT'
        event_time_EST = datetime.strftime(
            event_datetime + timedelta(hours=-4), '%d %b %Y %I:%M%p') + ' EST'

        embed = discord.Embed(title="__**Armadyl God Wars Event:**__", color=0x00ff00)
        embed.add_field(
            name="**Requirements:**", value='- Completion of Death Plateau and start of Troll Stronghold to the point where you defeat Dad.\n- One rope is required to access the dungeon for the first time.\n- Level 70 Ranged is required to enter Armadyls Encampment (cannot be boosted).\n- At least 43 Prayer for access to the protection prayers.\n- Two additional ropes  are required to access the Saradomin encampment for the first time.\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fd/Kree%27arra.png/revision/latest/scale-to-width-down/699?cb=20160713191756')

        embed.add_field(
            name="**Recommended Levels:**", value='85+ Hitpoints\n70+ Defence\n85+ Range\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fd/Kree%27arra.png/revision/latest/scale-to-width-down/699?cb=20160713191756')

        embed.add_field(
            name="**Suggested Gear:**", value='Ranged Attacker: http://prntscr.com/n590ht\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fd/Kree%27arra.png/revision/latest/scale-to-width-down/699?cb=20160713191756')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Chinning: http://prntscr.com/n593v7\n*Crossbow Only: http://prntscr.com/n5944k/n* Kree arra cannot be damaged with any Melee attacks. He attacks with melee only when he is not under attack, so its important that at least one player is attacking him at all times. His Ranged and Magic attacks hit all players in his chamber with a whirlwind attack that knocks players back and freezes them. His maximum hit is 71 with Ranged, 26 with Melee and 25 with Magic./n*Taking alchs allows you to hold more loot./n* Standing in one of the corners of the room can reduce a lot of damage, since you wont be knocked back by the boss/n* Taking Bones to Peaches allows you to have a stackable food source./n** If you choose to use chinchompas, you will be attacking the melee minion and damaging the boss with AOE damage. When the melee minion is dead, equip your crossbow and attack the boss as normal.', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/f/fd/Kree%27arra.png/revision/latest/scale-to-width-down/699?cb=20160713191756')
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
            name="**Recommended Levels:**", value='75+ Hitpoints\n75+ Attack\n75+ Strength\n75+ Defence\n85+ Range\n75+ Magic\n44+ Prayer (Eagle Eye, 70+ Piety, 74+ Rigour)\n', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')

        embed.add_field(
            name="**Suggested Gear:**", value='Melee Non-Void: http://prntscr.com/lu8g2p\nRange Non-Void: http://prntscr.com/lu8g8p\nVoid Melee (Meta): http://prntscr.com/lu8gsl', inline=False)
        embed.set_footer(text=event_time_EST + ' | ' + event_time_GMT)
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/2007scape/images/5/5c/Corporeal_Beast.png/revision/latest?cb=20160212005921')

        embed.add_field(
            name="**Suggested Inventory Setup:**", value='Void Melee Inv: http://prntscr.com/lu8mwl\n*Special weapons from best to worst DWH>BGS>Arclight>Crystal Halberd', inline=False)
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
