n=int(input())
s1 = list(map(int,input().strip().split()))[:n]
s1.sort(reverse=True)
for i in s1: 
    print(i, end="") 
