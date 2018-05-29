class Level:
    """create an object of this class to make level
        add different objects to this           """
    def __init__(self):
        self.__all_spines = []
        self.__all_walls = []
        self.__all_enemies = []
        self.__all_portals = []
        self.__all_textures = []
        self.__all_bitcoins = []

    def add_wall(self, wall):
        self.__all_walls.append(wall)

    def get_all_walls(self):
        return self.__all_walls

    def add_spine(self, spine):
        self.__all_spines.append(spine)

    def get_all_spines(self):
        return self.__all_spines

    def add_enemy(self, enemy):
        self.__all_enemies.append(enemy)

    def get_all_enemies(self):
        return self.__all_enemies

    def add_portal(self, portal):
        self.__all_portals.append(portal)

    def get_all_portals(self):
        return self.__all_portals

    def add_texture(self, texture):
        self.__all_textures.append(texture)

    def get_all_textures(self):
        return self.__all_textures

    def add_bitcoin(self, bitcoin):
        self.__all_bitcoins.append(bitcoin)

    def get_all_bitcoins(self):
        return self.__all_bitcoins
