def main():
    a = int(input("请输入最下值："))
    b = int(input("请输入最大值："))

    for i in range(a, b+1):
        s = i * i # 当前值的平方数
        k = i # 计算当期的值的位数
        b = 1 # 为了进行模运算

        while k > 0:
            k = k // 10
            b = b * 10
        
        c = s % b # 计算当前值的余数

        if i == c:
            print("{}^2 = {}".format(i,s))

if __name__ == "__main__":main()