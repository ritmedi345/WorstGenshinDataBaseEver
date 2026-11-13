from drafter import *
from dataclasses import dataclass
#from FischlFile import *
#from ArlecchinoFile import *
#from ClorindeFile import *
#from KokomiFile import *

#from pythonGenshinCharacters import *
#from mainGenshinCharactersNonDrafter import *

#Clroinde File

clorindeNormals = {'name': 'Oath of the Hunting Shadow'
                   
                   ,'talent info': """Normal Attack
Performs up to 5 rapid strikes.

Charged Attack
Consumes a certain amount of Stamina and fires Suppressing Shots in a fan pattern with her pistolet.

Plunging Attack
Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact."""
                   
                   ,"lv1": {"1 hit": "54.1%"
                           ,"2 hit": "51.6%"
                           ,"3 hit": "34.2*2%"
                           ,"4 hit": "23.1*3%"
                           ,"5 hit": "90%"
                           ,"charged attack": "128.1%"
                           ,"charged attack stamina cost": "20"
                           ,"plunge": "63.9%"
                           ,"low plunge": "128%"
                           ,"high plunge": "160%"}
                   
                   ,"lv9": {"1 hit": "99.3%"
                           ,"2 hit": "94.9%"
                           ,"3 hit A": "62.8%"
                           ,"3 hit B": "62.8%"
                           ,"4 hit A": "42.5%"
                           ,"4 hit B": "42.5%"
                           ,"4 hit C": "42.5%"
                           ,"5 hit": "165.4%"
                           ,"charged attack": "235.4%"
                           ,"charged attack stamina cost": "20"
                           ,"plunge": "117.5%"
                           ,"low plunge": "235%"
                           ,"high plunge": "293%"}
                   
                   ,"lv10": {"1 hit": "106.9%"
                           ,"2 hit": "102.1%"
                           ,"3 hit": "67.6*2%"
                           ,"4 hit": "45.7*3%"
                           ,"5 hit": "177.9%"
                           ,"charged attack": "253.3%"
                           ,"charged attack stamina cost": "20"
                           ,"plunge": "126.4%"
                           ,"low plunge": "253%"
                           ,"high plunge": "316%"}}

clorindeSkill = {'name': "Hunter's Vigil"
                 
                 ,'talent info': """Preparing her pistolet, she enters the "Night Vigil" state, using steel and shot together. In this state, Clorinde's Normal Attacks will be transformed into "Swift Hunt" pistolet attacks, and the DMG dealt is converted into Electro DMG that cannot be overridden by infusions, and she will be unable to use Charged Attacks. Using her Elemental Skill will transform it into "Impale the Night": Perform a lunging attack, dealing Electro DMG. The DMG done through the aforementioned method is considered Normal Attack DMG.

Swift Hunt
· When her Bond of Life is equal to or greater than 100% of her max HP: Performs a pistolet shot.
· When her Bond of Life is less than 100%, firing her pistolet will grant her Bond of Life, with the amount gained based on her max HP. The shots she fires can pierce opponents, and DMG dealt to opponents in their path is increased.

Impale the Night
The current percentage value of Clorinde's Bond of Life determines its effect:
· When the Bond of Life value is 0%, perform a normal lunging strike;
· When the Bond of Life value is less than 100% of her max HP, Clorinde is healed based on the Bond of Life value, and the AoE of the lunging attack and the DMG dealt is increased;
· When the value of the Bond of Life is equal to or greater than 100% of her max HP, use Impale the Night: Pact. The healing multiplier is increased, and the AoE and DMG dealt by the lunge is increased even further.

In addition, when Clorinde is in the Night Vigil state, healing effects other than Impale the Night will not take effect and will instead be converted into a Bond of Life that is a percentage of the healing that would have been received.

Clorinde will exit the "Night Vigil" state when she leaves the field.

Arkhe: Ousia
Periodically, when Clorinde's Swift Hunt shots strike opponents, she will summon a Surging Blade at the position hit that deals Ousia-aligned Electro DMG.

Though the evil that lurked in the shadows of the night had been purged across thousands of years, a shadow that the light could not reach clouded human hearts.
Even now, the warning left by the Golden Hunter is etched into her memory: Those of the Night Vigil, carrying aloft lit candles against the blackness, have greater need still to remain vigilant. Be not corrupted by the cold dark."""
                 
                 ,"lv1": {"Swift Hunt damage": ""
                         ,"Swift Hunt Bond of Life gain": ""
                         ,"Impale the Night damage": ""
                         ,"Impale the night healing": ""
                         ,"Bond of Life Conversion": "80%"
                         ,"Surging Blade Damage": ""
                         ,"Surging Blade Interval": "10s"
                         ,"Night Vigil State Duration": "7.5s"
                         ,"CD": "16s"}
                 
                 ,"lv9": {"Swift Hunt damage": ""
                         ,"Swift Hunt Bond of Life gain": ""
                         ,"Impale the Night damage": ""
                         ,"Impale the night healing": ""
                         ,"Bond of Life Conversion": "80%"
                         ,"Surging Blade Damage": ""
                         ,"Surging Blade Interval": "10s"
                         ,"Night Vigil State Duration": "7.5s"
                         ,"CD": "16s"}
                 
                 ,"lv10": {"Swift Hunt damage": ""
                         ,"Swift Hunt Bond of Life gain": ""
                         ,"Impale the Night damage": ""
                         ,"Impale the night healing": ""
                         ,"Bond of Life Conversion": "80%"
                         ,"Surging Blade Damage": ""
                         ,"Surging Blade Interval": "10s"
                         ,"Night Vigil State Duration": "7.5s"
                         ,"CD": "16s"}
                 
                 ,"lv12": {"Swift Hunt damage": ""
                         ,"Swift Hunt Bond of Life gain": ""
                         ,"Impale the Night damage": ""
                         ,"Impale the night healing": ""
                         ,"Bond of Life Conversion": "80%"
                         ,"Surging Blade Damage": ""
                         ,"Surging Blade Interval": "10s"
                         ,"Night Vigil State Duration": "7.5s"
                         ,"CD": "16s"}
                 
                 ,"lv13": {"Swift Hunt damage": ""
                         ,"Swift Hunt Bond of Life gain": ""
                         ,"Impale the Night damage": ""
                         ,"Impale the night healing": ""
                         ,"Bond of Life Conversion": "80%"
                         ,"Surging Blade Damage": ""
                         ,"Surging Blade Interval": "10s"
                         ,"Night Vigil State Duration": "7.5s"
                         ,"CD": "16s"}}

