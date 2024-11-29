import collections
from mcpi_e.minecraft import *
from mcpi_e.block import *

collections.Iterable = collections.abc.Iterable

server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

# my_file = open()
# my_file = open("unknown.txt")

mc = Minecraft.create(server_address, python_port, player_name)
xp , yp , zp = mc.player.getPos()

def pyramid(my_file, start_x, start_y, start_z):
   my = open(my_file )
   for line in my_file:
     nums = line.strip().split(" ")
     print(nums)
     x = int(nums[0]) + start_x
     y = int(nums[1]) + start_y
     z = int(nums[2]) + start_z
     b = int(nums[3])
     mc.setBlock(x, y, z, b)

for i in range(5):
  pyramid("c/asal.unknown.txt", xp, yp, zp+20*i)


