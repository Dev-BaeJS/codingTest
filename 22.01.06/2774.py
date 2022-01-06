n,m= map(int, input().split())

if( m < 45):
    if( n == 0):
        n =24
    n-=1
    m+=15
    print(n,m)
else:
    m-=45
    print(n,m)