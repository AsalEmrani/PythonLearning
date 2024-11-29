import collections


from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)
xp , yp , zp = mc.player.getPos()

for y in range(5):
    for z in range(4-y, 5+y, 1):
        for x in range(4-y, 5+y, 1):
             if x==4-y or x==5+y-1 or z==4-y or z==5+y-1 :
                mc.setBlock(x+xp, y+yp, z+zp, GOLD_BLOCK)