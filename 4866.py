T = int(input())
for test_case in range(1, T + 1):
    command = input()
    stack = []

    answer = None
    for ch in command:
        if ch == "(" or ch == "{":
            stack.append(ch)
        if ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = 0
                break
        elif ch == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                answer = 0
                break

    if answer == None:
        if len(stack) == 0:
            answer = 1
        elif len(stack) > 0:
            answer = 0

    print(f"#{test_case} {answer}")
