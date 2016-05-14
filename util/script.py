import socket

# iterations and size get defined externally

width = int(size)
height = int(size)
iterations = int(iterations)

def mandel(c):
    z = 0
    stop = iterations
    for h in range(0,iterations):
        z = z**2 + c
        if abs(z) > 2:
            stop = h
            break

    return stop
    # if abs(z) >= 2:
    #     return (False, stop)
    # else:
    #     return (True, stop)

hostname = socket.gethostname()
data = None
with open('/root/machines/' + hostname, "r") as infile:
    data = [tuple(map(int, line.split(','))) for line in infile]

for x, y in data:
    # map coords into (-2, 2)
    real = x / (width/2.0) - 1.5
    img = y / (height/2.0) - 1.0
    c = complex(real, img)
    print(str(x) + ',' + str(y) + ',' + str(mandel(c)))
