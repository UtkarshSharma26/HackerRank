import math
k=5
lamda=2.5
result=((lamda**k)*(math.exp(-lamda)))/math.factorial(k)
print(round(result,3))