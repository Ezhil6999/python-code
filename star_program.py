* * * * * * * * * 
*   * * * * *   *
*   *   *   *   *
*   * * * * *   *
* * * * * * * * *


n = 11

for i in range(n):
    for j in range(n):
        if i>=j and i+j>=n-1 and i%2==0 or i<=j and i+j<=n-1 and i%2==0 or i>=j and i+j<=n-1 and j%2==0 or i<=j and i+j>=n-1 and j%2==0:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()



or

input = 11

v =0 

if input%2 ==0:
    v = int(input/2)
else:
    v = int(input/2)

for i in range(input):
    for j in range(input):
        if i==0 or i==input-1 or j==0 or j==input-1:
            print("* ",end='')
        elif (i==j and i%2==0) or (i+j==input-1 and j%2==0):
            print("* ",end='')
        elif j%2==0 and input-1-j > i > j and j!=v:
            # print(input-1-j)
            print("* ",end='')
        elif  i%2==0 and input-1-i > j > i and i!=v:
            print("* ",end='')
        elif j%2==0 and input-1-j < i < j and j!=v:
            print("* ",end='')
        elif i%2==0 and input-1-i < j < i and i!=v:
            print("* ",end='')
        else:
            print("  ",end='')
    print()
