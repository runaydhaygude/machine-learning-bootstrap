
import numpy as np

# Here weights have be decided, the X (input from csv) will go as 
# as the sceond parameter to perceptronOutput (activation) function
# The goal is to find the right weights that will make the perceptron to predict the right output

# We initially randomly assign the weights, which will draw a line an divide the graph. 
# And pass the X1 and X2 values to compare the output of perceptronOutput with acutal supervised output. 
# If the output matches then it means the weights selected are correct
# If the output does not match then we need to adjust the weights (i.e. learn from the mistake) 
#  to fit the data correctly such that the output matches the supervised output
# The act of updating weights is "machine learning"

def perceptronOutput(W,X):
    if np.dot(W,X) >= 0:
        return 1
    else:
        return -1
#  Initial set of weights      
W = [-0.6, 0.75, 0.5]