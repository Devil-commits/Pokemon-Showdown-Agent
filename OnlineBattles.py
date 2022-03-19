# -*- coding: utf-8 -*-

import asyncio
import sys

from poke_env.player.random_player import RandomPlayer
from poke_env.player_configuration import PlayerConfiguration
from poke_env.server_configuration import ShowdownServerConfiguration

sys.path.append("./showdown_agent")

#from MaxDamagePlayer import MaxDamagePlayer
from SmartDamagePlayer import SmartDamagePlayer
from MiniMax import MinimaxPlayer
from poke_env.player.baselines import SimpleHeuristicsPlayer

async def main(): 
    team = """
Pelipper @ Damp Rock  
Ability: Drizzle  
EVs: 248 HP / 8 Def / 252 SpD  
Calm Nature  
IVs: 0 Spe  
- Scald  
- Defog  
- U-turn  
- Roost  

Barraskewda @ Choice Band  
Ability: Swift Swim  
EVs: 252 Atk / 4 SpD / 252 Spe  
Adamant Nature  
- Flip Turn  
- Liquidation  
- Crunch  
- Close Combat  

Porygon-Z @ Choice Specs  
Ability: Download  
EVs: 252 SpA / 4 SpD / 252 Spe  
Modest Nature  
IVs: 0 Atk  
- Shadow Ball  
- Ice Beam  
- Tri Attack  
- Psyshock  

Ferrothorn @ Rocky Helmet  
Ability: Iron Barbs  
EVs: 248 HP / 252 Def / 8 Spe  
Impish Nature  
- Stealth Rock  
- Body Press  
- Knock Off  
- Leech Seed  

Tapu Lele @ Choice Scarf  
Ability: Psychic Surge  
EVs: 252 SpA / 4 SpD / 252 Spe  
Modest Nature  
IVs: 0 Atk  
- Future Sight  
- Moonblast  
- Thunder  
- Psyshock  

Seismitoad @ Choice Specs  
Ability: Swift Swim  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
IVs: 0 Atk  
- Grass Knot  
- Earth Power  
- Icy Wind  
- Surf  
"""
    
    #print("Random Player:")

    # Create a player with the online server configuration
    #player = RandomPlayer(
    #        player_configuration=PlayerConfiguration("RemptonGames", "Cwalrus96!"),
    #        server_configuration=ShowdownServerConfiguration
    #)

    # Play a game on the ladder
    #await player.ladder(1)

    #print("Max Damage Player")

    #player = MaxDamagePlayer(
    #        player_configuration=PlayerConfiguration("RemptonGames", "Cwalrus96!"),
    #        server_configuration=ShowdownServerConfiguration
    #)

    # Play a game on the ladder
    #await player.ladder(1)

    #print("Smart Damage Player")

    #player = SmartDamagePlayer(
    #        player_configuration=PlayerConfiguration("RemptonGames", "Cwalrus96!"),
    #       server_configuration=ShowdownServerConfiguration
    #)

    # Play a game on the ladder
    #await player.ladder(1)

#     print("Minimax Player")

#     player = MinimaxPlayer(
#            battle_format="gen8ou", team=team, max_concurrent_battles=1,            
#            player_configuration=PlayerConfiguration("LeadNitrate", "anchit@123"),
#            server_configuration=ShowdownServerConfiguration
#     )

#     #Play a game on the ladder
#     await player.ladder(1)

     print("Simple Heuristic Player")

     player = SimpleHeuristicsPlayer(
           battle_format="gen8ou", team=team, max_concurrent_battles=1,            
           player_configuration=PlayerConfiguration("LeadNitrate", "anchit@123"),
           server_configuration=ShowdownServerConfiguration
    )

    #Play a game on the ladder
    await player.ladder(1)


if __name__ == "__main__": 
    asyncio.get_event_loop().run_until_complete(main())
