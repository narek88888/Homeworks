# ● Create Point namedtuple
# ● Create two points objects from Point namedtuple
# ● Write a function to get distance between that two points



from collections import namedtuple

Point = namedtuple("Point", "x, y")

point1 = Point(10, 20)
point2 = Point(20, 30)


def distance_function(p1, p2):

    formula = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

    return formula

print(distance_function(point1, point2))




# print(point1.x, point1.y)


# print(point2.x, point2.y)








