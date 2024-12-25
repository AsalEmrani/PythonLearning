import collections
import random
from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

x, y, z = mc.player.getTilePos()

# ابعاد خانه
width = 10
height = 5
depth = 10
# ابعاد سقف
roof_width = width
roof_depth = depth
roof_height = 5
# مختصات مرکز سقف (بر اساس مختصات خانه تنظیم شده)
roof_x = x + width // 2
roof_y = y + height
roof_z = z + depth // 2
# تنظیم پارامترها
wall_material = WOOD
roof_material = GLASS
door_block = DOOR_WOOD
floor_material = IRON_BLOCK

def add_doors(x, y, z, block):
    door_width = 2  # عرض هر در
    mc.setBlock(x, y, z, block)
    mc.setBlock(x, y+1, z, block)
    mc.setBlock(x+door_width, y, z, block)
    mc.setBlock(x+door_width, y+1, z, block)

def create_garden(x, y, z, width, depth, block_types):
    for i in range(height):
        for j in range(width):
            mc.setBlock(x+j, y+i, z, random.choice(block_types))

def create_pool(x, y, z, width, depth, height, block):
    for i in range(height):
        for j in range(width):
            for k in range(depth):
                mc.setBlock(x+j, y+i, z+k, block)

def build_walls(x, y, z, width, height, depth, block):
    for row in range(height):
        for column in range(width):
            mc.setBlock(x+column, y+row, z, block)
            mc.setBlock(x+column, y+row, z+depth-1, block)
        for layer in range(depth-2):
            mc.setBlock(x, y+row, z+layer+1, block)
            mc.setBlock(x+width-1, y+row, z+layer+1, block)
        if row == 0:
            mc.setBlocks(x, y, z+layer+1, x+width-1, y, z+layer+1, floor_material)

def build_roof(roof_x, roof_y, roof_z, width, depth, height, block):
    for i in range(height):
        for j in range(width):
            for k in range(depth):
                # محاسبه ارتفاع بلوک بر اساس فاصله از مرکز
                block_height = height - abs(j - width//2)
                if i <= block_height:
                    mc.setBlock(roof_x+j-width//2, roof_y+i, roof_z+k-depth//2, block)

# ساخت خانه
build_walls(x, y, z, width, height, depth, wall_material)
build_roof(roof_x, roof_y, roof_z, roof_width, roof_depth, roof_height, roof_material)

# اضافه کردن دو در در وسط دیوار جلویی
door_x = x + width // 2 - 1  # یک واحد به چپ جابجا شدیم تا دو در کنار هم قرار بگیرند
add_doors(door_x, y, z, DOOR_WOOD)

# اضافه کردن باغچه
garden_x = x + width + 2
garden_y = y
garden_z = z
garden_width = 10
garden_depth = 10
garden_blocks = [GRASS, FLOWER_YELLOW, FLOWER_CYAN]
create_garden(garden_x, garden_y, garden_z, garden_width, garden_depth, garden_blocks)