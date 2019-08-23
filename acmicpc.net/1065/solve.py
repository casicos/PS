_input = int(input())

if _input < 100:
    print(_input)
else:
    counter = 99
    i: int
    for i in range(100, _input):
        a = i // 100 % 10
        b = i // 10 % 10
        c = i % 10

        if a - b is b - c:
            counter += 1

    print(counter)