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