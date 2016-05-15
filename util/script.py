import socket

# iterations and size get defined externally

width = int(size)
height = int(size)
iterations = int(iterations)

mandelbox = {'x':(-0.5, -0.4), 'y':(-0.6, -0.5)}

def transform(val, oldmax, newbounds):
    newmin = float(newbounds[0])
    newmax = float(newbounds[1])
    return (val / (oldmax / (newmax - newmin))) + newmin

def mandel(c):
    z = 0
    stop = iterations
    for h in range(0,iterations):
        z = z**2 + c
        if abs(z) > 2:
            stop = h
            break

    return stop

hostname = socket.gethostname()
data = None
with open('/root/machines/' + hostname, "r") as infile:
    data = [tuple(map(int, line.split(','))) for line in infile]

for x, y in data:
    real = transform(x, width, mandelbox['x'])
    img = transform(y, height, mandelbox['y'])
    c = complex(real, img)
    print(str(x) + ',' + str(y) + ',' + str(mandel(c)))
