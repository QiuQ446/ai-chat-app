import os

def save_record(path,amount,note):
    with open(path,"a",encoding="utf-8")as f:
        f.write(f"{amount},{note}\n")

def load_records(path):
    if not os.path.exists(path):
        return []

    records = []

    with open(path,"r",encoding="utf-8")as f:
        for n,line in enumerate(f,1):
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                print(f"第 {n} 行格式有问题，已跳过")
                continue

            try:
                amount = float(parts[0])
            except ValueError:
                print(f"第 {n} 行金额不是数字，已跳过")
                continue
            records.append({
                "amount":amount,
                "note":parts[1],
            
            })
        return records

def main():
    path = "records.txt"

    while True:
        print("\n1.添加  2.查看  3.统计  0.退出")
        choice = input("请选择：")

        if choice == "0":
            break
        
        elif choice == "1":
            count = 0
            while True:
                try:
                    amount = float(input("金额："))
                    break
                except ValueError:
                    print("请输入正确的金额数量")
                    count += 1
                    if count == 3:
                        print("你已经输错3次金额，默认你放弃这一笔")
                        break
            if count != 3:                
                note = input("备注：")
                save_record(path,amount,note)
                print("已保存")
                
        
        elif choice == "2":
            records = load_records(path)
            if not records:
                print("还没记录")
                continue
            for i,r in enumerate(records,1):
                 print(f"{i},{r['amount']} {r['note']}")
                
        elif choice == "3":
            records = load_records(path)
            total = 0
            for r in records:
                total += r["amount"]
            print(f"共{len(records)}笔,合计{total:.2f}")

        else:
            print("请输入0~3")
                
if __name__ == "__main__":
    main()


