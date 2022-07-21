
W = [[0, 10, 15, 20],             # Example of distance matrix
     [5, 0, 9, 10],
     [6, 13, 0, 12],
     [8, 8, 9, 0]]


def tsp(Vi: int, A: list):         # The main function, TSP which requiems a start point and other points

    if A:                          # If A is NOT empty

        cost_list = list()         # A list of path costs
        visited_list = list()      # Vertex visited list
        
        for j in A:                # In A, iterate

            tsp_, Vmin = tsp(j, [x for x in A if x != j])    # Recursively compute the shortest path and visited vertex
            cost_list.append(W[Vi - 1][j - 1] + tsp_)        # Sum of the shortest path and starting point
            path = Vmin + "-->" +str(j)                      # Visited vertex
            visited_list.append(path)                        # store the visited vertex
        
        min_val = min(cost_list)                      # caculate minimum path
        index_min = cost_list.index(min_val)          # find index of minimum path
        min_V = visited_list[index_min]               # store the vertexes that minimum path visited
        
        return min_val, min_V                         # returns minimum path and its visited vertexes

    else:                                      # If A is empty
        return W[Vi-1][0], str()               # returns path of Vi to the starting point


print(tsp(1, [2, 3, 4]))                   
