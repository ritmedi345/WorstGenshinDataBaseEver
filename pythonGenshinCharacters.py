from dataclasses import dataclass
from FischlFile import *
from ClorindeFile import *
from ArlecchinoFile import *
from KokomiFile import *


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

