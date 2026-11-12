def main():
    number1 = float(input("输入你的第1个数字："))
    number2 = float(input("输入你的第2个数字："))
    point = input("输入符号：")

    if point == "+":
        answer = number1 + number2
    
    elif point == "-":
            answer = number1 - number2

    elif point == "*":
            answer = number1 * number2

    elif point == "/":
            if number2 == 0:
                print("除数不能为0")
                return            
            answer = number1 / number2

    else:
        print("符号错误，只能输入+ — * /")
        return
    print(answer)

if __name__ == "__main__":
    main()