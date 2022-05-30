import numpy as np
 
def calculate():
    
    data = ['1', '2', '3', '4', '7', '9', '10', '12', '15']
    
    if len(data) <9:
        raise ValueError("List must contain nine numbers.")
        
    data_new = np.array(data).reshape(3, 3)
    data_new = data_new.astype(int)
    # print(data_new)

    flattened_mean = np.mean(data_new).tolist()
    axis1_mean = np.mean(data_new, axis=0).tolist()
    axis2_mean = np.mean(data_new, axis=1).tolist()
    mean = [axis1_mean, axis2_mean, flattened_mean]
    # print(mean)

    flattened_variance = np.var(data_new).tolist()
    axis1_variance = np.var(data_new, axis=0).tolist()
    axis2_variance = np.var(data_new, axis=1).tolist()
    variance = [axis1_variance, axis2_variance, flattened_variance]
    # print(variance)

    flattened_standard_deviation = np.std(data_new).tolist()
    axis1_standard_deviation = np.std(data_new, axis=0).tolist()
    axis2_standard_deviation = np.std(data_new, axis=1).tolist()
    standard_deviation = [axis1_standard_deviation, axis2_standard_deviation, flattened_standard_deviation]
    # print(standard_deviation)

    flattened_max = data_new.max().tolist()
    axis1_max = data_new.max(axis=0).tolist()
    axis2_max = data_new.max(axis=1).tolist()
    max = [axis1_max, axis2_max, flattened_max]
    # print(max)

    flattened_min = data_new.min().tolist()
    axis1_min = data_new.min(axis=0).tolist()
    axis2_min = data_new.min(axis=1).tolist()
    min = [axis1_min, axis2_min, flattened_min]
    # print(min)

    flattened_sum = data_new.sum().tolist()
    axis1_sum = data_new.sum(axis=0).tolist()
    axis2_sum = data_new.sum(axis=1).tolist()
    sum = [axis1_sum, axis2_sum, flattened_sum]
    # print(sum)

    return ({
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max,
        'min': min,
        'sum': sum
    })

print(calculate())
