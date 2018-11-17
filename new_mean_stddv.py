def new_mean(mean , new_value , no_values ):

    return (mean + new_value) / (no_values + 1)

def new_std_dv(std_dv , mean , new_value , no_values):

    return std_dv + (new_value - mean) * (new_value - ( (mean + new_value) / (no_values + 1) ) )

mean = new_mean(mean , new_value , no_values )
std_dv = new_std_dv(std_dv , mean , new_value , no_values)

