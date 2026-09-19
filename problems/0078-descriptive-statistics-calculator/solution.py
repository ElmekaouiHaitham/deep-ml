import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    # Sort the data
    data = sorted(data)
    n = len(data)

    # Mean
    mean = sum(data) / n

    # Median
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = float(data[n // 2])

    # Mode
    counts = {}
    for x in data:
        counts[x] = counts.get(x, 0) + 1

    mode = max(counts, key=counts.get)

    # Population variance
    variance = sum((x - mean) ** 2 for x in data) / n

    # Standard deviation
    standard_deviation = variance ** 0.5

    # Split data for quartiles
    if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
    else:
        # Include the median in BOTH halves
        lower_half = data[:n // 2 + 1]
        upper_half = data[n // 2:]

    # Q1
    m = len(lower_half)
    if m % 2 == 0:
        q1 = (lower_half[m // 2 - 1] + lower_half[m // 2]) / 2
    else:
        q1 = float(lower_half[m // 2])

    # Q3
    m = len(upper_half)
    if m % 2 == 0:
        q3 = (upper_half[m // 2 - 1] + upper_half[m // 2]) / 2
    else:
        q3 = float(upper_half[m // 2])

    # Interquartile range
    iqr = q3 - q1

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q1,
        "50th_percentile": median,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }