from Integrate_Function import integrate
import multiprocessing
import time

#https://www.youtube.com/watch?v=aysceqdGFw8 
#for reference to the pool idea

def Get_X_Ranges(x_min, x_max, boxes_per_core):
    
    cores = multiprocessing.cpu_count()
    print(cores)
    mini = x_min
    maxi = x_max
    boxes = boxes_per_core
    
    x_range_per_core = (x_max-x_min)/cores
    x_ranges = []
    
    for x in range(cores): 
        a_cores_range = []
        
        a_cores_range.append(mini)
        mini = mini + x_range_per_core
        a_cores_range.append(mini)
        a_cores_range.append(boxes)
        x_ranges.append(a_cores_range)
        
        
        
    return x_ranges








def parallel_integrate(x_min,x_max,boxes_per_core):
    threads = multiprocessing.cpu_count()
    
    x_ranges = Get_X_Ranges(x_min, x_max, boxes_per_core)
    
    pool = multiprocessing.Pool(threads)
    result = list(pool.map(integrate, x_ranges))
    
    addition = 0.0
    for x in range(len(result)):
        addition = addition + result[x]
        
    
    return addition    






    