def probTest(limit):
    probYes = float(1)/6
    probNo = 1-probYes
    i = 1
    probFirstN = probYes
    while probFirstN > limit:
        print probFirstN
        i += 1
        probFirstN = probNo*probFirstN
    return i

print probTest(0.1)
