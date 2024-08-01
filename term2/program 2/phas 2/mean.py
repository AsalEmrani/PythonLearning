def mean(data):     
    """
    Return the sample arithmetic mean of data.
     >>> mean([1, 2, 3, 4, 4])     2.8          
     If data is empty, StatisticsError will be raised.     
     """
    data = list(data)
    if len(data) == 0:
        raise StatisticsError('mean requires at least one data point')
    
    return sum(data) / len(data)
