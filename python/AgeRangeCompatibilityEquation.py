def dating_range(age):
    if age <= 14:
        min_age = age - 0.10 * age
        max_age = age + 0.10 * age
    else:
        min_age = age / 2 + 7
        max_age = 2 * (age - 7)

    return f"{int(min_age)}-{int(max_age)}"