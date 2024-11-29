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

def create_maze(block_id) :
    my_file = open("c:\maze-map.txt")
    xp , yp , zp = mc.player.getPos()
    z = 0
    for line in my_file :
        z += 1
        items = line.strip().split(" ")
        x = 0
        for i in items :
            x += 1
            b = AIR if i == "p" else Block(block_id)
            mc.setBlock(xp+x, yp, zp+z, b)
            mc.setBlock(xp+x, yp+1, zp+z, b)
            mc.setBlock(xp+x, yp+2, zp+z, b)

while True :
    for chat in mc.events.pollChatPosts() :
        log(chat.message)

        if "Create maze" in chat.message :
            items = chat.message.split(" ")
            block_id = 1

            if len(items)>2 :
                block_id = int(items[2])

            create_maze(block_id)
    
    sleep(0.5)