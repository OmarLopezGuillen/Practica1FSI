# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

ab2 = search.GPSProblem('A', 'B'
                       , search.romania)

ab3 = search.GPSProblem('O', 'U'
                       , search.romania)
                       
ab4 = search.GPSProblem('L', 'N'
                       , search.romania)

ab5 = search.GPSProblem('S', 'E'
                       , search.romania)


print(search.breadth_first_graph_search(ab).path())

print("#####################")
print("\n")


print(search.depth_first_graph_search(ab).path())

print("#####################")
print("\n")

print(search.branch_and_bounds_graph_search(ab).path())

print("#####################")
print("\n")

print(search.metodo_subestimacion(ab2).path())

print("#####################")
print("\n")

print(search.metodo_subestimacion(ab3).path())

print("#####################")
print("\n")

print(search.metodo_subestimacion(ab4).path())

print("#####################")
print("\n")

print(search.metodo_subestimacion(ab5).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
