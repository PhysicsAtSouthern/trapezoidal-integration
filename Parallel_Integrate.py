from Integrate_Function import integrate
import multiprocessing



def Get_X_Ranges(x_min, x_max, boxes_per_core):
    
    cores = multiprocessing.cpu_count()
    
    x_range_per_core = (x_max-x_min)/cores
    x_ranges = []
    
    for x in range(cores): 
        a_cores_range = []
        a_cores_range.append(x_min)
        x_min = x_min + x_range_per_core
        a_cores_range.append(x_min)
        a_cores_range.append(boxes_per_core)
        x_ranges.append(a_cores_range)
        
        print(x_ranges)
        
    return x_ranges








def parallel_integrate(x_min,x_max,boxes_per_core):
    cores = multiprocessing.cpu_count()
    x_ranges = Get_X_Ranges(x_min, x_max, boxes_per_core)
    pool = multiprocessing.Pool(cores)
    result = list(pool.map(integrate, x_ranges))
    
    print(result)
    addition = 0.0
    for x in range(len(result)):
        addition = addition + result[x]
    return addition    






    