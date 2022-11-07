def solution(babbling):
    available_babbling : ["aya", "ye", "woo", "ma"]
    unavailable_babbling : ["ayaaya", "yeye", "woowoo", "mama"]
    for i in range(0, len(babbling)):
        for j in unavailable_babbling:
            if j in babbling[i] :
                del babbling[i]

    return