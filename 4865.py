from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    str1_set = set(str1)
    dict = defaultdict(int)
    for ch in str2:
        if ch in str1_set:
            dict[ch] += 1
    ch_counts = list(dict.items())
    ch_counts.sort(key=lambda x: x[1], reverse=True)

    print(f"#{test_case} {ch_counts[0][1]}")