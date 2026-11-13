from drafter import *
from dataclasses import dataclass
from pythonGenshinCharacters import *
from mainGenshinCharactersNonDrafter import *

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

start_server(State("", [character.name for character in characters], "Enter a search!"))
