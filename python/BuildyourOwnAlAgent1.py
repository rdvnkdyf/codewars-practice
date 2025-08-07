def next_states(s):
    results = []
    seen = set()

    def add_result(new_string):
        if new_string not in seen:
            results.append(new_string)
            seen.add(new_string)

    # Rule 1: xI -> xIU
    if s.endswith('I'):
        add_result(s + 'U')

    # Rule 2: Mx -> Mxx
    if s.startswith('M'):
        add_result(s + s[1:])

    # Rule 3: xIIIy -> xUy
    i = -1
    while True:
        i = s.find('III', i + 1)
        if i == -1:
            break
        add_result(s[:i] + 'U' + s[i+3:])

    # Rule 4: xUUy -> xy
    i = -1
    while True:
        i = s.find('UU', i + 1)
        if i == -1:
            break
        add_result(s[:i] + s[i+2:])
        
    return results