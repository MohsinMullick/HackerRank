"""Task:::
The provided code stub reads an integer, n , from STDIN. For all non-negative integers ,
 print 3 is[0,1,2]i^2 .
Example
The list of non-negative integers that are less than  is .
 Print the square of 3 is[0,1,2] each number on a separate line."""
if __name__=="__main__":
    n=int(input().strip())
    for i in range (n):
        print(i*i)

