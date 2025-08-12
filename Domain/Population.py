from collections import deque

from Domain.World import World
from Domain.LifeGiver import is_alive_in_next_generation

class Population:
    
    def __init__(self, initial_cell_values = None, previous_generation = None):
        if initial_cell_values:
            self.create_initial_generation(initial_cell_values)
        elif previous_generation:
            self.calculate_next_generation(previous_generation)
        
    def create_initial_generation(self, cell_values):
        self.census = 0
        self.cells = {}

        incoming_cell_values = deque(cell_values)

        for y in range(0, World.height):
            for x in range(0, World.width):
                incoming_cell = incoming_cell_values.popleft()
                self.cells[(x,y)] = incoming_cell
                if incoming_cell:
                    self.census += 1
                        
    def calculate_next_generation(self, previous_generation):
        self.census = 0
        self.cells = {}

        for y in range(0, World.height):
            for x in range(0, World.width):
                if is_alive_in_next_generation((x,y), previous_generation.cells):
                    self.cells[(x,y)] = 1
                    self.census += 1
                else:
                    self.cells[(x,y)] = 0

    def print_out(self):
        for y in range(0, World.height):
            for x in range(0, World.width):
                if self.cells[(x,y)]:
                    print("*", end = "")
                else:
                    print("-", end = "")
            print()
        print()
