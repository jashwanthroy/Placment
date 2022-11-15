n=int(input())
l=list(list(map(int,input().strip('[]').split(',')))[:n]
minimum=l.min()
print(minimum)
