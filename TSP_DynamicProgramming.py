from itertools import chain, combinations


def make_subset(s: list):                         # a function which returns subsets of a list from https://stackoverflow.com/a/1482316/12466594
    lst = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    lst = [set(x) for x in lst]
    return lst

def make_dict(lst):                                 # make a dictionaty from element of a list and its indexs
    dict1 = dict()
    for value in lst:
        dict1[tuple(value)] = int(lst.index(value))
    return dict1

def travel(n: int, W: list, V: list):                # main function, n: number of vertices, W: Adjacency Matrix, V: vertices
    v1 = V[0]
    V.remove(v1)                                    # remove v1 from vertices
    subsets_v = make_subset(V)                         # make all subsets of vertices

    subsets_index = make_dict(subsets_v)            # a dictionary for finding index of subsets in matrix D, P

    D = [[0] * len(subsets_v) for i in range(n)]        # initializing matrix D
    P = [[0] * len(subsets_v) for i in range(n)]        # initializing matrix P


    for i in range(1, n):           
        D[i][subsets_index[tuple(set())]] = W[i][0]     

    for k in range(1, n-1):
        for subset in subsets_v:
            if len(subset) == k:
                for i in V:
                    if (i != 1) and (i not in subset):
                        temp_list = list()
                        temp_list2 = list()
                        for j in subset:
                            temp_list.append(W[i-1][j-1] + D[j-1][subsets_index[tuple(subset-set([j]))]])
                            temp_list2.append(j)                            #store j for adding to P matrix 
                        min_val = min(temp_list)
                        D[i-1][subsets_index[tuple(subset)]] = min_val          # store minimum value in D matrix
                        j_gave_min = temp_list2[temp_list.index(min_val)]       
                        P[i-1][subsets_index[tuple(subset)]] = j_gave_min       # store j that gave the minimum

    temp_list = list()
    temp_list2 = list()
    for j in range(2, n+1):                                                     
        temp_list.append(W[0][j-1]  + D[j-1][subsets_index[tuple({x for x in V if x != j})]])   
        temp_list2.append(j)

    min_val = min(temp_list)
    D[0][subsets_index[tuple(V)]] = min_val                 # store final pathweight
    j_gave_min = temp_list2[temp_list.index(min_val)]
    P[0][subsets_index[tuple(V)]] = j_gave_min              # store j that gave the minimum
    min_length = D[0][subsets_index[tuple(V)]]              # save minimum length in min_length
    
    v1 = 1
    vertices = V.copy()
    path = list()
    path.append(v1)
    for i in range(len(V)):                                 # finding path from P matrix
        v1 = P[v1-1][subsets_index[tuple({x for x in vertices if x != v1})]]
        path.append(v1)                                    
        vertices.remove(v1)

    return min_length, path


W = [[0, 10, 15, 20],
     [5, 0, 9, 10],
     [6, 13, 0, 12],
     [8, 8, 9, 0]]

x, y = travel(4, W, [1, 2, 3, 4])

print(x)
print(y)
