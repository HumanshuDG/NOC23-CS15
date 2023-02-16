def remdup(l: list):
    duplicate = []
    for i in range(-1, -(len(l) + 1), -1):
        if l[i] not in duplicate:
            duplicate.append(l[i])
    duplicate.reverse()
    return duplicate

def splitsum(l: list):
    pass

def matrixflip(m, d):
    pass