clorindeBurst = {'name': "Last Lightfall"
                 
                 ,'talent info': """Grants herself a Bond of Life based upon her own max HP before swiftly evading and striking with saber and sidearm as one, dealing AoE Electro DMG.

It is said the legacy of the ancient art of resisting non-human beings with but a mortal body can be traced back to the Lochknights who resisted the Remurian Empire.
Be that as it may, so long as one can find a way to control the level of force used, it's not as if it cannot be used in duels against ordinary opponents."""
                 
                 ,"lv1": {"Skill Damage": "126.9*5%"
                         ,"Bond of Life Gain": "% Max Health"
                         ,"CD": "15s"
                         ,"Energy Cost": "60"}
                 
                 ,"lv9": {"Skill Damage": "215.7*5%"
                         ,"Bond of Life Gain": "114% Max Health"
                         ,"CD": "15s"
                         ,"Energy Cost": "60"}
                 
                 ,"lv10": {"Skill Damage": "228.4*5%"
                         ,"Bond of Life Gain": "120% Max Health"
                         ,"CD": "15s"
                         ,"Energy Cost": "60"}
                 
                 ,"lv13": {"Skill Damage": "269.6*5%"
                         ,"Bond of Life Gain": "138% Max Health"
                         ,"CD": "15s"
                         ,"Energy Cost": "60"}}

clorindeBaseStats = {"hp": {"lv80/90": "12045"
                           ,"lv90/90": "12956"
                           ,"lv100/100": "13877"}
                    
                    ,"atk": {"lv80/90": "314"
                           ,"lv90/90": "337"
                           ,"lv100/100": "413"}
                    
                    ,"def": {"lv80/90": "729"
                           ,"lv90/90": "784"
                           ,"lv100/100": "840"}}

clorindePassives = {"Dark-Shattering Flame": """After a nearby party member triggers an Electro-related reaction against an opponent, Electro DMG dealt by Clorinde's Normal Attacks and Last Lightfall will be increased by 20% of Clorinde's ATK for 15s. Max 3 stacks. Each stack is counted independently. The Maximum DMG increase achievable this way for the above attacks is 1,800."""
                    ,"Lawful Remuneration": """If Clorinde's Bond of Life is equal to or greater than 100% of her Max HP, her CRIT Rate will increase by 10% for 15s whenever her Bond of Life value increases or decreases. Max 2 stacks. Each stack is counted independently.
Additionally, Hunter's Vigil's Night Vigil state is buffed: While it is active, the percent of healing converted to Bond of Life increases to 100%."""
                    ,"Night Vigil's Harvest" : """Displays the location of nearby resources unique to Fontaine on the mini-map."""}

clorindeConstellations = {'"From This Day, I Pass the Candle' + "'s " + 'Shadow-Veil" '  : """While Hunter's Vigil's Night Vigil state is active, when Electro DMG from Clorinde's Normal Attacks hit opponents, they will trigger 2 coordinated attacks from a Nightvigil Shade summoned near the hit opponent, each dealing 30% of Clorinde's ATK as Electro DMG.
This effect can occur once every 1.2s. DMG dealt this way is considered Normal Attack DMG."""
                          ,'"Now, As We Face the Perils of the Long Night" ' : """Enhance the Ascension Talent "Dark-Shattering Flame": After a nearby party member triggers an Electro-related reaction against an opponent, Electro DMG dealt by Clorinde's Normal Attacks and Last Lightfall will be increased by 30% of Clorinde's ATK for 15s. Max 3 stacks. Each stack is counted independently. When you have 3 stacks, Clorinde's interruption resistance will be increased. The Maximum DMG increase achievable this way for the above attacks is 2,700.
You must first unlock the Ascension""" + ' Talent "Dark-Shattering Flame." '
                          ,'"I Pledge to Remember the Oath of Daylight"' : """Increases the Level of Hunter's Vigil by 3.
Maximum upgrade level is 15."""
                          ,'"To Enshrine Tears, Life, and Love"' : """When Last Lightfall deals DMG to opponent(s), DMG dealt is increased based on Clorinde's Bond of Life percentage. Every 1% of her current Bond of Life will increase Last Lightfall DMG by 2%. The maximum Last Lightfall DMG increase achievable this way is 200%."""
                          ,'"Holding Dawn"' +  "'s Coming as My Votive" + '"' : """Increases the Level of Last Lightfall by 3.
Maximum upgrade level is 15."""
                          , '"And So Shall I Never Despair"' : """For 12s after Hunter's Vigil is used, Clorinde's CRIT Rate will be increased by 10%, and her CRIT DMG by 70%.
Additionally, while Night Vigil is active, a Glimbright Shade will appear under specific circumstances, executing an attack that deals 200% of Clorinde's ATK as Electro DMG. DMG dealt this way is considered Normal Attack DMG.
The Glimbright Shade will appear under the following circumstances:
· When Clorinde is about to be hit by an attack.
· When Clorinde uses Impale the Night: Pact.
1 Glimbright Shade can be summoned in the aforementioned ways every 1s. 6 Shades can be summoned per single Night Vigil duration.
In addition, while Night Vigil is active, the DMG Clorinde receives is decreased by 80% and her interruption resistance is increased. This effect will disappear after the Night Vigil state ends or 1s after she summons 6 Glimbright Shades."""}

#Clorinde file end

#Fischl File Start
#fischlFile

fischlNormals = {"name": """Bolts of Downfall"""
    
                ,"talent info": '''Normal Attack Performs up to 5 consecutive shots with a bow.
Charged Attack
Performs a more precise Aimed Shot with increased DMG.
While aiming, the dark lightning spirits of Immernachtreich shall heed the call of their Prinzessin and indwell the enchanted arrowhead. When fully indwelt, the Rachsüchtig Blitz shall deal immense Electro DMG.

Plunging Attack
Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact.'''
    
                ,"lv1": {"1 hit": "44.1%"
                         ,"2 hit": "46.8%"
                         ,"3 hit": "58.1%"
                         ,"4 hit": "57.7%"
                         ,"5 hit": "72.1%"
                         ,"aimed shot": "43.9%"
                         ,"fully charged": "124%"
                         ,"plunge": "56.8%"
                         ,"low plunge": "114%"
                         ,"high plunge": "142%" }
                 
                 , "lv10": {"1 hit": "87.2%"
                         ,"2 hit": "92.5%"
                         ,"3 hit": "115%"
                         ,"4 hit": "114%"
                         ,"5 hit": "142%"
                         ,"aimed shot": "86.7%"
                         ,"fully charged": "223%"
                         ,"plunge": "112.3%"
                         ,"low plunge": "225%"
                         ,"high plunge": "281%" }}

