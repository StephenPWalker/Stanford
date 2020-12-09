import numpy as np
#####################################################################
#Generate artifical data
#####################################################################

true_w = np.array([1,2,3,4,5])
d = len(true_w)
points = []
for i in range(100000):
    x = np.random.randn(d)
    y = true_w.dot(x) + np.random.randn()
    points.append((x,y))
#####################################################################
#Gradient descent
#####################################################################
    
def F(w):
    return sum((w.dot(x) - y)**2 for x,y in points) / len(points)

def dF(w):
    return sum(2*(w.dot(x) - y) * x for x,y in points) / len(points)

def gradientDescent(F, dF, d):
    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = F(w)
        gradient = dF(w)
        w = w - eta * gradient
        print('Iteration {}: w = {}, F(w) = {}'.format(t, w, value))
        
#####################################################################
#Stochastic gradient
#####################################################################
        
def sF(w, i):
    x, y = points[i]
    return (w.dot(x) - y)**2

def sdF(w, i):
    x, y = points[i]
    return 2*(w.dot(x) - y) * x

def stochasticGradientDescent(sF, sdF, d, n):
    w = np.zeros(d)
    eta = 1
    numUpdates = 0
    for t in range(1000):
        for i in range(n):
            value = sF(w, i)
            gradient = sdF(w, i)
            numUpdates += 1
            eta = 1.0 / numUpdates
            w = w - eta * gradient
        print('Iteration {}: w = {}, F(w) = {}'.format(t, w, value))
#####################################################################
#Program to run
#####################################################################

#gradientDescent(F,dF,d)
stochasticGradientDescent(sF, sdF, d, len(points))
        
