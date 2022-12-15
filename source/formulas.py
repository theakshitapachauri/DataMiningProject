import math

def sig(x):
    #use logistic function as activation function
    # raise Exception('Implement this part.')

    #it is always recommended to do Neural net calculations in float
    return (float(1) / float(1 + math.exp(-x)))

def inv_sig(x):
    #derivative of the output of neruon with respect to its input
    # raise Exception('Implement this part.')

    # derivative of logistic function
    return (sig(x) * (1-(sig(x)))) 

def err(o, t):
    #squared error function, o is the actual output value and t is the target output 
    # raise Exception('Implement this part.')

    #math.pow calculates the value of a base raised to a power
    error = 0.5 * (math.pow((t - o),2))
    return error


def inv_err(o, t):
    # o - pred_output, t- true output
    #derivative of squared error function with respect to o
    # raise Exception('Implement this part.')

    #if the logistic function is used as activation and square error as loss function, 
    # we get derivative of squared error function as:
    return (o - t)

    


