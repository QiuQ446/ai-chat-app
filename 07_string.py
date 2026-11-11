def count_char(s):
    dic = {}
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def is_palindrome(s):
    
    return s == s[::-1]

def capitalize_word(s):
    words = s.split()
    result = []
    for w in words:
        result.append(w[0].upper() + w[1:])
    return " ".join(result)

def main():
    while True:
        print("1.字符统计 2.判断回文 3.首字母大写 0.退出")
        choice = input("请选择：")

        if choice not in ("0", "1", "2", "3"):
            print("只能输入 0~3")
            continue

        if choice == "0":
            print("已退出")
            break
        
        s = input("请输入字符")

        if choice == "1":
            print(count_char(s))
        elif choice == "2":
            if is_palindrome(s):
                print("是回文字符")
            else:
                print("不是回文字符")
        elif choice == "3":
            print(capitalize_word(s))
        



if __name__ == "__main__":
    main()
    


    