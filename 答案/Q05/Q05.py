'''
从键盘输入整数a,b(a<b),
 寻求满足勾股的整数，
 x,y,z的组合。
'''
import math # 导入第三方库

def main():
    a = int(input("请输入最小值：")) # 获取用户输入，并转换成int类型
    b = int(input("请输入最大值："))

    for x in range(a,b+1):
        for y in range(x+1, b+1):
            #d = x * x + y * y # d = x ** 2 + y**2 
            d = x ** 2 + y**2 
            z = int(math.sqrt(d)) # 求d得开平方

            if z <=b and z * z == d:
                print("{}^2 + {}^2 = {} = {}^2".format(x,y,d,z))

if __name__ == "__main__":main()
