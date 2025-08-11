from collections import deque

from Domain.World import World
from Domain.LifeGiver import is_alive_in_next_generation

class Population:
    
    def __init__(self, initial_cell_values = None, previous_generation = None):
        if initial_cell_values:
            self.cells = self.create_initial_generation(initial_cell_values)
        elif previous_generation:
            self.cells = self.calculate_next_generation(previous_generation)
        
    def create_initial_generation(self, cell_values):
        incoming_cell_values = deque(cell_values)
        arranged_cell_values = {}

        for y in range(0, World.height):
            for x in range(0, World.width):
                arranged_cell_values[(x,y)] = incoming_cell_values.popleft()
        
        return arranged_cell_values
                
    def calculate_next_generation(self, previous_generation):
        next_generation_cell_values = {}

        for y in range(0, World.height):
            for x in range(0, World.width):
                if is_alive_in_next_generation((x,y), previous_generation.cells):
                    next_generation_cell_values[(x,y)] = 1
                else:
                    next_generation_cell_values[(x,y)] = 0

        return next_generation_cell_values

    def print_out(self):
        for y in range(0, World.height):
            for x in range(0, World.width):
                if self.cells[(x,y)]:
                    print("*", end = "")
                else:
                    print("-", end = "")
            print()
        print()
