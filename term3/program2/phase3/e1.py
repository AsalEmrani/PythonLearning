import collections
from random import *
from time import *

from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

x, y, z = mc.player.getTilePos() 

dir = "e"

exit_block = STONE

while True: 
    if dir == "e" :
        if mc.getBlock(x, y, z+1) == 0 :
            z += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "s"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x+1, y, z) == 0 :
            x += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "e"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z-1) == 0 :
            z -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "n"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x-1, y, z) == 0 :
            x -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "w"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
    elif dir == "s" :
        if mc.getBlock(x-1, y, z) == 0 :
            x -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "w"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z+1) == 0 :
            z += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "s"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x+1, y, z) == 0 :
            x += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "e"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z-1) == 0 :
            z -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "n"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
    elif dir == "w" :
        if mc.getBlock(x, y, z-1) == 0 :
            z -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "n"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x-1, y, z) == 0 :
            x -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "w"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z+1) == 0 :
            z += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "s"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x+1, y, z) == 0 :
            x += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "e"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
    elif dir == "n" :
        if mc.getBlock(x+1, y, z) == 0 :
            x += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "e"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z-1) == 0 :
            z -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "n"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x-1, y, z) == 0 :
            x -= 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "w"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break
        elif mc.getBlock(x, y, z+1) == 0 :
            z += 1
            mc.setBlock(x, y, z, GLOWSTONE_BLOCK)
            dir = "s"
            if mc.getBlock(x, y, z + 1) == EXIT_BLOCK:
                print("شما از هزارتو خارج شدید!")
                break

            
        
        