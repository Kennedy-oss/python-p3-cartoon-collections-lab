def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(words):
    return any(len(word) > 4 for word in words)

def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheeses:
            return item
    return None

# Example usage
dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarves)

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
print(summon_captain_planet(planeteer_calls))

short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))

assorted_words = ["two", "go", "industrious", "bop"]
print(long_planeteer_calls(assorted_words))

snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks))

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup))

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients))

