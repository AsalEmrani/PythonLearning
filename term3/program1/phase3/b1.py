import collections


from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

xp , yp , zp = mc.player.getPos()

from_x, from_y, frome_z = -67, 106, -251
to_x, to_y, to_z = -59, 111, -243

file = open("house.txt", "w")

for y in range(from_y, to_y) :
    for z in range(frome_z, to_z) :
        for x in range(from_x, to_x) :
            b = mc.getBlock(x, y, z)
            if b != 0 :
                line = f"{x-from_x} {y-from_y} {z-frome_z} {b} \n"
                file.write(line)

print("Scan completed!")