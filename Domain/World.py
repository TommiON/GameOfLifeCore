class World:
    width = None
    height = None
    toroidal_in_X_dimension = True
    toroidal_in_Y_dimension = True
    generation_one = {}
    
    @classmethod
    def set_width(cls, width):
        cls.width = width

    @classmethod
    def set_height(cls, height):
        cls.height = height
    
    @classmethod
    def set_generation_one(cls, cells):
        cls.generation_one = cells

    @classmethod
    def set_toroidal_in_X_dimension(cls, value):
        cls.toroidal_in_X_dimension = value
    
    @classmethod
    def set_toroidal_in_Y_dimension(cls, value):
        print("Setteriin?", value)
        cls.toroidal_in_Y_dimension = value