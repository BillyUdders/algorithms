def sequence(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c


if __name__ == '__main__':
    for n, z in enumerate(sequence(c=1)):
        print(f"z({n}) = {z}")
        if n >= 9:
            break
