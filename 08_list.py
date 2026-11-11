def remove_dup(lst):    
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

def merge_two_list(a,b):
    res = []
    for i in a:
        res.append(i)
    for j in b:
        res.append(j)
    res.sort()
    return res

def read_numbers(prompt):
    raw = input(prompt)
    nums = []
    for p in raw.split():
        nums.append(int(p))
    return nums

def main():
    while True:
        print("1.去重保序 2.冒泡排序 3.合并两个有序列表 0.退出")
        choice = input("请选择")

        if choice == "0":
            print("已退出")
            break
        elif choice == "1":
            print(remove_dup(read_numbers("请输入你的列表：")))
        elif choice == "2":
            print(bubble_sort(read_numbers("请输入你的列表：")))
        elif choice == "3":
            a = read_numbers("请输入列表a：")
            b = read_numbers("请输入列表b：")
            print(merge_two_list(a, b))
        else:
            print("请输入0~3")

if __name__ == "__main__":
    main()
            

            
