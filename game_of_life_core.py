from Domain.World import World
from Domain.Population import Population
from Engine.Setupper import read_setup_from_json

from time import sleep

def main():
    start()

def start():
    try:
        world_config = read_setup_from_json()
    except ValueError as error:
        print("VIRHE!", error)

    World.set_width(world_config["worldWidth"])
    World.set_height(world_config["worldHeight"])
    generation_one = Population(initial_cell_values = world_config["initialCells"])

    run(generation_one)

def run(initial_generation):
    current_generation = initial_generation
    number_of_current_generation = 1

    while True:        
        if current_generation.census == 0:
            print("SUKUPUUTTO!")
            current_generation.print_out()
            break
        else:
            print("Sukupolvi:", number_of_current_generation, "Väkiluku:", current_generation.census)
            current_generation.print_out()
        
        sleep(0.5)

        next_generation = Population(previous_generation = current_generation)
        current_generation = next_generation
        number_of_current_generation += 1

if __name__ == "__main__":
    main()

