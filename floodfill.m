clear; clc;

%read in values from maze text file
%only mazes with even numbered dimensions work
fileID = fopen('maze1.txt','r');
formatSpec = '%d';
A = fscanf(fileID,formatSpec);
fclose(fileID);

%find maze dimensions
dim = sqrt(numel(A));

%convert A from vector to matrix form
A = vec2mat(A,dim);

%create a new maze with initial flood fill values
B = ones(dim);

%initialize the destination squares to zero
B(dim/2:dim/2+1, dim/2:dim/2+1) = 0;

%fill remaining squares with number of cells away from destination
%fill squares to the left and right of destination
for i=2:dim/2-1
    B(dim/2:dim/2+1, dim/2-i) = i;
    B(dim/2:dim/2+1, dim/2+1+i) = i;
end

%fill squares to top and bottom of destination
for i=2:dim/2-1
    B(dim/2-i, dim/2:dim/2+1) = i;
    B(dim/2+1+i, dim/2:dim/2+1) = i;
end

%fill upper left corner
for i=dim/2:-1:2
    for j=dim/2:-1:1
        B(i-1,j) = B(i,j)+1;
    end
end

%fill upper right corner
for i=dim/2:-1:2
    for j=dim/2+1:dim
        B(i-1,j) = B(i,j)+1;
    end
end

%fill lower left corner
for i=dim/2+1:dim-1
    for j=dim/2:-1:1
        B(i+1,j) = B(i,j)+1;
    end
end

%fill lower right corner
for i=dim/2+1:dim-1
    for j=dim/2+1:dim
        B(i+1,j) = B(i,j)+1;
    end
end

B

i = 6;
j = 1;
%initialize stack
stack = java.util.Stack();

while B(i,j) ~= 0
    [min_open, W, S, E, N] = find_min(dim,A,B,i,j);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if B(i,j) - 1 ~= min_open
        %push current cell onto stack
        stack.push([i j]);
        while ~stack.isEmpty()
            coord = stack.pop();
            m = coord(1);
            n = coord(2);
            [min_open] = find_min(dim,A,B,m,n);
            if B(m,n) - 1 ~= min_open
                B(m,n) = min_open + 1;
                %push North neighbor
                if m ~= 1
                    if B(m-1,n) ~= 0
                        stack.push([m-1 n]);
                    end
                end
                %push South neighbor
                if m ~= dim
                    if B(m+1,n) ~= 0
                        stack.push([m+1 n]);
                    end
                end
                %push West nieghbor
                if n ~= 1
                    if B(m,n-1) ~= 0
                        stack.push([m n-1]);
                    end
                end
                %push East neighbor
                if n ~= dim
                    if B(m,n+1) ~= 0
                        stack.push([m n+1]);
                    end
                end
            end
        end
    end
    %lead robot to nearest neighbor not separated by a wall and with the
    %lowest flood fill value
    if min_open == W
        j = j - 1;
    end
    if min_open == S
        i = i + 1;
    end
    if min_open == E
        j = j + 1;
    end
    if min_open == N
        i = i - 1;
    end
    
end

B