fischlSkill = {"name": "Nightrider"
               
               ,"talent info": """Summons Oz. The night raven forged of darkness and lightning descends upon the land, dealing Electro DMG in a small AoE.
For the ability's duration, Oz will continuously attack nearby opponents with Freikugel.

Hold to adjust the location Oz will be summoned to.
Press again any time during the ability's duration to once again summon him to Fischl's side.

"My time is most precious, and I shall not waste it on the likes of you... Go, Oz, fall upon them, and bring down upon them your Rachsüchtig Blitz, that which tears open the long night."
—Flowers for Princess Fischl (IV): Farewell Frau Welt"""
               
               ,"lv1": {"Oz": "88.8%"
                       ,"Summoning Damage": "115%"
                       ,"Oz Duration": "10s"
                       ,"CD": "25s"}
               
               ,"lv10": {"Oz": "160%"
                       ,"Summoning Damage": "208%"
                       ,"Oz Duration": "10s"
                       ,"CD": "25s"}
               
               ,"lv13": {"Oz": "189%"
                       ,"Summoning Damage": "245%"
                       ,"Oz Duration": "10s"
                       ,"CD": "25s"}}

fischlBurst = {'name': 'Midnight Phantasmagoria'
               
               ,'talent info': """Summons Oz to spread his twin wings of twilight and defend Fischl.
Has the following properties during the ability's duration:
·Fischl takes on Oz's form, greatly increasing her Movement Speed.
·Strikes nearby opponents with lightning, dealing Electro DMG to opponents she comes into contact with. Each opponent can only be struck once.
·Once this ability's effects end, Oz will remain on the battlefield and attack his Prinzessin's foes. If Oz is already on the field, then this will reset the duration of his presence.

"...In the hordes of beasts that follow the cursed blood, only Prince Nachtraben, who bore witness to the extinction of a thousand worlds, knows her true greatness. Thus the night wings he spreads are his eternal promise to protect Her Royal Highness."
—Flowers for Princess Fischl (I): End Time Zersetzung"""
               
               ,"lv1": {"Falling Thunder": "208%"
                       ,"CD": "15"
                       ,"Energy Cost": "60"}
               
               ,"lv10": {"Falling Thunder": "374%"
                       ,"CD": "15"
                       ,"Energy Cost": "60"}
               
               ,"lv13": {"Falling Thunder": "442%"
                       ,"CD": "15"
                       ,"Energy Cost": "60"}}

fischlBaseStats = {"hp": {"lv80/90": "8553"
                          ,"lv90/90": "9189"
                          ,"lv100/100": "9825" }
                   ,"atk": {"lv80/90": "227"
                           ,"lv90/90": "244"
                           ,"lv100/100": "307"}
                   ,"def": {"lv80/90": "553"
                            ,"lv90/90": "594"
                            ,"lv100/100": "635"}
                   ,"cr": "5%"
                   ,"cd": "50%"
                   ,"em": 0 }

fischlConstellations = {"Gaze of the Deep" : """Even when Oz is not present in combat, he can still watch over Fischl through his raven eyes. When Fischl performs a Normal Attack against an opponent, Oz fires a coordinated attack, dealing DMG equal to 22% of Fischl's ATK."""
                        , "Devourer of All Sins": '''When Nightrider is used, it deals an additional 200% ATK as DMG, and its AoE is increased by 50%.'''
                        , 'Wings of Nightmare': '''Increases the Level of Nightrider by 3.
Maximum upgrade level is 15.'''
                        , 'Her Pilgramage of Bleak': '''When Midnight Phantasmagoria is used, it deals 222% of ATK as Electro DMG to surrounding opponents.
When the skill duration ends, Fischl regenerates 20% of her HP.'''
                        ,'Against the Fleeting Light': '''Increases the Level of Midnight Phantasmagoria by 3.
Maximum upgrade level is 15.'''
                        ,'Evernight Raven': '''Extends the duration of Oz's presence on the field by 2s. Additionally, Oz performs coordinated attacks with your active character when present, dealing 30% of Fischl's ATK as Electro DMG.'''}

fischlPassives = {'Stellar Predator': '''When Fischl hits Oz with a fully-charged Aimed Shot, Oz brings down Thundering Retribution, dealing AoE Electro DMG equal to 152.7% of the arrow's DMG.'''
                  , 'Undone By Thy Sinful Hex': '''If your current active character triggers an Electro-related Elemental Reaction when Oz is on the field, the opponent shall be stricken with Thundering Retribution that deals Electro DMG equal to 80% of Fischl's ATK.'''
                  , 'Mein Hausgarten': '''When dispatched on an expedition in Mondstadt, time consumed is reduced by 25%.'''
                  , "Witch's Eve Right: Phantasmal Nocturne" : """After completing Witch's Homework: Of the Unexpected, Fischl will become a Hexerei character. When the party includes at least 2 Hexerei characters, you will gain the Hexerei: Secret Rite effect, which enhances Hexerei characters.

Hexerei: Secret Rite
Hark, Prince Nachtraben, Ozvaldo Hrafnavins, he who has witnessed the fall of countless worlds. Sing now the starry septet for your sovereign, for this is the moment of deepest sin, when the gathered souls at the end of causality shatter the darkness of fate.
Additionally, when Oz is on the field, party members will gain additional buff effects:
· After a nearby party member triggers an Overloaded reaction, Fischl and other nearby active party members have their ATK increased by 22.5% for 10s.
· After a nearby party member triggers an Electro-Charged or Lunar-Charged reaction, Fischl and other nearby active party members have their Elemental Mastery increased by 90 for 10s."""  }

#Fischl File End

#Sangonomiya Kokomi file

kokomiBaseStats = {"hp": {'80/90': '12524'
                              ,'90/90': '13471'
                              ,'100/100': '14428'}
                       
                       ,"atk": {'80/90': '218'
                              ,'90/90': '234'
                              ,'100/100': '287'}
                       
                       ,"def": {'80/90': '611'
                              ,'90/90': '657'
                              ,'100/100': '704'}}

