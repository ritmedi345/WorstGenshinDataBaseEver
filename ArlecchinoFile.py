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

