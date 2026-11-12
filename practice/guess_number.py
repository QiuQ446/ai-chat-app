import random

def main():
    answer =  random.randint(1,100)
    tries = 0
    print("我想了一个 1-100 的整数，你猜猜看～") 

    while True:
        raw = input("请输入你猜的数字：")
        tries += 1

        try:
            guess = int(raw)
        except ValueError:
            print("这不是数字哦，再试一次")
            continue
        if guess < answer:
            print("小了")
        elif guess > answer:
            print("大了")
        else:
            print(f"猜对啦，答案是{answer},你一共用了{tries}次")

if __name__ == "__main__":
    main()