kokomiNormals = {'name': "The Shape of Water"
                     
                     ,'talent info': """Normal Attack
Performs up to 3 consecutive attacks that take the form of swimming fish, dealing Hydro DMG.

Charged Attack
Consumes a certain amount of Stamina to deal AoE Hydro DMG after a short casting time.

Plunging Attack
Gathering the might of Hydro, Kokomi plunges towards the ground from mid-air, damaging all opponents in her path. Deals AoE Hydro DMG upon impact with the ground."""
                     
                     ,"lv1": {"1 hit": "68.4%"
                              ,'2 hit': "61.5%"
                              , '3 hit': "94.3%"
                              , "charged attack": "148%"
                              ,"charged attack stamina cost": "50"
                              ,"plunge damage": "56.8%"
                              , "low plunge": "114%" 
                              , "high plunge" : "142%" }
                     
                     ,"lv10": {"1 hit": "123.1%"
                              ,'2 hit': "110.8%"
                              , '3 hit': "169.8%"
                              , "charged attack": "267%"
                              ,"charged attack stamina cost": "50"
                              ,"plunge damage": "112.3%"
                              , "low plunge": "225%" 
                              , "high plunge" : "281%" }}

kokomiSkill = {'name': "Kurage's Oath"
                   
                   ,'talent info': """Summons a "Bake-Kurage" created from water that can heal her allies.
Using this skill will apply the Wet status to Sangonomiya Kokomi.

Bake-Kurage
Deals Hydro DMG to surrounding opponents and heals nearby active characters at fixed intervals. This healing is based on Kokomi's Max HP.

Kokomi needs timely "refreshment" in order to maintain optimal work efficiency."""
                   
                   ,"lv1": {"healing": "4.4% Max HP + 423"
                            , "damage": "109.2%"
                            , "duration": "12s"
                            , "CD": "20s"}
                   
                   ,"lv10": {"healing": "7.9% Max HP + 932"
                            , "damage": "196.5%"
                            , "duration": "12s"
                            , "CD": "20s"}
               
                   ,"lv13": {"healing": "9.4% Max HP + 1165"
                            , "damage": "232%"
                            , "duration": "12s"
                            , "CD": "20s"}}

kokomiBurst = {'name': "Nereid's Ascension"
                   
                   ,'talent info': """Summons the might of Watatsumi, dealing Hydro DMG to surrounding opponents, before robing Kokomi in a Ceremonial Garment made from the flowing waters of Sangonomiya.

Ceremonial Garment
·Sangonomiya Kokomi's Normal Attack, Charged Attack and Bake-Kurage DMG are increased based on her Max HP.
·When her Normal and Charged Attacks hit opponents, Kokomi will restore HP for all nearby party members, and the amount restored is based on her Max HP.
·Increases Sangonomiya Kokomi's resistance to interruption and allows her to walk on the water's surface.

These effects will be cleared once Sangonomiya Kokomi leaves the field.

Clear light coalesces into robes around Her Excellency, Sangonomiya Kokomi, reflecting her magnificent form."""
                   
                   ,"lv1": {"skill damage": "10.4% Max HP"
                            ,"normal attack bonus": "4.8% Max HP"
                            , "charged attack bonus": "6.8% Max HP"
                            , "bake-kurage bonus": "7.1% Max HP"
                            , "healing per hit": "0.81% Max HP + 77"
                            , "duration": "10s"
                            , "CD": "18s"
                            , "energy cost": "70"}
                   
                   ,"lv10": {"skill damage": "18.7% Max HP"
                            ,"normal attack bonus": "8.7% Max HP"
                            , "charged attack bonus": "12.2% Max HP"
                            , "bake-kurage bonus": "12.8% Max HP"
                            , "healing per hit": "1.45% Max HP + 169"
                            , "duration": "10s"
                            , "CD": "18s"
                            , "energy cost": "70"}
                   
                   ,"lv13": {"skill damage": "22.1% Max HP"
                            ,"normal attack bonus": "10.3% Max HP"
                            , "charged attack bonus": "14.4% Max HP"
                            , "bake-kurage bonus": "15.1% Max HP"
                            , "healing per hit": "1.72% Max HP + 211"
                            , "duration": "10s"
                            , "CD": "18s"
                            , "energy cost": "70"}}

kokomiPassives = {"Princess of Watatsumi" : """Decreases swimming Stamina consumption for your own party members by 20%.
Not stackable with Passive Talents that provide the exact same effects."""
                      
                      ,"Flawless Strategy"  : """Sangonomiya Kokomi has a 25% Healing Bonus, but a 100% decrease in CRIT Rate."""
                      
                      ,"Tamakushi Casket" : """If Sangonomiya Kokomi's own Bake-Kurage is on the field when she uses Nereid's Ascension, the Bake-Kurage's duration will be refreshed."""
                      
                      ,"Song of Pearls" : """While donning the Ceremonial Garment created by Nereid's Ascension, the Normal and Charged Attack DMG Bonus Sangonomiya Kokomi gains based on her Max HP will receive a further increase based on 15% of her Healing Bonus."""}

kokomiConstellations = {"At Water's Edge" : """While donning the Ceremonial Garment created by Nereid's Ascension, the final Normal Attack in Sangonomiya Kokomi's combo will unleash a swimming fish to deal 30% of her Max HP as Hydro DMG.
This DMG is not considered Normal Attack DMG."""
                      
                      ,"The Clouds Like Waves Rippling"  : """Sangonomiya Kokomi gains the following Healing Bonuses with regard to characters with 50% or less HP via the following methods:
·Kurage's Oath Bake-Kurage: 4.5% of Kokomi's Max HP.
·Nereid's Ascension Normal and Charged Attacks: 0.6% of Kokomi's Max HP."""
                      
                      ,"The Moon, A Ship O'er the Seas" : """Increases the Level of Nereid's Ascension by 3.
Maximum upgrade level is 15."""
                      
                      ,"The Moon Overlooks the Waters " : """While donning the Ceremonial Garment created by Nereid's Ascension, Sangonomiya Kokomi's Normal Attack SPD is increased by 10%, and Normal Attacks that hit opponents will restore 0.8 Energy for her.
This effect can occur once every 0.2s."""
                            
                            ,"All Streams Flow to the Sea" : """Increases the Level of Kurage's Oath by 3.
Maximum upgrade level is 15."""
                            
                            , "Sango Isshin" : """While donning the Ceremonial Garment created by Nereid's Ascension, Sangonomiya Kokomi gains a 40% Hydro DMG Bonus for 4s when her Normal and Charged Attacks heal, or would heal, any party member with 80% or more HP."""}
#kokomi file ended

#Arlecchino

