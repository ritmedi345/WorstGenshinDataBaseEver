from pythonGenshinCharacters import *

def main(running: bool) -> bool:
    while running:
        userInput = mainPage(characters)
                
        if userInput == 'QUIT'.lower().strip():
            return False
            
        cleanPut = cleanUpSearch(userInput)
        
        if isName(cleanPut):
            currentCharacter = directSearch(cleanPut)
            
            currentCharacter.normalLevel = 1
            currentCharacter.skillLevel = 1
            currentCharacter.burstLevel = 1
            currentCharacter.level = 80
            currentCharacter.constellation = 0
            
            overviewInput = characterOverview(currentCharacter)
            
            while overviewInput.lower().strip() not in ['basestats'
                                                        , 'talents'
                                                        , 'passives'
                                                        , 'constellations'
                                                        , 'quit'
                                                        , 'basestat'
                                                        , 'talent'
                                                        , 'passive'
                                                        , 'constellation']:
                
                overviewInput = characterOverview(directSearch(cleanPut))
            
            if overviewInput.lower().strip() == 'quit':
                return False
            
            elif overviewInput.strip().lower() == 'talents' or overviewInput.strip().lower() == 'talent':
                #print talents
                currentCharacter.normalLevel = 1
                currentCharacter.skillLevel = 1
                currentCharacter.burstLevel = 1
                
                print(currentCharacter.name + "'s talents \n")
                
                #I really like switch statements in java and C# and I think this would be a good time to use them
                #  the closest thing python has to switch statements is case matching, so I will use that instead
                
                match currentCharacter:
                    case Clorinde:
                        #use more case matching for level
                        print(Clorinde.normals['lv' + str(Clorinde.normalLevel)])
                        print(Clorinde.skill['lv' + str(Clorinde.skillLevel)])
                        print(Clorinde.burst['lv' + str(Clorinde.burstLevel)])
                              
        
        if not isName(cleanPut):
            mainPage(filterCharacters(cleanPut))


main(True)