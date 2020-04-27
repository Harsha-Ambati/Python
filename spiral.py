def spiral(r2, c2, a):
   r1 = 0;
   c1 = 0
   while (r1 < r2 and c1 < c2):
       for i in range(c1, c2):
            print(a[r1][i], end=" ")
            r1 += 1

            for i in range(r1, r2):
                print(a[i][c2 - 1], end=" ")
                c2 -= 1
       if (r1 < r2):
           for i in range(c2 - 1, (c1 - 1), -1):
                print(a[r2 - 1][i], end=" ")
                r2 -= 1
                if (c1 < c2):
                    for i in range(r2 - 1, r1 - 1, -1):
                        print(a[i][c1], end=" ")
                        c1 += 1

a = [[1, 2, 3, 4,],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

R = 4;
C = 4
spiral(R, C, a)

