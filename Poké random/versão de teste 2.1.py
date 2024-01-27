import random

# Dicionário com os Pokémon e suas respectivas rotas em Fire Red
pokemons_rotas_fire_red = {
    "Bulbasaur": "Um dos pokémons iniciais",
    "Venusaur": "Evolui do Ivysaur no level 32",
    "Charmander": "Um dos pokémons iniciais",
    "Charmeleon": "Evolui do Charmander no level 16",
    "Charizard": "Evolui do Charmeleon no level 36",
    "Squirtle": "Um dos pokémons iniciais",
    "Wartortle": "Evolui do Squirtle no level 16",
    "Blastoise": "Evolui do Wartortle no level 36",
    "Caterpie": "Encontrado em Route 2, Viridian Forest, ou Route 25",
    "Metapod": "Evolui de Caterpie no level 7 ou encontrado na Viridian Forest, Route 24, ou Route 25",
    "Butterfree": "Evolui de Metapod no level 10",
    "Weedle": "Encontrado na Viridian Forest, Route 2, Route 24, ou Route 25",
    "Kakuna": "Evolui de Weedle no level 7 ou encontrado na Viridian Forest, Route 24 ou Route 25.",
    "Beedrill": "Evolui de Kakuna no level 10",
    "Pidgey": "Encontrado em muitos lugares, mas tente em Route 2, 25, 24, 5, 7, 8, e 6",
    "Pidgeotto": "Evolui de Pidgey no level 18, ou encontrado em Routes 21, 15, and 14",
    "Pidgeot": "Evolui de Pidgeotto no level 36",
    "Rattata": "Encontrado em todo lugar, mas tente em Routes 1, 2, 15, 14 e 21",
    "Raticate": "Evolui de Rattata no level 20 ou encontre em Routes 21, 17, 16, 18",
    "Spearow": "Encontre em Routes 17, 18, 16, 3, 4, 9, e 22",
    "Fearow": "Evolui de Spearow no level 20 ou encontre em Route 23, 17, ou 18",
    "Ekans": "Route 23, 4, 9, 8, ou 11",
    "Arbok": "Route 23 ou Unknown Dungeon",
    "Pikachu": "Encontrado na Viridian Forest ou Power Plant",
    "Raichu": "Evolui de Pikachu com a Thunder Stone ou encontre na Power Plant, Unknown Dungeon, ou Route 23",
    #"Sandshrew": "Encontre em Route 23, 11, 8, 4, ou 9", #exclusivo em leaf green
    #"Sandslash": "Evolui de Sandshrew no level 22 ou encontre em Unknown Dungeon ou Route 23", #exclusivo em leaf green
    "Nidoran Female": "Encontre em Safari Zone ou Route 22",
    "Nidorina": "Encontre em Safari Zone, Route 8, ou no Game Corner",
    "Nidoqueen": "Evolui de Nidorina com a Moon Stone",
    "Nidoran Male": "Encontre em Safari Zone ou Route 22",
    "Nidorino": "Ganhe em Game Corner ou encontre em Safari Zone",
    "Nidoking": "Evolui de Nidorina com a Moon Stone",
    "Clefairy": "Ganhe em Game Corner, ou encontre em Mt. Moon",
    "Clefable": "Evolui de Clefairy com a Moon Stone",
    #"Vulpix": "Cinnabar Island, ou Routes 8 ou 7", #exclusivo em leaf green
    #"Ninetales": "Evolui de Vulpix com Fire Stone", #exclusivo em leaf green
    "Jigglypuff": "Encontre em Route 3",
    "Wigglytuff": "Encontre em Unknown Dungeon ou evolui de Jigglypuff com a Moon Stone",
    "Zubat": "Encontre em Mt. Moon, Rock Tunnel, ou Seafoam Islands",
    "Golbat": "Encontre em Seafoam Islands, Route 23, ou evolui de Zubat no level 22",
    "Oddish": "Routes 5, 7, 6, 24, 25, 12, 13, 14, ou 15",
    "Gloom": "Evolui de Oddish no level 21, ou Routes 12, 13, 14, ou 15",
    "Vileplume": "Evolui de Gloom com a Leaf Stone",
    "Paras": "Encontrado em Safari Zone ou Mt. Moon",
    "Parasect": "Evolui de Paras no level 24 ou encontre em Safari Zone ou Unknown Dungeon",
    "Venonat": "Encontre em Safari Zone ou Routes 12, 13, 14, ou 15",
    "Venomoth": "Evolui de Venonat no level 31 ou encontre em Unknown Dungeon, Victory Road, ou Safari Zone",
    "Diglett": "Encontre em Diglett's Cave",
    "Dugtrio": "Encontre em Digletts Cave ou evolui de Diglett no level 26",
    "Meowth": "Routes 5, 6, 7, ou 8",
    "Persian": "Evolui de Meowth no level 28",
    "Psyduck": "Pesque-o em Safari Zone ou Cerulean City ou encontre em Seafoam Islands, Route 4, 24, 29",
    "Golduck": "Evolui de Psyduck no level 33 ou encontre em Seafoam Islands",
    "Mankey": "Routes 5, 6, 7, ou 8",
    "Primeape": "Evolui de Mankey no level 28",
    "Growlithe": "Cinnabar Island, ou Routes 7, 8",
    "Arcanine": "Evolui de Growlithe com a Fire Stone",
    "Poliwag": "Pesque em Pallet Town, Viridian City, Route 22, ou Vermillion City",
    "Poliwhirl": "Evolui de Poliwag no level 25 ou pesque em Celadon City ou Route 9",
    "Poliwrath": "Evolui de Poliwhirl com a Water Stone",
    "Abra": "Ganhe no Game Corner ou encontre em Routes 24 and 25",
    "Kadabra": "Evolui de Abra no level 16 ou encontre em Unknown Dungeon",
    "Alakazam": "Este pokémon evolui de Kadabra só depois de passar pelo Game Link (trocando)",
    "Machop": "Encontre em Rock Tunnel ou Victory Road",
    "Machoke": "Evolui de Machop no level 28 ou encontre em Victory Road",
    "Machamp": "Este pokémon evolui de Machoke só depois de passar pelo Game Link (trocando)",
    #"Bellsprout": "Routes 6, 7, 12, 13, 14, 15, 24, ou 25", #exclusivo em leaf green
    #"Weepinbell": "Evolui de Bellsprout no level 21 ou encontre em Routes 12, 13, 14, ou 15", #exclusivo em leaf green
    #"Victreebel": "Evolui de Weepinbell com a Leaf Stone", #exclusivo em leaf green
    "Tentacool": "Encontre em Routes 12, 13, 17, 18, 19, 20, ou pesque em Pallet Town",
    "Tentacruel": "Evolui de Tentacool no level 30",
    "Geodude": "Encontre em Victory Road, Rock Tunnel, ou Mt. Moon",
    "Graveler": "Evolui de Geodude no level 25 ou encontre em Victory Road",
    "Golem": "Este pokémon evolui de Graveler só depois de passar pelo Game Link (trocando)",
    "Ponyta": "Encontre em Cinnabar Island",
    "Rapidash": "Evolui de Ponyta no level 40 ou encontre em Unknown Dungeon",
    #"Slowpoke": "Pesque em Celadon City, Safari Zone, Cinnabar Island, Route 9 ou 10, ou ache-o em Seafoam Islands", #exclusivo em leaf green
    #"Slowbro": "Evolui de Slowpoke no level 37 ou encontre em Route 23, Unknown Dungeon, ou Seafoam Island", #exclusivo em leaf green
    "Magnemite": "Encontre em Unknown Dungeon ou Power Plant",
    "Magneton": "Evolui de Magnemite no Level 30 ou encontre em Unknown Dungeon ou Power Plant",
    "Farfetch'd": "Troque na casa perto da Bike Voucher em Vermilion City",
    "Doduo": "Encontre em Routes 16, 17, 18 ou Safari Zone",
    "Dodrio": "Evolui de Doduo no level 31 ou encontre em Unknown Dungeon",
    "Seel": "Encontre em Seafoam Islands ou Cinnabar Island",
    "Dewgong": "Evolui de Seel no level 34 ou encontre em Seafoam Islands",
    "Grimer": "Encontre na Cinnabar's Mansion",
    "Muk": "Evolui de Grimer no level 38 ou encontre na Mansão Cinnabar, Unknown Dungeon",
    "Shellder": "Pesque em Vemilion City ou Routes 6, 19, 20, 21",
    "Cloyster": "Evolui de Shellder com Water Stone",
    "Gastly": "Encontre na torre de Lavender Town",
    "Haunter": "Evolui de Gastly no level 25 ou encontre na torre de Lavender Town",
    "Gengar": "Este pokémon evolui de Haunter só depois de passar pelo Game Link (trocando)",
    "Onix": "Encontre em Victory Road ou Rock Tunnel",
    "Drowzee": "Encontre em Route 11",
    "Hypno": "Evolui de Drowsee no level 26 ou encontre em Unknown Dungeon",
    "Krabby": "Pesque em vários lugares, especialmente em Routes 4, 11, 12, 13, 17, 18, ou 25",
    "Kingler": "Evolui de Krabby no level 28 ou encontre em Seafoam, pesque em Unknown Dungeon",
    "Voltorb": "Encontre em Power Plant ou Route 9",
    "Electrode": "Encontre na Mansão de Cinnabar, Power Plant, ou Unknown Dugeon",
    "Exeggcute": "Encontre em Safari Zone",
    "Exeggutor": "Evolui de Exeggcute com a Leaf Stone",
    "Cubone": "Enontre na torre de Lavender Town",
    "Marowak": "Evolui de Cubone no 28 ou encontre na Victory Road ou Unknown Dungeon",
    "Hitmonlee": "Uma de suas escolhas após derrotar a primeira GYM de Saffron City",
    "Hitmonchan": "Uma de suas escolhas após derrotar a primeira GYM de Saffron City",
    "Lickitung": "Troque na torre da Route 18",
    "Koffing": "Encontre na mansão de Cinnabar",
    "Weezing": "Evolui de Koffing no level 35 ou encontre na Mansão Cinnabar",
    "Rhyhorn": "Pegue no Safari Zone",
    "Rhydon": "Evolui de Rhyhorn no level 42 ou encontre em Unknown Dungeon",
    "Chansey": "Encontre em Safari Zone ou Unknown Dungeon",
    "Tangela": "Troque no laboratório de Cinnabar ou pegue na Route 21",
    "Kangaskhan": "Encontre em Safari Zone",
    "Horsea": "Pesque em Cinnabar Island, Routes 21, 19, 20, ou Celadon ou enconte em Seafoam",
    "Seadra": "Evolui de Horsea no level 32 ou encontre em Seafoam, pesque em Route 23 ou Unknown Dungeon",
    "Goldeen": "Encontre em Routes 24, 25, 4, 11, 12, 18, 19, 20, 21, ou 22",
    "Seaking": "Evolui de Goldeen no level 33 ou encontre em Unknown Dungeon ou Route 23",
    #"Staryu": "Pesque em Routes 19, 20, 21, Cinnabar Island ou encontre em Seafoam Islands", #exclusivo em leaf green
    #"Starmie": "Evolui de Staryu com a Water Stone", #exclusivo em leaf green
    "Mr. Mime": "Troque em uma casa em Route 2 após a Diglett's Cave",
    "Scyther": "Ganhe no Game Corner ou encontre em Safari Zone",
    "Jynx": "Troque ao norte de Cerulan City",
    "Electabuzz": "Pegue-o na Power Plant",
    #"Magmar": "Encontre em Cinnabar's Mansion", #exclusivo em leaf green
    "Pinsir": "Ganhe no Game Corner ou encontre em Safari Zone", #exclusivo em leaf green
    "Tauros": "Pegue em Safari Zone",
    "Magikarp": "Pesque em Routes 12, 13, 17, 18 ou Fushia City",
    "Gyarados": "Evolui de Magikarp no level 20",
    "Lapras": "Pegue no final do prédio Silph Co. em Saffron City",
    "Ditto": "Encontre em Unknown Dungeon ou Routes 13, 14, 15 e 23",
    "Eevee": "Encontre pelas portas do fundo da Mansão Celadon e suba as escadas",
    "Vaporeon": "Evolui de Eevee com uma Water Stone",
    "Jolteon": "Evolui de Eevee com uma Thunder Stone",
    "Flareon": "Evolui de Eevee com uma Fire Stone",
    "Porygon": "Ganhe no Game Corner",
    "Omanyte": "Escolha o Helix Fossil e leve ao laboratório de Cinnabar",
    "Omastar": "Evolui de Omanyte no level 40",
    "Kabuto": "Escolha o Dome Fossil e leve ao laboratório de Cinnabar",
    "Kabutops": "Evolui de Kabuto no level 40",
    "Aerodactyl": "Use HM01 (Cut) para entrar por de trás do Museum. Pegue o Old Amber e leve para o laboratório de Cinnabar",
    "Snorlax": "Acorde-o com a Poké-Flute em Route 16 ou 12",
    "Articuno": "Encontre-o no fim da caverna de Seafoam Islands",
    "Zapdos": "Encontre-o no fim da Power Plant",
    "Moltres": "Encontre-o no fim da Victory Road",
    "Dratini": "Ganhe no Game Corner ou pegue em Safari Zone",
    "Dragonair": "Evolui de Dratini no level 30",
    "Dragonite": "Evolui de Dragonair no level 55",
    "Mewtwo": "Encontre no final da caverna Unknown Dungeon, a noroeste de Cerulean City depois de vencer a Elite Four"
}

