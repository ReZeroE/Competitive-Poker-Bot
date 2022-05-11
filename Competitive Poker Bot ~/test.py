import os
import sys

cc = []
rourou = []
ct = 0

while True:
    ct += 1
    poker_list = []
    for i in range(1, 14):
        poker_list.append(i)
        poker_list.append(i)
        poker_list.append(i)
        poker_list.append(i)
    # joker
    poker_list.append(14)
    poker_list.append(15)

    print(len(poker_list))

    # random pick
    import random
    cc = random.choices(poker_list, k = 27)
    for element in cc:
        if element in poker_list:
            poker_list.remove(element)
    rourou = poker_list

    if abs(sum(rourou) - sum(cc)) <= 3:
        break

print(cc)
print(rourou)
print(f"count: {ct}")
