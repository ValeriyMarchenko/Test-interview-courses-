def sum(*args):
    l = list(zip(*args)) 
    return l


l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(sum(l1, l2))