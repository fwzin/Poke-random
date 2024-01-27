import random

# Lista de todos os Pokémon disponíveis em Fire Red
pokemons_disponiveis = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise",  # Adicione todos os Pokémon disponíveis
                        # ... continuar com a lista de Pokémon
                        ]

# Função para criar um time aleatório
def criar_time(incluir_inicial=True):
    time = []

    # Adiciona o inicial se necessário
    if incluir_inicial:
        inicial = random.choice(["Bulbasaur", "Charmander", "Squirtle"])
        time.append(inicial)
        pokemons_disponiveis.remove(inicial)

    # Adiciona os outros Pokémon aleatórios
    for _ in range(6 - len(time)):
        pokemon_aleatorio = random.choice(pokemons_disponiveis)
        time.append(pokemon_aleatorio)
        pokemons_disponiveis.remove(pokemon_aleatorio)

    return time

# Exemplo de uso
incluir_inicial = input("Deseja incluir o inicial no time? (s/n): ").lower() == 's'
time_aleatorio = criar_time(incluir_inicial)
print("Seu time Pokémon aleatório é:")
print(time_aleatorio)
