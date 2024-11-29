from_x, from_y, from_z = 128, -65, -143
to_x, to_y, to_z = 141, -59, -115

my_file = open("house1.txt", "w")

for y in range(from_y, to_y):
    for z in range(from_z, to_z):
        for x in range(from_x, to_x):
            b = mc.getBlock(x, y, z)
            if b != 0 :
                line = f"{x-from_x} {y-from_y} {z-from_z} {b}\n"
                my_file.write(line)

print("SCAN COMPLETED.")