def range(min, max, step):
    sonlar = []
    while min < max:
        if step:
            sonlar.append(min)
            min += int(step)
        else:
            sonlar.append(min)
            min += 1
    return sonlar
print(range(0, 10, 2))
