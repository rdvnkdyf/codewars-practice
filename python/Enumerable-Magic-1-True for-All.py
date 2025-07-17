def _all(seq, fun): 
    # your code here
    return all(fun(item) for item in seq)