"""
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
...
[] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
"""

# 내 답안
from random import *

passenger = {}
count = 0

for i in range(1, 51):
    passenger[i] = randint(5, 51)

    if 5 <= passenger[i] <= 15:
        print("[{}] {}번째 손님 (소요시간 : {}분)".format("o", i, passenger[i]))
        count += 1
    else:
        print("[{}] {}번째 손님 (소요시간 : {}분)".format("", i, passenger[i]))

print("총 탑승 승객 : {}".format(count))

# 나도코딩 답안
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {}번째 손님 (소요시간 : {}분)".format(i, passenger[i]))
        cnt += 1
    else:
        print("[] {}번째 손님 (소요시간 : {}분)".format(i, passenger[i]))

print("총 탑승 승객 : {}".format(cnt))