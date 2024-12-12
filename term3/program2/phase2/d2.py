import collections
from time import *
from requests import *
from mcpi_e.minecraft import *
from mcpi_e.block import *
collections.Iterable = collections.abc.Iterable
server_address = "Pycraft.yasan.ac"
python_port = 11130
player_name = "a_emrani"

mc = Minecraft.create(server_address, python_port, player_name)

maze_map = get("http://mcedu.ir/yas/api/mazemap?size=small").text

maze_lines = maze_map.split("\n")
 
xp, yp, zp = mc.player.getPos() 

z = 0
for line in maze_map :
    z += 1
    items = line.split(" ") 
    x = 0 
    for line in items :
        x += 1
        b = AIR if i == "p" else STONE
        mc.setBlock(xp+x, yp, zp+z, b )
 
def create_maze(block_id) :
    my_file = open("c:\maze-map.txt")
    xp , yp , zp = mc.player.getPos()
    z = 0
    maze_lines = maze_map.split("\n")
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

while True:
    for chat in mc.events.pollChatPosts():
        log(chat.message)

        if chat.message.startswith("Create maze"):
            parts = chat.message.split()
            block_id = int(parts[2])
            size = parts[3]  # small, medium, or large
            if size == "small":
                api_url = "http://mcedu.ir/yas/api/mazemap?size=small"
            elif size == "medium":
                api_url = "http://mcedu.ir/yas/api/mazemap?size=medium"
            elif size == "large":
                api_url = "http://mcedu.ir/yas/api/mazemap?size=large"
            else:
                mc.postChat("Invalid size. Please use small, medium, or large.")
                continue

            maze_map = get(api_url).text
            create_maze(block_id, maze_map)

        sleep(0.5)
                    
