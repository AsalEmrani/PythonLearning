import collections


from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)
xp , yp , zp = mc.player.getPos()

for y in range(5) :
    for z in range(y, 9-y, 1) :
        for x in range(y, 9-y, 1):
            if x==y or x==9-y-1 or z==y or z==9-y-1:
                bl = STONE
                if y==4:
                    bl = LAVA
                mc.setBlock(x+xp, y+yp, z+zp, bl)