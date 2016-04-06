import pygame, Funk

__author__ = 'Bhavik & Ram'

class Tile(pygame.Rect): #every tiles are rectangular shaped so pygame.Rect

    List = [] #creating list for tiles
    width, height = 32, 32 #giving tiles width and height
    total_tiles = 1 #keeping track on total tiles
    H, V = 1, 22  #giving horizontal and vertical dis for object_classes file

    #creating obstacles tiles
    invalids = [1,2,3,4,5,6,7,8,10,11,12,13,14,20,21,22,
    23,26,28,29,30,32,35,36,41,44,
    45,58,59,61,62,64,66,
    67,70,77,78,88,
    89,92,94,95,99,100,102,103,105,106,107,108,110,
    111,112,113,117,119,124,128,
    133,139,141,142,143,146,152,154,
    155,156,157,158,159,168,172,174,176,
    177,181,182,184,187,188,189,190,191,192,194,197,198,
    199,204,206,208,209,212,214,215,220,
    221,241,242,
    243,251,264,
    265,270,273,275,278,280,281,283,285,286,
    287,288,289,290,291,292,293,294,295,296,297,298,299,
    300,301,302,303,304,305,306,307,308]


    def __init__(self, x, y, Type): #creating constructor with arguments (self, x-cordi, y-cordi, Type-1/0 used or not)

        self.parent = None #to store parent detail
        self.H, self.G, self.F = 0,0,0 #to calculate destination distance

        self.type = Type
        self.number = Tile.total_tiles # we are going to give tile number to our tile
        Tile.total_tiles += 1

        if Type == 'empty': #if there is any tile is walkable or not
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) ) #calling a Constuctor

        Tile.List.append(self) #appending the tile to list

    @staticmethod #we are going to call the get tile method
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod #drawing our tiles in our display
    def draw_tiles(screen):
        half = Tile.width / 2

        for tile in Tile.List:

            pass

            # if not(tile.type == 'empty'):
            #     pygame.draw.rect(screen, [40, 40, 40], tile )

            # if tile.G != 0:
            #   Funk.text_to_screen(screen, tile.G, tile.x, tile.y + half, color = [120, 157, 40])
            # if tile.H != 0:
            #   Funk.text_to_screen(screen, tile.H, tile.x + half, tile.y + half, color = [20 , 67, 150])
            # if tile.F != 0:
            #   Funk.text_to_screen(screen, tile.F, tile.x + half, tile.y, color = [56, 177, 177])

            # Funk.text_to_screen(screen, tile.number, tile.x, tile.y)