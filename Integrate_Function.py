import math                       


def integrand(x):
    return x*x

def integrate(x_min, x_max, n_boxes):
    delta_x = (x_max - x_min)/n_boxes
    
    sum = (-1/2)*delta_x*(integrand(x_min) + integrand(x_max))
    
    
    for i in range(n_boxes):
        sum = sum + integrand(x_min + i*delta_x)*delta_x
        
    return sum


