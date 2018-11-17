from math import *

def new_mean(mean , new_value , no_values ):

    return (no_values * mean + new_value) / (no_values + 1)

def new_std_dv(std_dv , mean , new_value , no_values):

        V = no_values * (std_dv)**2 + (new_value - mean) * (new_value - ( (no_values * mean + new_value) / (no_values + 1) ) )

        return sqrt( V / (no_values + 1))

mean = new_mean(mean , new_value , no_values )
std_dv = new_std_dv(std_dv , mean , new_value , no_values)

