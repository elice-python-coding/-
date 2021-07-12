# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin #금액에서 coin으로 나누는 몫을 count에 저장
    n %= coin #나머지를 금액에 저장
print(count)
