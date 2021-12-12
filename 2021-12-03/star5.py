filename = 'input1.txt'
gamma = b''
epsilon = b''
bits = []
initialised = False

with open(filename, 'r') as file:
    for line in file.readlines():
        line = line.strip('\n')
        print(line)
        if not initialised:
            bits = [0] * (len(line))
            initialised = True
        for bit in range(len(line)):
            if line[bit] == '1':
                bits[bit] += 1
            elif line[bit] == '0':
                bits[bit] -= 1
            else:
                print(f"Error: {line[bit]}")
    print(f"BITS: {bits}")


for bit in bits:
    if bit > 0:
        gamma += b'1'
        epsilon += b'0'
    else:
        gamma += b'0'
        epsilon += b'1'

g = int(gamma, 2)
e = int(epsilon, 2)

print(f"Gamma   = {g}")
print(f"Epsilon = {e}")
mul = g * e
print(f"Answer  = {mul}")