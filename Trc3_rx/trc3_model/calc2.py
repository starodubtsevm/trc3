def calc(sample, _data, size, index, h):

    if len(_data) == size:
        _data[index] = sample
    else:
        _data.append(sample)
        index = (index + 1) % size
    acc = 0  # accumulator
    indx = index
    for j in (len(size)):
        acc += _data[indx] * h[j]
        if indx == ((size) - 1):
            indx = 0
        else:
            indx += 1
    return (int(acc) / 32768)  # result to 16 bit value
