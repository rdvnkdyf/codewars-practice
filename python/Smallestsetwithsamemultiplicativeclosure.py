def smallest_set_with_same_closure(s):
    s = sorted(set(s))
    if 1 in s:
        s.remove(1)
        
    result = set()
    closure = {1}

    for val in s:
        # Eğer değer mevcut closure'dan elde edilebiliyorsa ekleme
        can_form = False
        to_check = {1}
        seen = set()

        while to_check:
            x = to_check.pop()
            if x == val:
                can_form = True
                break
            for r in result:
                y = x * r
                if y > val:
                    continue
                if y not in seen:
                    seen.add(y)
                    to_check.add(y)

        if not can_form:
            result.add(val)

    return result
