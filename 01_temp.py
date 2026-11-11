def c_to_f():
    celsius = float(input("请输入摄氏度:"))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"华氏度是{fahrenheit:.1f}°F")

def f_to_c():
    fahrenheit = float(input("请输入华氏度："))
    celsius = (fahrenheit-32) * 5 / 9
    print(f"摄氏度是{celsius:.1f}°C")



if __name__ == "__main__":
    print("输入 1 → 摄氏度转华氏度,输入 2 → 华氏度转摄氏度")
    tip = int(input())
    if tip == 1:
        c_to_f()

    elif tip == 2:
         f_to_c()        

    else:
        print("只能输入 1 或 2")

        