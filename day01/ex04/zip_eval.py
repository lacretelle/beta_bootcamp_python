def evaluate(coefs, words):
    score = 0
    tmp = []
    for i in words:
        tmp.append(len(i))
    for a, val in enumerate(tmp):
        score += val * coefs[a]
    return score
