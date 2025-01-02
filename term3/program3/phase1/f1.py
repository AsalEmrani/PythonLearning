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
road_points = []
exit_block = STONE
processing = True  # متغیر برای تشخیص دور اول یا دوم
mc.postToChat("بلاک در حال پردازش مسیر است...")

while True: 
    if mc.getBlock(x, y, z) == STONE.id :  # بررسی پایان مسیر
        mc.postToChat("شما از هزارتو خارج شدید!")
        processing = False
        break
    
    mc.setBlock(x, y, z, AIR)  # مخفی‌کردن بلاک‌ها در دور اول
    if dir == "e":
        if mc.getBlock(x, y, z+1) == 0:
            z += 1
            dir = "s"
        elif mc.getBlock(x+1, y, z) == 0:
            x += 1
            dir = "e"
        elif mc.getBlock(x, y, z-1) == 0:
            z -= 1
            dir = "n"
        elif mc.getBlock(x-1, y, z) == 0:
            x -= 1
            dir = "w"
    elif dir == "s":
        if mc.getBlock(x-1, y, z) == 0:
            x -= 1
            dir = "w"
        elif mc.getBlock(x, y, z+1) == 0:
            z += 1
            dir = "s"
        elif mc.getBlock(x+1, y, z) == 0:
            x += 1
            dir = "e"
        elif mc.getBlock(x, y, z-1) == 0:
            z -= 1
            dir = "n"
    elif dir == "w":
        if mc.getBlock(x, y, z-1) == 0:
            z -= 1
            dir = "n"
        elif mc.getBlock(x-1, y, z) == 0:
            x -= 1
            dir = "w"
        elif mc.getBlock(x, y, z+1) == 0:
            z += 1
            dir = "s"
        elif mc.getBlock(x+1, y, z) == 0:
            x += 1
            dir = "e"
    elif dir == "n":
        if mc.getBlock(x+1, y, z) == 0:
            x += 1
            dir = "e"
        elif mc.getBlock(x, y, z-1) == 0:
            z -= 1
            dir = "n"
        elif mc.getBlock(x-1, y, z) == 0:
            x -= 1
            dir = "w"
        elif mc.getBlock(x, y, z+1) == 0:
            z += 1
            dir = "s"

    # ذخیره‌کردن موقعیت
    point = [x, y, z]
    if point in road_points:
        i = road_points.index(point)
        del road_points[i:]
    road_points.append(point)

    if mc.getBlock(x, y-1, z) == STONE.id:  # پایان مسیر
        mc.postToChat("*** مسیر پردازش شد! ***")
        break

    sleep(0.1)

# نمایش مسیر در دور دوم
for p in road_points:
    mc.setBlock(x, y, z, AIR)  # پاک‌کردن بلاک‌های قبلی
    x, y, z = p
    mc.setBlock(x, y, z, GLOWSTONE_BLOCK)  # نمایش مسیر
    sleep(0.4)