arlecchinoBaseStats = {"hp": {'80/90': '12182'
                              ,'90/90': '13013'
                              ,'100/100': '14034'}
                       
                       ,"atk": {'80/90': '318'
                              ,'90/90': '342'
                              ,'100/100': '419'}
                       
                       ,"def": {'80/90': '711'
                              ,'90/90': '765'
                              ,'100/100': '819'}}

arlecchinoNormals = {'name': "Invitation to a Beheading"
                     
                     ,'talent info': """Normal Attack
Performs up to 6 consecutive spear strikes.

Charged Attack
Consumes a fixed amount of Stamina, dashing toward a nearby opponent and cleaving once.
Continuously holding this button will cause Arlecchino to consume Stamina and engage in up to 5s of high-speed movement.

Plunging Attack
Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact.

Masque of the Red Death
When Arlecchino has a Bond of Life equal to or greater than 30% of her Max HP, she will enter the "Masque of the Red Death" state, where her Normal, Charged, and Plunging Attacks will be converted to deal Pyro DMG. This cannot be overridden.
When in the "Masque of the Red Death" state, Arlecchino's Normal Attacks will deal extra DMG to opponents on hit that scales off her ATK multiplied by a certain ratio of her current Bond of Life percentage. This will consume 7.5% of said current Bond of Life. Her Bond of Life can be consumed this way every 0.03s. When her Bond of Life is consumed in this manner, All Is Ash's CD will decrease by 0.8s."""
                     
                     ,"lv1": {"masque of the red death increase": "120.4%"
                              ,"1 hit": "47.5%"
                              , "2 hit": "52.1%"
                              , "3 hit": "65.4%"
                              , "4 hit": "37.1*2%"
                              , "5 hit": "70%"
                              , "6 hit": "85.4%"
                              , "charged attack": "90.8%"
                              , "charged attack stamina cost": "25"
                              , "high speed movement": "40/s"
                              , "plunge damage" : "63.9%"
                              , "low plunge": "127.8%"
                              , "high plunge": "159.7%" }
                     
                     ,"lv10": {"masque of the red death increase": "238%"
                              ,"1 hit": "93.9%"
                              , "2 hit": "103%"
                              , "3 hit": "129.3%"
                              , "4 hit": "73.4*2%"
                              , "5 hit": "138.3%"
                              , "6 hit": "168.8%"
                              , "charged attack": "179.5%"
                              , "charged attack stamina cost": "25"
                              , "high speed movement": "40/s"
                              , "plunge damage" : "126.4%"
                              , "low plunge": "252.7%"
                              , "high plunge": "315.6%" }
                     
                     ,"lv13": {"masque of the red death increase": "288.4%"
                              ,"1 hit": "113.8%"
                              , "2 hit": "124.8%"
                              , "3 hit": "156.6%"
                              , "4 hit": "89*2%"
                              , "5 hit": "167.6%"
                              , "6 hit": "204.5%"
                              , "charged attack": "217.5%"
                              , "charged attack stamina cost": "25"
                              , "high speed movement": "40/s"
                              , "plunge damage" : "153.1%"
                              , "low plunge": "306.2%"
                              , "high plunge": "382.5%" }}

arlecchinoSkill = {'name': "All Is Ash"
                   
                   ,'talent info': """Summons forth Balemoon Bloodfire, dealing Pyro DMG to multiple nearby opponents and performing a dash-cleave against one of them, dealing AoE Pyro DMG.
Opponents hit by the aforementioned attack will have a Blood-Debt Directive applied to them.

Blood-Debt Directive
·Lasts 30s. Every 5s, it will deal 1 instance of Pyro DMG to the opponent. Max 2 instances. This DMG will be considered Elemental Skill DMG.
·When Arlecchino uses a Charged Attack or her Elemental Burst, Balemoon Rising, she will absorb and clear nearby Blood-Debt Directives. Each Directive absorbed grants her a Bond of Life worth 65% of her Max HP.
·The maximum value of the Bond of Life she can be granted through Blood-Debt Directives within 35s after using her Elemental Skill is 145% of her Max HP. Using the Elemental Skill again during this duration will restart the count on duration and the limit on the value of Bond of Life she may gain from Blood-Debt Directives.

As she sees it, not every grain of wheat that falls upon the earth will grow into an ear, while those who obstruct her, once burned to ashes, can certainly be used to nourish flowers."""
                   
                   ,"lv1": {"spike damage": "14.8%"
                            ,"cleave damage": "133.6%"
                            , "blood-debt directive damage": "31.8%"
                            , "CD": "30s" }
                   
                   ,"lv10": {"spike damage": "26.7%"
                            ,"cleave damage": "240.4%"
                            , "blood-debt directive damage": "57.2%"
                            , "CD": "30s" }}

arlecchinoBurst = {'name': "Balemoon Rising"
                   
                   ,'talent info': """Arlecchino's great wing of Balemoon Bloodfire beats as she absorbs and clears Blood-Debt Directives around her. She deals AoE Pyro DMG before clearing the CD of All Is Ash and healing herself. The healing is based on her Bond of Life value and ATK.

It is commonly believed throughout Teyvat that moon phases other than the full moon are mere metaphors of ill-omen, used only by those who practice alchemy and astrology.
She saw this crimson moon in her dreams many times. Were those portents of disaster? Indeed they were, but the destined catastrophes belonged to those who enraged her."""
                   
                   ,"lv1": {"burst damage": "370.4%"
                            , "hp restore": "150% Bond of Life + 150% atk"
                            , "CD": "15s"
                            , "energy cost": "60"}
                   
                   ,"lv10": {"burst damage": "666.7%"
                            , "hp restore": "150% Bond of Life + 150% atk"
                            , "CD": "15s"
                            , "energy cost": "60"}
                   
                   ,"lv13": {"burst damage": "787.1%"
                            , "hp restore": "150% Bond of Life + 150% atk"
                            , "CD": "15s"
                            , "energy cost": "60"}}

arlecchinoPassives = {"Agony Alone May Be Repaid" : """Blood-Debt Directives have the following characteristics:
·Arlecchino will be granted a Bond of Life worth 130% of her Max HP when an opponent to which she herself applied a Directive is defeated.
·5s after a Directive is applied, it will be upgraded to a Blood-Debt Due. When absorbed, it will instead grant Arlecchino a Bond of Life worth 130%.
A Bond of Life created in the aforementioned ways cannot exceed the original limit on the value of Bonds of Life obtained through All Is Ash."""
                      
                      ,"Strength Alone Can Defend"  : """Arlecchino gains 1% All Elemental and Physical RES for every 100 ATK she has in excess of 1,000. The maximum RES increase she can gain this way for each is 20%."""
                      
                      ,"The Balemoon Alone May Know" : """While in combat, Arlecchino gains a 40% Pyro DMG Bonus and can only be healed through Balemoon Rising."""}

