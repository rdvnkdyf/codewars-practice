def get_chance(n,x,a):
    prob=1.0
    for i in range(a):
        prob*=(n-x-i)/(n-i)
    
    return round(prob,2)