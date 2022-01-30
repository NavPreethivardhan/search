x = [1,2,3]
y = [3,4,5]
sol = []
i = 0
while i < len(x) and i< len(y):
    a = x[i]
    b = y[i]
    sol.append((a,b))
    i+=1
print((x, y))