pokemons_rotas_leaf_green = {
    "Bulbasaur": "Um dos pokémons iniciais",
    "Venusaur": "Evolui do Ivysaur no level 32",
    "Charmander": "Um dos pokémons iniciais",
    "Charmeleon": "Evolui do Charmander no level 16",
    "Charizard": "Evolui do Charmeleon no level 36",
    "Squirtle": "Um dos pokémons iniciais",
    "Wartortle": "Evolui do Squirtle no level 16",
    "Blastoise": "Evolui do Wartortle no level 36",
    "Caterpie": "Encontrado em Route 2, Viridian Forest, ou Route 25",
    "Metapod": "Evolui de Caterpie no level 7 ou encontrado na Viridian Forest, Route 24, ou Route 25",
    "Butterfree": "Evolui de Metapod no level 10",
    "Weedle": "Encontrado na Viridian Forest, Route 2, Route 24, ou Route 25",
    "Kakuna": "Evolui de Weedle no level 7 ou encontrado na Viridian Forest, Route 24 ou Route 25.",
    "Beedrill": "Evolui de Kakuna no level 10",
    "Pidgey": "Encontrado em muitos lugares, mas tente em Route 2, 25, 24, 5, 7, 8, e 6",
    "Pidgeotto": "Evolui de Pidgey no level 18, ou encontrado em Routes 21, 15, and 14",
    "Pidgeot": "Evolui de Pidgeotto no level 36",
    "Rattata": "Encontrado em todo lugar, mas tente em Routes 1, 2, 15, 14 e 21",
    "Raticate": "Evolui de Rattata no level 20 ou encontre em Routes 21, 17, 16, 18",
    "Spearow": "Encontre em Routes 17, 18, 16, 3, 4, 9, e 22",
    "Fearow": "Evolui de Spearow no level 20 ou encontre em Route 23, 17, ou 18",
    #"Ekans": "Route 23, 4, 9, 8, ou 11", #exclusivo em fire red
    #"Arbok": "Route 23 ou Unknown Dungeon", #exclusivo em fire red
    "Pikachu": "Encontrado na Viridian Forest ou Power Plant",
    "Raichu": "Evolui de Pikachu com a Thunder Stone ou encontre na Power Plant, Unknown Dungeon, ou Route 23",
    "Sandshrew": "Encontre em Route 23, 11, 8, 4, ou 9", #exclusivo em leaf green
    "Sandslash": "Evolui de Sandshrew no level 22 ou encontre em Unknown Dungeon ou Route 23", #exclusivo em leaf green
    "Nidoran Female": "Encontre em Safari Zone ou Route 22",
    "Nidorina": "Encontre em Safari Zone, Route 8, ou no Game Corner",
    "Nidoqueen": "Evolui de Nidorina com a Moon Stone",
    "Nidoran Male": "Encontre em Safari Zone ou Route 22",
    "Nidorino": "Ganhe em Game Corner ou encontre em Safari Zone",
    "Nidoking": "Evolui de Nidorina com a Moon Stone",
    "Clefairy": "Ganhe em Game Corner, ou encontre em Mt. Moon",
    "Clefable": "Evolui de Clefairy com a Moon Stone",
    "Vulpix": "Cinnabar Island, ou Routes 8 ou 7", #exclusivo em leaf green
    "Ninetales": "Evolui de Vulpix com Fire Stone", #exclusivo em leaf green
    "Jigglypuff": "Encontre em Route 3",
    "Wigglytuff": "Encontre em Unknown Dungeon ou evolui de Jigglypuff com a Moon Stone",
    "Zubat": "Encontre em Mt. Moon, Rock Tunnel, ou Seafoam Islands",
    "Golbat": "Encontre em Seafoam Islands, Route 23, ou evolui de Zubat no level 22",
    #"Oddish": "Routes 5, 7, 6, 24, 25, 12, 13, 14, ou 15", #exclusivo em fire red
    #"Gloom": "Evolui de Oddish no level 21, ou Routes 12, 13, 14, ou 15", #exclusivo em fire red
    #"Vileplume": "Evolui de Gloom com a Leaf Stone", #exclusivo em fire red
    "Paras": "Encontrado em Safari Zone ou Mt. Moon",
    "Parasect": "Evolui de Paras no level 24 ou encontre em Safari Zone ou Unknown Dungeon",
    "Venonat": "Encontre em Safari Zone ou Routes 12, 13, 14, ou 15",
    "Venomoth": "Evolui de Venonat no level 31 ou encontre em Unknown Dungeon, Victory Road, ou Safari Zone",
    "Diglett": "Encontre em Diglett's Cave",
    "Dugtrio": "Encontre em Digletts Cave ou evolui de Diglett no level 26",
    "Meowth": "Routes 5, 6, 7, ou 8",
    "Persian": "Evolui de Meowth no level 28",
    #"Psyduck": "Pesque-o em Safari Zone ou Cerulean City ou encontre em Seafoam Islands, Route 4, 24, 29", #exclusivo em fire red
    #"Golduck": "Evolui de Psyduck no level 33 ou encontre em Seafoam Islands", #exclusivo em fire red
    "Mankey": "Routes 5, 6, 7, ou 8",
    "Primeape": "Evolui de Mankey no level 28",
    #"Growlithe": "Cinnabar Island, ou Routes 7, 8", #exclusivo em fire red
    #"Arcanine": "Evolui de Growlithe com a Fire Stone", #exclusivo em fire red
    "Poliwag": "Pesque em Pallet Town, Viridian City, Route 22, ou Vermillion City",
    "Poliwhirl": "Evolui de Poliwag no level 25 ou pesque em Celadon City ou Route 9",
    "Poliwrath": "Evolui de Poliwhirl com a Water Stone",
    "Abra": "Ganhe no Game Corner ou encontre em Routes 24 and 25",
    "Kadabra": "Evolui de Abra no level 16 ou encontre em Unknown Dungeon",
    "Alakazam": "Este pokémon evolui de Kadabra só depois de passar pelo Game Link (trocando)",
    "Machop": "Encontre em Rock Tunnel ou Victory Road",
    "Machoke": "Evolui de Machop no level 28 ou encontre em Victory Road",
    "Machamp": "Este pokémon evolui de Machoke só depois de passar pelo Game Link (trocando)",
    "Bellsprout": "Routes 6, 7, 12, 13, 14, 15, 24, ou 25", #exclusivo em leaf green
    "Weepinbell": "Evolui de Bellsprout no level 21 ou encontre em Routes 12, 13, 14, ou 15", #exclusivo em leaf green
    "Victreebel": "Evolui de Weepinbell com a Leaf Stone", #exclusivo em leaf green
    "Tentacool": "Encontre em Routes 12, 13, 17, 18, 19, 20, ou pesque em Pallet Town",
    "Tentacruel": "Evolui de Tentacool no level 30",
    "Geodude": "Encontre em Victory Road, Rock Tunnel, ou Mt. Moon",
    "Graveler": "Evolui de Geodude no level 25 ou encontre em Victory Road",
    "Golem": "Este pokémon evolui de Graveler só depois de passar pelo Game Link (trocando)",
    "Ponyta": "Encontre em Cinnabar Island",
    "Rapidash": "Evolui de Ponyta no level 40 ou encontre em Unknown Dungeon",
    "Slowpoke": "Pesque em Celadon City, Safari Zone, Cinnabar Island, Route 9 ou 10, ou ache-o em Seafoam Islands", #exclusivo em leaf green
    "Slowbro": "Evolui de Slowpoke no level 37 ou encontre em Route 23, Unknown Dungeon, ou Seafoam Island", #exclusivo em leaf green
    "Magnemite": "Encontre em Unknown Dungeon ou Power Plant",
    "Magneton": "Evolui de Magnemite no Level 30 ou encontre em Unknown Dungeon ou Power Plant",
    "Farfetch'd": "Troque na casa perto da Bike Voucher em Vermilion City",
    "Doduo": "Encontre em Routes 16, 17, 18 ou Safari Zone",
    "Dodrio": "Evolui de Doduo no level 31 ou encontre em Unknown Dungeon",
    "Seel": "Encontre em Seafoam Islands ou Cinnabar Island",
    "Dewgong": "Evolui de Seel no level 34 ou encontre em Seafoam Islands",
    "Grimer": "Encontre na Cinnabar's Mansion",
    "Muk": "Evolui de Grimer no level 38 ou encontre na Mansão Cinnabar, Unknown Dungeon",
    #"Shellder": "Pesque em Vemilion City ou Routes 6, 19, 20, 21", #exclusivo em fire red
    #"Cloyster": "Evolui de Shellder com Water Stone", #exclusivo em fire red
    "Gastly": "Encontre na torre de Lavender Town",
    "Haunter": "Evolui de Gastly no level 25 ou encontre na torre de Lavender Town",
    "Gengar": "Este pokémon evolui de Haunter só depois de passar pelo Game Link (trocando)",
    "Onix": "Encontre em Victory Road ou Rock Tunnel",
    "Drowzee": "Encontre em Route 11",
    "Hypno": "Evolui de Drowsee no level 26 ou encontre em Unknown Dungeon",
    "Krabby": "Pesque em vários lugares, especialmente em Routes 4, 11, 12, 13, 17, 18, ou 25",
    "Kingler": "Evolui de Krabby no level 28 ou encontre em Seafoam, pesque em Unknown Dungeon",
    "Voltorb": "Encontre em Power Plant ou Route 9",
    "Electrode": "Encontre na Mansão de Cinnabar, Power Plant, ou Unknown Dugeon",
    "Exeggcute": "Encontre em Safari Zone",
    "Exeggutor": "Evolui de Exeggcute com a Leaf Stone",
    "Cubone": "Enontre na torre de Lavender Town",
    "Marowak": "Evolui de Cubone no 28 ou encontre na Victory Road ou Unknown Dungeon",
    "Hitmonlee": "Uma de suas escolhas após derrotar a primeira GYM de Saffron City",
    "Hitmonchan": "Uma de suas escolhas após derrotar a primeira GYM de Saffron City",
    "Lickitung": "Troque na torre da Route 18",
    "Koffing": "Encontre na mansão de Cinnabar",
    "Weezing": "Evolui de Koffing no level 35 ou encontre na Mansão Cinnabar",
    "Rhyhorn": "Pegue no Safari Zone",
    "Rhydon": "Evolui de Rhyhorn no level 42 ou encontre em Unknown Dungeon",
    "Chansey": "Encontre em Safari Zone ou Unknown Dungeon",
    "Tangela": "Troque no laboratório de Cinnabar ou pegue na Route 21",
    "Kangaskhan": "Encontre em Safari Zone",
    "Horsea": "Pesque em Cinnabar Island, Routes 21, 19, 20, ou Celadon ou enconte em Seafoam",
    "Seadra": "Evolui de Horsea no level 32 ou encontre em Seafoam, pesque em Route 23 ou Unknown Dungeon",
    "Goldeen": "Encontre em Routes 24, 25, 4, 11, 12, 18, 19, 20, 21, ou 22",
    "Seaking": "Evolui de Goldeen no level 33 ou encontre em Unknown Dungeon ou Route 23",
    "Staryu": "Pesque em Routes 19, 20, 21, Cinnabar Island ou encontre em Seafoam Islands", #exclusivo em leaf green
    "Starmie": "Evolui de Staryu com a Water Stone", #exclusivo em leaf green
    "Mr. Mime": "Troque em uma casa em Route 2 após a Diglett's Cave",
    #"Scyther": "Ganhe no Game Corner ou encontre em Safari Zone", #exclusivo em fire red
    "Jynx": "Troque ao norte de Cerulan City",
    #"Electabuzz": "Pegue-o na Power Plant", #exclusivo em fire red
    "Magmar": "Encontre em Cinnabar's Mansion", #exclusivo em leaf green
    "Pinsir": "Ganhe no Game Corner ou encontre em Safari Zone", #exclusivo em leaf green
    "Tauros": "Pegue em Safari Zone",
    "Magikarp": "Pesque em Routes 12, 13, 17, 18 ou Fushia City",
    "Gyarados": "Evolui de Magikarp no level 20",
    "Lapras": "Pegue no final do prédio Silph Co. em Saffron City",
    "Ditto": "Encontre em Unknown Dungeon ou Routes 13, 14, 15 e 23",
    "Eevee": "Encontre pelas portas do fundo da Mansão Celadon e suba as escadas",
    "Vaporeon": "Evolui de Eevee com uma Water Stone",
    "Jolteon": "Evolui de Eevee com uma Thunder Stone",
    "Flareon": "Evolui de Eevee com uma Fire Stone",
    "Porygon": "Ganhe no Game Corner",
    "Omanyte": "Escolha o Helix Fossil e leve ao laboratório de Cinnabar",
    "Omastar": "Evolui de Omanyte no level 40",
    "Kabuto": "Escolha o Dome Fossil e leve ao laboratório de Cinnabar",
    "Kabutops": "Evolui de Kabuto no level 40",
    "Aerodactyl": "Use HM01 (Cut) para entrar por de trás do Museum. Pegue o Old Amber e leve para o laboratório de Cinnabar",
    "Snorlax": "Acorde-o com a Poké-Flute em Route 16 ou 12",
    "Articuno": "Encontre-o no fim da caverna de Seafoam Islands",
    "Zapdos": "Encontre-o no fim da Power Plant",
    "Moltres": "Encontre-o no fim da Victory Road",
    "Dratini": "Ganhe no Game Corner ou pegue em Safari Zone",
    "Dragonair": "Evolui de Dratini no level 30",
    "Dragonite": "Evolui de Dragonair no level 55",
    "Mewtwo": "Encontre no final da caverna Unknown Dungeon, a noroeste de Cerulean City depois de vencer a Elite Four"
}