arlecchinoConstellations = {'"All Reprisals and Arrears, Mine to Bear..."' : """Masque of the Red Death is further enhanced, the value of the increase is 100%. Additionally, Arlecchino's interruption resistance is increased when she performs Normal or Charged Attacks while affected by the Masque of the Red Death."""
                      
                      ,'"All Rewards and Retribution, Mine to Bestow..."'  : """Blood-Debt Directives are now already Blood-Debt Due when first applied.
When Arlecchino absorbs such a Due, she unleashes Balemoon Bloodfire in front of her, dealing 900% of her ATK as AoE Pyro DMG and increasing her All Elemental RES and Physical RES by 20% for 15s. This effect can trigger once every 10s.
You must first unlock the Ascension Talent"""+  '"Agony Alone May Be Repaid."'
                      
                      ,'"You Shall Become a New Member of Our Family..."'  : """Increases the Level of Normal Attack: Invitation to a Beheading by 3.
Maximum upgrade level is 15."""
                      
                      ,'"You Shall Love and Protect Each Other Henceforth..."'  : """When Arlecchino successfully absorbs a Blood-Debt Directive, Balemoon Rising's CD will decrease by 2s and 15 Elemental Energy will be restored to her. This effect can occur once every 10s."""
                            
                            ,'"For Alone, We Are as Good as Dead..."'  : """Increases the Level of Balemoon Rising by 3.
Maximum upgrade level is 15."""
                            
                            , '"From This Day On, We Shall Delight in New Life Together."' : """The DMG of Balemoon Rising is increased by Arlecchino's ATK multiplied by 700% of Arlecchino's current Bond of Life percentage.
For 20s after Arlecchino uses All Is Ash, both her Normal Attacks and Elemental Burst gain 10% increased CRIT Rate and 70% increased CRIT DMG. This effect can be triggered up to once every 15s."""}

#arlecchino file ended



'''ENDGOAL: I need to have a general dataclass that I could use for ANY genshin character
BASEGOAL: Fischl, Clorinde, Arlecchino, Kokomi represented with a singular dataclass'''



@dataclass
class Character:
    name : str
    rarity : int #either 4 or 5, represents 4 or 5 star
    baseStats: dict
    ascension: str #string that goes to dictionary of ascension names and stats given
    normals: dict #dictionary of normal scalings
    skill: dict #dictionary of skill scalings
    burst: dict #dictionary of burst scalings
    normalLevel : int #helps map which dictionary is used for normals
    skillLevel : int #helps map which diciontary is used for skill
    burstLevel : int #helps map which dictionary is used for burst
    level : int #int that helps map which dictionary is used for base stats
    levelCap : int #int that helps map which dictionary is used for base stats
    constellation : int #int that indexes which constellation the character's at
    consetllationEffect : dict #dictionary of what each constellation does
    passives: dict #dictionary of each character's passives
    weapon: str #string that represents the weapon of the character
    element: str #string that represents the element of the character

ascension = {"4 star": {"atk": "24.0%"
                  , "hp": "24.0%"
                  , "def": "30.0%"
                  , "hb": "18.5%"
                  , "pdb": "24.0%"
                  , 'hdb': '24.0%'
                  , 'edb': '24.0%'
                  , 'cdb': '24.0%'
                  , 'gdb': '24.0%'
                  , 'ddb': '24.0%'
                  , 'adb': '24.0%'
                  , 'pdb': '30.0%'
                  } #no 4 star has cr or cd ascension
             , "5 star": {"atk": "28.8%"
                          ,"hp": "28.8%"
                          ,"def": "36.0%"
                          ,"hb": "22.1%"
                          ,"pdb": "28.8%"
                          ,"hdb": "28.8%"
                          ,"edb": "28.8%"
                          ,"cdb": "28.8%"
                          ,"gdb": "28.8%" 
                          ,"ddb": "28.8%"
                          ,"adb": "28.8%"
                          ,"cd": "38.4%"
                          ,"cr": "19.2%" }} #no 5 star has pdb ascension

Fischl = Character("Fischl"
                   ,4 #rarity
                   , fischlBaseStats #base stats dictionary
                   , "atk" #fischl's ascension
                   , fischlNormals #fischl's normal attack scalings
                   , fischlSkill #fischl's skill damage scalings
                   , fischlBurst #fischl's burst damage scalings
                   , 10 #normal talent level
                   , 10 #skill talent level
                   , 10 #burst talent level
                   , 90 #level
                   , 90 #level cap
                   , 0 #constellation level
                   , fischlConstellations #fischl's constellations
                   , fischlPassives #fischl's passives
                   , "bow" #Fischl uses a bow
                   , "electro" #Fischl is an electro character
                   )

Clorinde = Character("Clorinde"
                     ,5 #Clorinde is a 5 star
                     ,clorindeBaseStats #Clorinde's base stats
                     ,"cr" #Clorinde ascends with crit rate
                     ,clorindeNormals #Clorinde's normal attack scalings
                     ,clorindeSkill #Clorinde's skills
                     ,clorindeBurst #Clorinde's burst
                     ,10 #Clorinde Normal Level
                     ,13 #Clorinde Skill Level
                     ,13 #Clorinde Burst Level
                     , 100 #level
                     , 100 #level cap
                     , 6 #constellation level
                     , clorindeConstellations
                     , clorindePassives
                     , "sword"
                     , "electro"
                     )

Arlecchino = Character("Arlecchino"
                       ,5
                       , arlecchinoBaseStats
                       , "cd"
                       , arlecchinoNormals
                       , arlecchinoSkill
                       , arlecchinoBurst
                       , 10
                       , 1
                       , 1
                       , 80
                       , 90
                       , 0
                       , arlecchinoConstellations
                       , arlecchinoPassives
                       , "polearm"
                       , "pyro"
                       )

Kokomi = Character("Sangonomiya Kokomi"
                   ,5
                   , kokomiBaseStats
                   , "hb"
                   , kokomiNormals
                   , kokomiSkill
                   , kokomiBurst
                   , 10
                   , 10
                   , 10
                   , 90
                   , 90
                   , 0
                   , kokomiConstellations
                   , kokomiPassives
                   , "catalyst"
                   , "hydro"
                   )


