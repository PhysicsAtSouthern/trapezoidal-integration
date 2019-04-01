from Integrate_Function import integrate
import multiprocessing 



def parallel_integrate(x_min,x_max,boxes_per_core):
    
    cores = multiprocessing.cpu_count()
    
    x_range_per_core = (x_max-x_min)/cores
    x_ranges = []
    
    for x in range(cores): 
        a_cores_range = []
        a_cores_range.append(x_min)
        x_min = x_min + x_range_per_core
        a_cores_range.append(x_min)
        x_ranges.append(a_cores_range)
        print(x_ranges)
        
    return x_ranges



def add(x):
    return x[0]+x[1]

def test_map():
    LIST = [[1,2],[3,4],[5,6]]
    result = map(add,LIST)
    return result
    
    