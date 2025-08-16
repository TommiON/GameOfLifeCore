from Domain.World import World

class Neighborhood:

    def __init__(self, x, y):
        if x == 0:
            if World.toroidal_in_X_dimension:
                left_neighbor_column = World.width - 1
            else:
                left_neighbor_column = None
        else:
            left_neighbor_column = x - 1
        
        if x == World.width - 1:
            if World.toroidal_in_X_dimension:
                right_neighbor_column = 0
            else:
                right_neighbor_column = None
        else:
            right_neighbor_column = x + 1

        if y == 0:
            if World.toroidal_in_Y_dimension:
                upper_neighbor_row = World.height - 1
            else:
                upper_neighbor_row = None
        else:
            upper_neighbor_row = y - 1

        if y == World.height - 1:
            if World.toroidal_in_Y_dimension:
                lower_neighbor_row = 0
            else:
                lower_neighbor_row = None
        else:
            lower_neighbor_row = y + 1

        self.neighbors = []

        if left_neighbor_column is not None:
            self.neighbors.append((left_neighbor_column, y))
            if upper_neighbor_row is not None:
                self.neighbors.append((left_neighbor_column, upper_neighbor_row))
            if lower_neighbor_row is not None:
                self.neighbors.append((left_neighbor_column, lower_neighbor_row))
        
        if upper_neighbor_row is not None:
            self.neighbors.append((x, upper_neighbor_row))
        
        if lower_neighbor_row is not None:
            self.neighbors.append((x, lower_neighbor_row))

        if right_neighbor_column is not None:
            self.neighbors.append((right_neighbor_column, y))
            if upper_neighbor_row is not None:
                self.neighbors.append((right_neighbor_column, upper_neighbor_row))
            if lower_neighbor_row is not None:
                self.neighbors.append((right_neighbor_column, lower_neighbor_row))