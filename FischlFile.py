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