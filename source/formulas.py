import math

def sig(x):
    #use logistic function as activation function
    # raise Exception('Implement this part.')
    return (1.0/ float(1 + math.exp(-x)))

def inv_sig(x):
    #derivative of the output of neruon with respect to its input
    # raise Exception('Implement this part.')
    output = sig(x)
    return (output * (1-output)) 

def err(o, t):
    #squared error function, o is the actual output value and t is the target output 
    # raise Exception('Implement this part.')
    error = math.square(t - o)
    return error

def inv_err(o, t):
    # o - pred_output, t- true output
    #derivative of squared error function with respect to o
    # raise Exception('Implement this part.')
    return 2*(o-t)/t.size

    


