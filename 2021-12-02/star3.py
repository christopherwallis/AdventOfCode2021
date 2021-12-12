filename = 'input3.txt'
forward = 0
depth = 0


with open(filename, 'r') as file:
    line = file.readline().strip('\n').split(' ')
    print(f"{line[0]}: {line[1]}")

    while True:
        if line[0] == "forward":
            forward = forward + int(line[1])
        if line[0] == "down":
            depth = depth + int(line[1])
        if line[0] == "up":
            depth = depth - int(line[1])
        try:
            line = file.readline().strip('\n').split(' ')
            print(f"{line[0]}: {line[1]}")
        except IndexError as e:
            print(e)
            break


print(f"Forward = {forward}")
print(f"Depth = {depth}")

print(f"Multiple = {forward * depth}")