import pandas

print("csv")
mijndata = pandas.read_csv("Pokemon.csv")

print(mijndata)
'''for mijnpokemons in mijndata["Name"]:
      print(mijnpokemons)'''




#favoriete pokemon zoeken#
#hoeveel en welke pokemons zijn sterker dan 80
#welke type 1 gemiddelde de meeste defence.
#onderzoeks vraag.


def favorietepokemon(mijndata):
    mijnpokemon = input("Wat is je favoriete Pokemon? ")
    pokemon_info = mijndata[mijndata["Name"] == mijnpokemon]

    if not pokemon_info.empty:
        pokemon_attack = pokemon_info.iloc[0]["Attack"]
        higher_attack_pokemon = mijndata[mijndata["Attack"] > pokemon_attack]
        print(f"Pokemon gevonden!")
        print("Pokemon:", mijnpokemon)
        print("Attack:", pokemon_attack)


        if not higher_attack_pokemon.empty:
            print("Pokemons with higher Attack:")
            print(higher_attack_pokemon[["Name", "Attack"]])
        else:
            print("No other Pokémon have a higher Attack value.")
    else:
        print("Pokemon not found or you have a typo!")

favorietepokemon(mijndata)