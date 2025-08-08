from Domain.Population import Population
from Domain.World import World

World.set_width(4)
World.set_height(3)

test_cells = [1,0,1,0,0,1,1,1,0,0,0,1]

population = Population(initial_cell_values=test_cells)
population.print_out()

population2 = Population(previous_generation='jaa')

