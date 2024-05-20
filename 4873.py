# import time

def findContinuousChar(s):
    for i in range(0, len(s) - 2 + 1):
        if s[i] == s[i+1]:
            return i
    return None

T = int(input())
for test_case in range(1, T + 1):
    s = input()


    # while findContinuousChar(s) != None:
    #     index = findContinuousChar(s)
    #     s = s[:index] + s[index+2:]

    # while 1:
    #     out = findContinuousChar(s) # n
    #     if out == None:
    #         break
    #     s = s[:out] + s[out+2:] # n

    # start = time.time()
    stack = []
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        elif len(stack) > 0:
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
    # end = time.time()

    # print(f"{(end-start)*1000:.5f}")
    # print(f"#{test_case} {len(s)}")
    print(f"#{test_case} {len(stack)}")
