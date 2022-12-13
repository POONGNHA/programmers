def solution(s):
    CntP = s.count('p') + s.count('P')
    CntY = s.count('y') + s.count('Y')
    if CntP - CntY == 0:
        return True;
    else :
        return False;
