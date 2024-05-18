def calculate(a, b, op):
    a, b = int(a), int(b)
    answer = None
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    elif op == "/":
        answer = a // b

    return answer


T = int(input())
for test_case in range(1, T + 1):
    datas = input().split()

    answer = None
    stack = []
    for data in datas:
        try:
            if data == ".":
                if len(stack) == 1:
                    answer = stack.pop()
                else:
                    answer = "error"
            elif data.isdecimal():
                stack.append(data)
            else:
                b = stack.pop()
                a = stack.pop()
                c = calculate(a, b, data)
                stack.append(str(c))
        except:
            answer = "error"
            break

    print(f"#{test_case} {answer}")
