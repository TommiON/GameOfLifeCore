from Domain.World import World
from Domain.Population import Population
from Engine.Setupper import read_setup_from_json

from time import sleep
from sys import argv

def main():
    if len(argv) > 1:
        run_in_local_mode(config_file_name = argv[1])
    else:
        run_in_REST_mode()

def run_in_local_mode(config_file_name):
    try:
        world_config = read_setup_from_json(filename = config_file_name)
    except ValueError as error:
        print("VIRHE:", error)
    except FileNotFoundError as error:
        print("VIRHE: konfiguraatiotiedostoa ei löydy")

    
    World.set_width(world_config["worldWidth"])
    World.set_height(world_config["worldHeight"])

    current_generation = Population(initial_cell_values = world_config["initialCells"])
    generation_ordinal = 1

    while True:        
        if current_generation.census == 0:
            print("SUKUPUUTTO!")
            current_generation.print_out()
            break
        else:
            print("Sukupolvi:", generation_ordinal, "Väkiluku:", current_generation.census)
            current_generation.print_out()
        
        sleep(0.5)

        next_generation = Population(previous_generation = current_generation)
        current_generation = next_generation
        generation_ordinal += 1

def run_in_REST_mode():
    pass    

if __name__ == "__main__":
    main()