#nestedDict = {"lv1": {"1": 0, "2": 1, "3": 2}
#              , "lv2": {"4":3, "5":4, "6":5}}
#print(nestedDict["lv1"])
#print(nestedDict["lv1"]["2"])
#print(Fischl)
#print(Fischl.baseStats['atk']['lv90/90'])
#print(Fischl.ascension)
#print(Fischl.rarity)
#print(Fischl.normals['talent info'])
#print(Fischl.passives["Witch's Eve Right: Phantasmal Nocturne"])

characters = [Arlecchino, Clorinde, Fischl, Kokomi]
elements = ["pyro", "hydro", 'electro', 'cryo', 'geo', 'dendro', 'anemo']
weapons = ['sword', 'polearm', 'claymore', 'bow', 'catalyst']

def characterOverview(character: Character) -> str:
    '''will get given a character, in drafter this is from an input button, here this is a
    search input, but it will pring out general overview of the given character and return a
    string representing the 'page' '''
    print("Name: "+ character.name)
    print(str(character.rarity) + " star character")
    print("Element: " + character.element)
    print("Weapon: " + character.weapon)
    
    print('---')
    print("Base Stats")
    print("Talents")
    print("Passives")
    print("Constellations")
    print("Main Page")
    return input("Travel by typing name of page: ")

def mainPage(chars: list[Character]) -> str:
    '''this should be the main page that uses a list of Characters that will update
    overtime if filters are put in as it should be the 'base state, but it will return
    user input of what character they want specifically or element or weapon'''
    #if... [list of characters from filterCharacters() is empty, then display that filters will be
    #  reset after an empty input (an input that doesn't store to a variable)
    print('---'*7)
    
    if not chars:
        input("No characters are available with current filters")
        chars = characters
    
    for character in chars: #change characters to a return of filterCharacters()
        print(character.name)
    
    print("---"*3)
    print("Filter by searching up 'element:...' or 'weapon:...'")
    print("Have multiple filters by seperating your filters with spaces")
    print("---"*3)
    return input("Search: ")

#print("Apples".split(":"))
searchExample = "weapons: bow element: electro"
#print(searchExample)
searchExample = searchExample.replace(": ", ":")
#print(searchExample)
#removes spaces after colon, need to do this to every input
#print("---"*3)
searchExample2 = "weapons: bow       element:  electro"
#print(searchExample2)
searchExample2 = searchExample.replace(": ", ":")
#print(searchExample2)
#for terms in searchExample2.split(" "):
    #print(terms)
    #surprisingly outputs what I need it as
    #so this is also needed?
    
#print('---'*3)

searchExample3 = "weapons:  bow    ,    element:    electro  sangonomiya"

def cleanUpSearch (userInput: str):
    searchTermList = []
    
    if not userInput:
        #have something later check if the cleanUpSearch is falsity, then make user redo search
        return []
    
    userInput = userInput.replace(": ", ":")
    #print(userInput)
    userInput = userInput.replace(",", "")
    for term in userInput.split(' '):
        if term:
            #print(term)
            #print(term.find("s:"))
            wrongIndexPoint = term.find("s:")
            if wrongIndexPoint > -1:
                term = term[:wrongIndexPoint] + term[(wrongIndexPoint+1):]
                #print(term)
            searchTermList.append(term.lower())
    
    
    
    #draft here, turn into a helper function
    for character in characters:
        for term in character.name.split(" "):
            #print(term) #lets see what this prints out -> DOES PRINT OUT EVERY NAME AHAHAHAHA
            for searchTerm in searchTermList:
                if searchTerm.lower() == term.lower():
                    return [term]
    
    #cycle2 to create better output for searchExample3
    #print("---")
    searchTermListCycle2 = []
    for term in searchTermList:
        if len(term) == 1:
            for i in range(len(searchTermList)):
                
                if searchTermList[i][-1] == ":":
                    #print(searchTermList[i] + searchTermList[i+1])
                    searchTermListCycle2.append(searchTermList[i] + searchTermList[i+1])
                    #this creates an issue where search examples 1 and 2 become empty list returns
            
            return searchTermListCycle2
    
    return searchTermList

searchExample4 = 'weapon: bow element: electro sangonomiya fischl'

#print(cleanUpSearch(searchExample))
#print('-')
#print(cleanUpSearch(searchExample2))
#print('-')
#print(cleanUpSearch(searchExample3))
#print('-')
#print(cleanUpSearch(""))
##print('-')
#print(cleanUpSearch(searchExample4))
#print('-')

searchExample5 = "WEApons: bow eleMENT: electro"
#print(cleanUpSearch(searchExample5))
#search example 4 returns the last character's name in the search, which is odd but I'll take it

#cleanUpSearch is fully* working
#if theres a name of a character in the search, that should be prioritized
#ex: weapon: electro element: electro arlecchino -> goes to arlecchino
'''to fix this issue, I need to forloop through the terms before the second cycle to see if a
character's name is in it; if yes, then return a 1 length list of just that character's name'''

#print(mainPage())

#for character in characters:
#    for name in character.name.split(" "):
#        print(name)

#SO NOW CLEANUPSEARCH WORKS

#now what needs to happen is that the list returned from cleanUpSearch is checked if it's a name

def isName(searchTermList:list[str]) -> bool:
    '''takes the search term list returned from cleanUpSearch and returns True if it's a name of a
    character that's in the hard coded characters list
    
    parameter:
    searchTermList : list[str]
    
    return:
    isCharacter: bool'''
    
    #since a cleaned up search including a character's name should only be 1 element list
    #  it can be hardcoded as checking searchTermList[0] only
    
    isCharacter = False
    
    for character in characters:
        for name in character.name.split(" "):
            isCharacter = isCharacter or (searchTermList[0] == name)
    
    return isCharacter #redirect function will check if this function's return was True

#print('---'*7)

#print(isName(cleanUpSearch(searchExample))) #False
#print(isName(cleanUpSearch(searchExample2))) #False
#print(isName(cleanUpSearch(searchExample3))) #True
#print(isName(cleanUpSearch(searchExample4))) #True

def directSearch(searchTermList: list[str]) -> Character: #Character and not str because isName() return True is prereq for ts
    '''checks the result of isName() and if it is true, then it directly returns the dataclass
    of the searched character
    
    parameter:
    searchTermList: list[str] #although here it will always only have 1 term
    
    return:
    character: Character #will flow to the first page redirectory'''
    
    #I guess I'll match the search term to a name in the character list
    #print(searchTermList)
    #print(searchTermList[0])
    #print('-')
    for character in characters:
        #print(character.name)
        if searchTermList[0] in character.name.split(" "):
            return character

