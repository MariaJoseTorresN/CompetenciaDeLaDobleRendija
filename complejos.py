
def suma(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]

def producto(c1, c2):
    a = (c1[0] * c2[0]) + (-(c1[1] * c2[1]))
    b = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (c1[0] * c2[0]) + (-(c1[1] * c2[1])), (c1[0] * c2[1]) + (c1[1] * c2[0])

def module(c):
    return (c[0]**2 + c[1]**2)**(1/2)
