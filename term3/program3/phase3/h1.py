from math import *
import collections
from mcpi_e.minecraft import *
from mcpi_e.block import *
from PIL import Image, ImageSequence
from time import *

collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)
px, py, pz = mc.player.getTilePos() 

blockColorList = [
    # [[R,G,B],[ID,Data]]
    [[0, 0, 0], [0, 0]],  # Air
    [[125, 125, 125], [1, 0]],  # Smooth Stone
    [[133, 96, 66], [3, 0]],  # Dirt
    [[117, 117, 117], [4, 0]],  # Cobblestone
    [[156, 127, 78], [5, 0]],  # Wooden Plank
    [[83, 83, 83], [7, 0]],  # Bedrock
    [[217, 210, 158], [12, 0]],  # Sand
    [[136, 126, 125], [13, 0]],  # Gravel
    [[143, 139, 124], [14, 0]],  # Gold Ore
    [[135, 130, 126], [15, 0]],  # Iron Ore
    [[115, 115, 115], [16, 0]],  # Coal Ore
    [[154, 125, 77], [17, 0]],  # Wood
    [[182, 182, 57], [19, 0]],  # Sponge
    [[221, 221, 221], [35, 0]],  # White Wool
    [[233, 126, 55], [35, 1]],  # Orange Wool
    [[179, 75, 200], [35, 2]],  # Magenta Wool
    [[103, 137, 211], [35, 3]],  # Light Blue Wool
    [[192, 179, 28], [35, 4]],  # Yellow Wool
    [[59, 187, 47], [35, 5]],  # Light Green Wool
    [[217, 132, 153], [35, 6]],  # Pink Wool
    [[66, 67, 67], [35, 7]],  # Dark Gray Wool
    [[157, 164, 165], [35, 8]],  # Gray Wool
    [[39, 116, 148], [35, 9]],  # Cyan Wool
    [[128, 53, 195], [35, 10]],  # Purple Wool
    [[39, 51, 153], [35, 11]],  # Blue Wool
    [[85, 51, 27], [35, 12]],  # Brown Wool
    [[55, 76, 24], [35, 13]],  # Dark Green Wool
    [[162, 44, 42], [35, 14]],  # Red Wool
    [[26, 23, 23], [35, 15]],  # Black Wool
    [[249, 236, 77], [41, 0]],  # Gold
    [[230, 230, 230], [42, 0]],  # Iron
    [[159, 159, 159], [43, 0]],  # TwoHalves
    [[155, 110, 97], [45, 0]],  # Brick
    [[90, 108, 90], [48, 0]],  # Mossy Cobblestone
    [[20, 18, 29], [49, 0]],  # Obsidian
    [[129, 140, 143], [56, 0]],  # Diamond Ore
    [[99, 219, 213], [57, 0]],  # Diamond Block
    [[107, 71, 42], [58, 0]],  # Workbench
    [[132, 107, 107], [73, 0]],  # Redstone Ore
    [[239, 251, 251], [80, 0]],  # Snow Block
    [[158, 164, 176], [82, 0]],  # Clay
    [[107, 73, 55], [84, 0]],  # Jukebox
    [[192, 118, 21], [86, 0]],  # Pumpkin
    [[110, 53, 51], [87, 0]],  # Netherrack
    [[84, 64, 51], [88, 0]],  # Soul Sand
    [[137, 112, 64], [89, 0]]  # Glowstone
]


def getBlockColor(RGB):
    similarBlock = [0, 0]
    minDistance = float('inf')
    for index in blockColorList:
        eachDistance = colorDistance(RGB, index[0])

        if (eachDistance < minDistance):
            minDistance = eachDistance
            similarBlock = index[1]

    return similarBlock


def colorDistance(colorRGB, blockRGB):
    return sqrt(
        pow(colorRGB[0] - blockRGB[0], 2) + pow(colorRGB[1] - blockRGB[1], 2) + pow(colorRGB[2] - blockRGB[2], 2))

def renderImage(image, clean, delta):
    width,height = image.size
    for x in range(width) :
        for y in range(height) :
            rgb = image.getpixel((x,y))
            block = getBlockColor(rgb)
            block_parametrs = Block(block[0], block[1])
            if clean == True:
                mc.setBlock(y+px, py, x+pz - delta , AIR)
            else:
                mc.setBlock(y+px, py, x+pz - delta, block_parametrs)


mc.settings.SYS_SPEED = 0
gif_image = Image.open('c:\img\dog.gif')

dx = 0
for frame in ImageSequence.Iterator(gif_image):
    converted_frame = frame.convert('RGB')
    renderImage(converted_frame, False, dx)
    sleep(2)
    renderImage(converted_frame, True, dx)
    dx += 1