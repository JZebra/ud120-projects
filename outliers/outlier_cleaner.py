#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Params
        predictions- array. predicted net worth
        ages- array. list of ages of training set
        net_worths- array. actual net worth

        Assumes that all params are the same length

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).

    """
    
    cleaned_data = []

    ### your code goes here

    retain_percent = 0.9
    num_points = len(predictions)
    retain_num = int(retain_percent * num_points)
    
    data = []
    for i in xrange(num_points):
        error = (net_worths[i] - predictions[i]) ** 2
        datum = tuple([ages[i][0], net_worths[i][0], error[0]])
        data.append(datum)


    sorted_data = sorted(data, key=lambda x: x[2])
    cleaned_data = sorted_data[:retain_num]

    return cleaned_data

