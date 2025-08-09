from collections import deque

from Domain.World import World

class Population:
    def __init__(self, initial_cell_values = None, previous_generation = None):
        if initial_cell_values:
            self.cells = self.create_initial_generation(initial_cell_values)
        elif previous_generation:
            self.cells = self.calculate_next_generation(previous_generation)
        
    def create_initial_generation(self, cell_values):
        self.validate_cell_input(cell_values)
        
        incomingCellValues = deque(cell_values)
        arranged_cell_values = {}

        for y in range(0, World.height):
            for x in range(0, World.width):
                arranged_cell_values[(x,y)] = incomingCellValues.popleft()
        
        return arranged_cell_values
                
    def calculate_next_generation(self, previousGeneration):
        print("Lasketaan seuraavan sukupolven elinmahdollisuudet")

    def print_out(self):
        for y in range(0, World.height):
            for x in range(0, World.width):
                print(self.cells[(x,y)], end = " ")
            print()

    def validate_cell_input(self, cellValues):
        if len(cellValues) > (World.width * World.height):
            raise ValueError("Syötteessä liikaa arvoja")
        elif len(cellValues) < (World.width * World.height):
            raise ValueError("Syötteessä liian vähän arvoja")
        else:
            for value in cellValues:
                if value not in [0, 1, "0", "1", True, False]:
                    raise ValueError("Syötteessä saa olla vain totuusarvoja")