def getCharacterByName(fullName: str) -> Character:
    for character in characters:
        if character.name == fullName:
            return character

#since searchExample3 and searchExample4 returned True on isName(), I will test on those:

#print(directSearch(cleanUpSearch(searchExample3))) #correctly gave Sangonomiya Kokomi
#print(directSearch(cleanUpSearch(searchExample4))) #correctly gave Fischl
        
#userInput = mainPage()

#cleanInput = cleanUpSearch(userInput)
#print(cleanInput)
#print(isName(cleanInput))

#if isName(cleanInput):
#    character = directSearch(cleanInput)
#    characterOverview(character)

#that was a run of the direct search flow chart AND IT WORKS!!
    
cleanInput = (cleanUpSearch(searchExample2)) #correctly ['weapon:bow', 'element:electro']
#print(cleanInput)

#print(isName(cleanInput)) #correctly prints False

def filterCharacters(cleanInputs: list[str]) -> list[Character]:
    #check what the input is
    print(cleanInputs) #['weapon:bow', 'element:electro']
    filterTypes = []
    elementsWanted = []
    weaponsWanted = []
    returnFilteredCharacters = []
    
    for cleanInput in cleanInputs:
        filterTypes.append(cleanInput[:cleanInput.find(":")])
        if (cleanInput[cleanInput.find(":")+1:]) in elements:
            elementsWanted.append((cleanInput[cleanInput.find(":")+1:]))
        elif (cleanInput[cleanInput.find(":")+1:]) in weapons:
            weaponsWanted.append((cleanInput[cleanInput.find(":")+1:]))
            
    #check if theyre matching
    matchingType = True
    for i in range(len(filterTypes)):
        matchingType = matchingType and filterTypes[i] == filterTypes[i-1]
    
    #if only elements or only weapons act as or instead of and logic
    if matchingType: #or logic
        if filterTypes[0] == 'element':
            for character in characters:
                if character.element in elementsWanted:
                    returnFilteredCharacters.append(character)
        
        elif filterTypes[0] == 'weapon':
            for character in characters:
                if character.weapon in weaponsWanted:
                    returnFilteredCharacters.append(character)
    
    if not matchingType: #and logic
        for character in characters:
            if character.weapon in weaponsWanted and character.element in elementsWanted:
                returnFilteredCharacters.append(character)
    
    for filteredCharacter in returnFilteredCharacters:
        print(filteredCharacter.name)
    return returnFilteredCharacters
    
#chars =filterCharacters2(cleanUpSearch("weapon: bow, weapon: catalyst"))

#f#or char in chars:
   # print(char.name)

#print(chars)
    
#print(cleanUpSearch("weapon: bow, weapon: catalyst"))
#fuck it bro theres no point in spending like 4 hours on this singular issue anyways
#print(searchExample) #electro bow
#print(searchExample2) #electro bow
#print(searchExample3)
#print(searchExample4)
#print(searchExample5)




set_website_title("Genshin Database Prototype")
set_site_information(
    author="Rithwik Medisetti",
    description="Filter through a small (very small) selection of genshin characters!",
    sources="Thanks to the Drafter docs and my study group.",
    planning=["plan.pdf", "design.pdf"],
    links=["https://github.com/your-username/your-repository"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    query: str
    results: list[str]
    message: str

def getCharacterByName(fullName: str) -> Character:
    for character in characters:
        if character.name == fullName:
            return character

@route
def index(state: State) -> Page:
    return Page(state, [
        Header("Genshin Character Search"),

        Header("Available Characters"),
        BulletedList(state.results),

        "---",

        "Filter by searching up 'element:...' or 'weapon:...'",
        "Have multiple filters by separating your filters with spaces",

        "---",

        "Search:",
        TextBox("query", state.query),
        Button("Search", "search"),

        Header("Results"),
        state.message
    ])


@route
def search(state: State, query: str) -> Page:
    state.query = query
    cleanedInput = cleanUpSearch(query)

    if not cleanedInput:
        state.results = []
        state.message = "Please enter a search."

    elif isName(cleanedInput):
        character = directSearch(cleanedInput)
        state.currentCharacter = character.name
        return characterOverviewPage(state)

    else:
        filteredCharacters = filterCharacters2(cleanedInput)
        state.results = [character.name for character in filteredCharacters]

        if state.results:
            state.message = "Matching characters:"
        else:
            state.message = "No matching characters found."

    return index(state)

@route
def characterOverviewPage(state: State) -> Page:
    character = getCharacterByName(state.currentCharacter)
    return Page(state, [
        Header(character.name),
        str(character.rarity) + " star character",
        "Element: " + character.element,
        "Weapon: " + character.weapon,

        Button("View Base Stats", "baseStatsPage"),
        Button("View Talents", "talentsPage"),
        Button("Back to Search", "index")
    ])

@route
def baseStatsPage(state: State) -> Page:
    character = getCharacterByName(state.currentCharacter)
    stats = character.baseStats

    return Page(state, [
        Header(character.name + " - Base Stats"),

        Header("Level 80/90"),
        "HP: " + stats["hp"]["lv80/90"],
        "ATK: " + stats["atk"]["lv80/90"],
        "DEF: " + stats["def"]["lv80/90"],

        Header("Level 90/90"),
        "HP: " + stats["hp"]["lv90/90"],
        "ATK: " + stats["atk"]["lv90/90"],
        "DEF: " + stats["def"]["lv90/90"],
        
        Header("Level 100/100"),
        "HP: " + stats["hp"]["lv100/100"],
        "ATK: " + stats["atk"]["lv100/100"],
        "DEF: " + stats["def"]["lv100/100"],
        
        Button("View Talents", "talentsPage", Argument("characterName", character.name)),      
           Button("Back to Overview", "characterOverviewPage", Argument("characterName", character.name))
    ])

@route
def talentsPage(state: State) -> Page:
    character = getCharacterByName(state.currentCharacter)

    return Page(state, [
        Header(character.name + " - Talents"),

        Header("Normal Attack"),
        character.normals["talent info"],

        Header("Elemental Skill"),
        character.skill["talent info"],

        Header("Elemental Burst"),
        character.burst["talent info"],

        Button("Back to Overview", "characterOverviewPage"),
        Button("View Base Stats", "baseStatsPage")
    ])

#start_server(State("", [character.name for character in characters], "Enter a search!"))
start_server(State("" , [character.name for character in characters], "Enter a search!"))
