
import numpy as np

# Here weights have be decided, the X (input from csv) will go as 
# as the sceond parameter to perceptronOutput (activation) function
# The goal is to find the right weights that will make the perceptron to predict the right output

def perceptronOutput(W,X):
    if np.dot(W,X) >= 0:
        return 1
    else:
        return -1
#  Initial set of weights      
W = [-0.6, 0.75, 0.5]