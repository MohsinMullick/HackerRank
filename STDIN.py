"""Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

____The first line contains the sum of the two numbers.
____The second line contains the difference of the two numbers (first - second).
____The third line contains the product of the two numbers."""
if __name__=="__main__":
    a=int(input().strip())
    b=int(input().strip())
    sum=a+b
    print(sum)
    diff=a-b
    print(diff)
    pro=a*b
    print(pro)
