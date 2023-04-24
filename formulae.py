import numpy as np
import math

def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

def arrangements(n,k):
    return np.math.factorial(n) // np.math.factorial(n-k)

def permutation(n):
    return np.math.factorial(n)

def bayesformula(p_a_b, p_b, p_a):
    return p_a_b*p_b/p_a

def probability(m,n):
    return m/n

def bernulli(n,k,p):
    return(combinations(n,k)*(p**k)*((1-p)**(n-k)))

def puasson(la,m):
    return(((la**m)/np.math.factorial(m))*(math.e**(-1*la)))

def expected_value(n,p):
    return n*p

def standard_deviation(n,p):
    return np.math.sqrt(expected_value(n,p)*(1-p))