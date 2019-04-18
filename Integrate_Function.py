import math                       
import os
import time

def integrand(x):
    return x

def integrate(x_range_list):
    start = time.time()
    x_min = x_range_list[0]  
    x_max = x_range_list[1]
    n_boxes = x_range_list[2]
    
    delta_x = (x_max - x_min)/n_boxes
    
    sum = (-1/2)*delta_x*(integrand(x_min) + integrand(x_max))
    
    
    for i in range(n_boxes):
        sum = sum + integrand(x_min + i*delta_x)*delta_x
    end = time.time()
    print(f'\nTime to complete: {end - start:.2f}s\n')
    return sum


