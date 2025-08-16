from Domain.Population import Population
from Domain.World import World
from Engine.Setupper import setup_world

from time import sleep
from sys import exit

def run_in_local_mode(config_file_name):
    try:
        setup_world(config_file_name = config_file_name)
    except ValueError as error:
        print("VIRHE:", error)
        exit(1)
    except FileNotFoundError as error:
        print("VIRHE: konfiguraatiotiedostoa ei löydy")
        exit(1)

    print_welcome()

    current_generation = Population(initial_cell_values = World.generation_one)

    while True:        
        if current_generation.census == 0:
            print("SUKUPUUTTO!")
            current_generation.print_out()
            break
        else:
            print("Sukupolvi:", current_generation.generation, "Väkiluku:", current_generation.census)
            current_generation.print_out()
        
        sleep(0.5)

        next_generation = Population(previous_generation = current_generation)
        current_generation = next_generation

def print_welcome():
    if World.toroidal_in_X_dimension:
        endless_X_string = "(päättymätön)"
    else:
        endless_X_string = ""
    
    if World.toroidal_in_Y_dimension:
        print("???", World.toroidal_in_Y_dimension)
        endless_Y_string = "(päättymätön)"
    else:
        endless_Y_string = ""

    print("Maailman leveys", World.width, endless_X_string, "ja korkeus", World.height, endless_Y_string)