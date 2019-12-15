function[min_open, W, S, E, N] = find_min(dim,A,B,i,j)
    binary = de2bi(A(i,j),4,'left-msb');

    count = 1;

    W = dim^2;
    S = dim^2;
    E = dim^2;
    N = dim^2;

    for m=1:4
        if binary(m) == 0 && count == 1
            W = B(i,j-1);
        end
        if binary(m) == 0 && count == 2
            S = B(i+1,j);
        end
        if binary(m) == 0 && count == 3
            E = B(i,j+1);
        end
        if binary(m) == 0 && count == 4
            N = B(i-1,j);
        end
        count = count + 1;
    end
    min_open = min([W S E N]);
end
