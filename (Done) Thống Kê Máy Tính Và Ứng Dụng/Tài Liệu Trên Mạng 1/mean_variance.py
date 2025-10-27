import numpy as np 
data = [[2, 4], [3, 7], [4, 6], [5, 5], [2, 3]]

def mean(data):
    return sum(data)/len(data)
mu = mean(data)
print(mu)

def varance(data):
    mu = mean(data)
    return sum([(point - mu)**2 for point in data])/len(data)
print(varance(data))