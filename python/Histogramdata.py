def histogram(values, bin_width):
    if not values:
        return []

    max_value = max(values)
    
    num_bins = (max_value // bin_width) + 1
    
    bins = [0] * num_bins

    for value in values:
        bin_index = value // bin_width
        bins[bin_index] += 1
    
    return bins