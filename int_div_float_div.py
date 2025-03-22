"""Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a//b
 . The second line should contain the result of float division, a / b.

No rounding or formatting is necessary."""
if __name__=="__main__":
    a=int(input().strip())
    b=int(input().strip())
    div=a//b
    print(div)
    f_div=a/b
    print(f_div)

