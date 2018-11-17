from math import  sqrt

def new_mean(m , value , no_values ):

    return (no_values * m + value) / (no_values + 1)

def new_std_dv(std_dv , m , value , no_values):

    Sx = (no_values - 1)* std_dv **2 + ( value - m) * (value - (no_values * m + value) / (no_values + 1) )
    V = Sx/(no_values)

    return sqrt( V)


