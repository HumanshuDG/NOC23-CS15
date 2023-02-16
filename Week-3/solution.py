def remdup(l: list):
    duplicate = []
    for i in range(-1, -(len(l) + 1), -1):
        if l[i] not in duplicate:
            duplicate.append(l[i])
    duplicate.reverse()
    return duplicate

def splitsum(l: list):
    square_sum, cube_sum = 0, 0
    for num in l:
        if num >= 0:
            square_sum += num ** 2
        else:
            cube_sum += num ** 3
    return [square_sum, cube_sum]

def matrixflip(m, d):
    pass
