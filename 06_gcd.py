def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    a = int(input("请输入a的值:"))
    b = int(input("请输入b的值:"))
    print(f"gcd({a},{b})={gcd(a, b)}")
    print(f"lcm({a},{b})={lcm(a, b)}")


if __name__ == "__main__":
    main()