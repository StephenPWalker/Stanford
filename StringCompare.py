def computeStringDistance(s,t): # recursion
    def recurse(u,v):
        if u == 0:
            result = v
        elif v == 0:
            result = u
        elif s[u - 1] == t[v - 1]:
            result = recurse(u - 1, v - 1)
        else:
            subCost = 1 + recurse(u - 1, v - 1)
            delCost = 1 + recurse(u - 1, v)
            insCost = 1 + recurse(u, v - 1)
            result = min(subCost, delCost, insCost)
        return result
    return recurse(len(s), len(t))

def computeStringDistanceMemozation(s,t): # recursion and memoization i.e dynamic programming
    cache = {}
    def recurse(u,v):
        if (u, v) in cache:
            return cache[(u, v)]
        if u == 0:
            result = v
        elif v == 0:
            result = u
        elif s[u - 1] == t[v - 1]:
            result = recurse(u - 1, v - 1)
        else:
            subCost = 1 + recurse(u - 1, v - 1)
            delCost = 1 + recurse(u - 1, v)
            insCost = 1 + recurse(u, v - 1)
            result = min(subCost, delCost, insCost)
        cache[(u, v)] = result
        return result
    return recurse(len(s), len(t))

s = 'cat'
t = 'cats' 
print('The minimum cost of difference between strings {} and {} is: {}'.format(s, t, computeStringDistance(s, t)))

s = 'cat' * 200
t = 'cats' * 200
print('The minimum cost of difference between strings is: {}'.format(computeStringDistanceMemozation(s, t)))
