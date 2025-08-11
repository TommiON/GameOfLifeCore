from Domain.World import World
from Domain.Neighborhood import Neighborhood

def is_alive_in_next_generation(cell_coordinates, all_cells_of_previous_generation):
    x = cell_coordinates[0]
    y = cell_coordinates[1]

    current_cell = all_cells_of_previous_generation[(x,y)]

    neighborhood = Neighborhood(x,y)
    living_neighbors = 0

    for cell in neighborhood.neighbors:
        x_neighbor = cell[0]
        y_neighbor = cell[1]
        neighbor_cell = all_cells_of_previous_generation[(x_neighbor, y_neighbor)]
        if neighbor_cell:
            living_neighbors += 1

    if current_cell and living_neighbors in {2, 3}:
        # on tällä hetkellä elossa ja pysyy elossa
        return True
    elif not current_cell and living_neighbors == 3:
        # on tällä hetkellä kuollut mutta herää eloon
        return True
    else:
        # kuolee tai pysyy kuolleena
        return False
