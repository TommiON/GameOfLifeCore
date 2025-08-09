from Domain.World import World
from Engine.Setupper import read_setup_from_json

def main():
    print("-- Game of Life --")
    setup()
    run()

def setup():
    world_config = read_setup_from_json()
    World.set_width(world_config["worldWidth"])
    World.set_height(world_config["worldHeight"])

def run():
    print("Maailman mitat!!!", World.width, 'X', World.height)

if __name__ == "__main__":
    main()

