#import mincraft_connection
import collections


from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

xp , yp , zp = mc.player.getPos()

for x in range(5) :
    for z in range(5) :
        mc.setBlock(x+xp , yp , z+zp , GOLD_BLOCK)