# Função para criar um time aleatório
def criar_time(incluir_inicial, rotas):
    time = []

    # Adiciona o inicial se necessário
    if incluir_inicial:
        inicial = random.choice(["Bulbasaur", "Charmander", "Squirtle"])
        time.append(inicial)

    # Adiciona os outros Pokémon aleatórios
    for _ in range(6 - len(time)):
        pokemon_aleatorio = random.choice(list(rotas.keys()))
        time.append(pokemon_aleatorio)

    return time

# Função para escolher a versão e criar o time aleatório
def escolher_versao():
    print("Escolha a versão:")
    print("1. Fire Red")
    print("2. Leaf Green")

    escolha = input("Digite o número da versão desejada (1 para Fire Red, 2 para Leaf Green): ")

    if escolha == "1":
        incluir_inicial = input("Deseja incluir o inicial no time? (s/n): ").lower() == 's'
        time_aleatorio = criar_time(incluir_inicial, pokemons_rotas_fire_red)
    elif escolha == "2":
        incluir_inicial = input("Deseja incluir o inicial no time? (s/n): ").lower() == 's'
        time_aleatorio = criar_time(incluir_inicial, pokemons_rotas_leaf_green)
    else:
        print("Escolha inválida. Tente novamente.")
        return escolher_versao()

    print("Seu time Pokémon aleatório é:")
    for pokemon in time_aleatorio:
        if escolha == "1":
            print(f"{pokemon} - Encontrado em: {pokemons_rotas_fire_red.get(pokemon, 'Desconhecido')}")
        elif escolha == "2":
            print(f"{pokemon} - Encontrado em: {pokemons_rotas_leaf_green.get(pokemon, 'Desconhecido')}")

# Chama a função para escolher a versão e criar o time aleatório
escolher_versao()