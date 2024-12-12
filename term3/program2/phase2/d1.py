import collections
from time import *
from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)
 
xp, yp, zp = mc.player.getPos() 

dx = 0
while True:
    if mc.getBlock(xp + dx + 1, yp, zp) == 0  :
        mc.setBlock(xp + dx, yp, zp, AIR)
        dx += 1
        mc.setBlock(xp + dx, yp, zp, GLOWSTONE_BLOCK)
        sleep(0.4)
    else:
        break
