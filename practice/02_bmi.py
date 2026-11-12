def main():
    height = float(input("请输入你的身高(m)："))
    
    weight = float(input("请输入你的体重(kg)："))

    bmi =  weight / (height**2)

    if bmi < 18.5:
        print(f"你的BMI是{bmi:.1f},按照中国BMI的标准，你偏瘦。")
    elif bmi < 24:
        print(f"你的BMI是{bmi:.1f},按照中国BMI的标准，你正常。")
    elif bmi < 28:
        print(f"你的BMI是{bmi:.1f},按照中国BMI的标准，你超重。")
    else:
        print(f"你的BMI是{bmi:.1f},按照中国BMI的标准，你肥胖。")

if __name__ == "__main__":
    main()
    