def find_min(dim, A, B, i, j):
    binary = []
    
    for char in A[i, j]:
        binary.append(int(char))
    
    count = 1
    
    W = dim**2
    S = dim**2
    E = dim**2
    N = dim**2
    
    for index in range(4):
        if binary[index] == 0 and count == 1:
            W = B[i, j-1]
        if binary[index] == 0 and count == 2:
            S = B[i+1, j]
        if binary[index] == 0 and count == 3:
            E = B[i, j+1]
        if binary[index] == 0 and count == 4:
            N = B[i-1, j]
        count += 1
    
    min_open = min([W, S, E, N])
    
    return [min_open, W, S, E, N]
