k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

#x값의 증가에 따른 y값과, 적분 크기
point_y = []
area = []
while ( k > 1 ):
    point_y.append(k)
    if k % 2 == 0 :
        area.append(float(abs(k-k/2)/2 + k/2))
        k = k / 2
    elif k % 2 == 1 :
        area.append(float((abs((k * 3 + 1) - k) / 2 ) + k))
        k = k * 3 + 1

#(0,0)일때 전체값, area 리스트의 크기보다 ranges[0] - ranges[1]이 더 크다면 -1, 나머지는 정상출력
result = []
for i in ranges:
    if i == [0,0]:
        result.append(sum(area))
    elif len(area) + i[1] == i[0] + 1:
        result.append(0)
    elif len(area) + i[1] > i[0] + 1:
        result.append(-1)
    else:
        result.append(sum(area[i[0] : i[1]]))