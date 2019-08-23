_input = int(input())

if _input < 100:
    print(_input)
else:
    counter = 99
    i: int
    for i in range(100, _input + 1):
        a = i // 100
        b = (i % 100) // 10
        c = (i % 10)

        if a - b is b - c:
            counter += 1

    print(counter)