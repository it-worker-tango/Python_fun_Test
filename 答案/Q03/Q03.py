'''
考拉兹猜想：
对自然数n 循环执行如下操作。
·n 是偶数时，用n 除以2
·n 是奇数时，用n 乘以3 后加1
如此循环操作的话，无论初始值是什么数字，
最终都会得到1（会进入1 → 4 → 2 → 1 这个循环）
------------------------------------------
问题：求在小于10000 的偶数中，
符合考拉兹猜想这样“能回到初始值的数”有多少个。并打印出来。
'''
def is_loop(n):
    '''判断是否符合条件'''
    check = n * 3 + 1 # 本题为改版，第一次都乘以3然后加1
    while check != 1: # 判断是否回到了1
        if check % 2 == 0: # 判断是否为偶数
            check = check // 2 # 这里因为不需要小数，所以用//
        else:
            check = check * 3 + 1
        
        if check == n: # 判断是否和初始值相等
            return True
    return False # 不符合条件

if __name__ == "__main__":
    num_list = [] # 定义一个用来保存结果的列表
    for i in range(2, 10000, 2): # 因为判断的是偶数，所以从2开始，每次加2
        if is_loop(i): # 符合猜想
            num_list.append(i)

    print("符合猜想的共有{}个".format(len(num_list)))
    for n in num_list:
        print(n)





