"""First N natural numbers"""

N = int(input())
i = 1
while i <= N:
    print(i)
    i+=1

"""First N odd natural numbers"""

N = int(input())
i = 1
while i <= N:
    if(i%2 != 0):
        print(i)
    i+=1
