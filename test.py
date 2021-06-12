loc = (9, 9)
middleNeighbors = [(x, y) for x in range(loc[0] - 1, loc[0] + 2) for y in range(loc[1] - 1, loc[1] + 2) if
                   (x, y) != loc and 0 <= x < 10 and 0 <= y < 10]  # middle

locEdge = (0, 5)

edgeNeighbors = [(x, y) for x in range(locEdge[0] + 2) for y in range(locEdge[1] - 1, locEdge[1] + 2) if
                 (x, y) != locEdge]  # edge

locCorner = (9, 9)

cornerNeighbors = [(x, y) for x in range(locCorner[0] - 1, locCorner[0] + 1) for y in
                   range(locCorner[1] - 1, locCorner[1] + 1)
                   if (x, y) != locCorner]  # corner

print(middleNeighbors)

