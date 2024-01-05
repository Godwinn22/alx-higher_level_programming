def magic_calculation(a, b):
    import magic_calculation_102 as m
    if a < b:
        c = m.add(a, b)
        for i in range(4, 6):
            c = m.add(c, i)
        return c
    else:
        return m.sub(a, b)