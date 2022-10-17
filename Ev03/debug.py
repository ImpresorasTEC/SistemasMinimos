import random
l = [random.randint(0,100) for i in range(100)]
l2 = []
for e in l:
    print(e)
print("\n")

for i in range(100):
    l2.append(l[i])
    if((i+1)%10==0):
        print("PROMEDIO:", sum(l2)/10)
        l2.clear()
