def calculate(num1,num2,point):
    

    if point == "+":
        answer = num1 + num2

    elif point == "-":
        answer = num1 -num2

    elif point == "*":
        answer = num1 * num2

    elif point == "/":
        if num2 == 0:
            return None
        
        answer = num1 / num2

    else:
        return None
        

    return answer
if __name__ == "__main__":

    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    
    point = input("请输入符号：")
    
    result = calculate(num1, num2, point)
    if result is None:
        print("计算失败：除数不能为 0 或符号错误")
    else:
        print(f"{num1:g} {point} {num2:g} = {result:g}")