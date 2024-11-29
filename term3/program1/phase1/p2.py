#from mincraft_connection import *
from mcpi_e.minecraft import *
from mcpi_e.block import *
import collections
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

xp , yp , zp = mc.player.getPos()

for y in range(5):
  for x in range(5-y):
    mc.setBlock(x+y+1+xp, y+yp, zp, GOLD_BLOCK)
    # print(f'({x+y+1},{y+1}) ', end="")
  # print("", end="\n")

        
for y in range(5):
  for x in range(5-y):
    mc.setBlock(x+6+xp, y+yp, zp, GOLD_BLOCK)
    # print(f'({x+6},{y+1}) ', end="")
  # print("", end="\n")


