import numpy as np
from find_min import find_min

def floodfill(A):
    #input maze dimensions
    #only even numbers
    dim = 6

    #distance value matrix
    B = np.zeros((dim, dim), dtype=int)

    #set int type
    half_dim = int(dim/2)

    #fill squares to the left and right of destination
    for i in range(1, half_dim):
        B[half_dim - 1:half_dim + 1, half_dim - 1 - i] = i
        B[half_dim - 1:half_dim + 1, half_dim + i] = i
        
    #fill squares to top and bottom of destination
    for i in range(1, half_dim):
        B[half_dim - 1 - i, half_dim - 1:half_dim + 1] = i
        B[half_dim + i, half_dim - 1:half_dim + 1] = i

    #fill upper left corner
    for i in range(half_dim - 1, -1, -1):
        for j in range(half_dim - 2, -1, -1):
            B[i - 1, j] = B[i, j] + 1
            
    #fill upper right corner
    for i in range(half_dim - 1, -1, -1):
        for j in range(half_dim + 1, dim):
            B[i - 1, j] = B[i, j] + 1
            
    #fill lower left corner
    for i in range(half_dim, dim - 1):
        for j in range(half_dim - 2, -1, -1):
            B[i + 1, j] = B[i, j] + 1

    #fill lower right corner
    for i in range(half_dim, dim - 1):
        for j in range(half_dim + 1, dim):
            B[i + 1, j] = B[i, j] + 1

    #start in lower left corner
    i = dim - 1
    j = 0

    #initialize stack
    stack = []

    while B[i, j] != 0:
        #binary = read_sensor()
        min_open, W, S, E, N = find_min(dim, A, B, i, j)
        if B[i, j] - 1 != min_open:
            #push current cell onto stack
            stack.append( (i, j) )
            while len(stack) != 0:
                m, n = stack.pop()
                #binary = read_sensor()
                min_open = find_min(dim, A, B, m, n)[0]
                if B[m, n] - 1 != min_open:
                    B[m, n] = min_open + 1
                    #push North neighbor
                    if m != 0:
                        if B[m - 1, n] != 0:
                            stack.append( (m-1, n) )
                    #push South neighbor
                    if m != dim - 1:
                        if B[m + 1, n] != 0:
                            stack.append( (m+1, n) )
                    #push West neighbor
                    if n != 0:
                        if B[m, n - 1] != 0:
                            stack.append( (m, n-1) )
                    #push East neighbor
                    if n != dim - 1:
                        if B[m, n + 1] != 0:
                            stack.append( (m, n+1) )
        #lead robot to nearest neighbor not separated by a wall and with the lowest flood fill value
        if min_open == W:
            j = j - 1
        if min_open == S:
            i = i + 1
        if min_open == E:
            j = j + 1
        if min_open == N:
            i = i - 1
    return B
