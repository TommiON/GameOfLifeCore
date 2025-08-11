from Domain.World import World
from Domain.Population import Population
from Engine.Setupper import read_setup_from_json

generations = []

def main():
    print("-- Game of Life --")
    setup()
    run()

def setup():
    world_config = read_setup_from_json()

    World.set_width(world_config["worldWidth"])
    World.set_height(world_config["worldHeight"])

    generation_one = Population(initial_cell_values = world_config["initialCells"])
    generations.append(generation_one)

    generation_one.print_out()

def run():
    generation_two = Population(previous_generation = generations[0])

    generation_two.print_out()

if __name__ == "__main__":
    main()

