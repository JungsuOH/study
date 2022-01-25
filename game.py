import random

# 수정하는 중
# 수정하는게 되는지 확인중입니다.
answer = random.randrange(1, 101)
print(answer)

count = 0

while(True):
    guess = int(input("정답을 추측해보세요 : "))
    count += 1

    if guess > answer:
        print("다운")
    elif guess < answer:
        print("업")
    elif guess == answer:
        break

print("축하합니다! 시도 횟수는 {}번 입니다.".format(count))
