'''
求用十进制，二进制，八进制
表示都是回文数的所有数字中，
大于十进制20的最小值。
'''
# 1 回顾Python的进制转换
num = 9
print('num的二进制:',bin(num))
print('num的八进制:',oct(num))
# 2 回顾字符串的切片反转
my_str = "ABCDEFG"
print("my_str反转后：",my_str[::-1])

def hw():
    '''
    取得比20大的最小回文数
    '''
    num = 21 # 因为要取得比20大的数
    while True: #因为不知道是多少，所以用了循环
        num_str_10 = str(num) # 将十进制转换成字符串
        num_str_2 = str(bin(num)) # 先将十进制转换成二进制，再转换成字符串
        num_str_8 = str(oct(num)) # 将八进制的数转换成字符串
        num_str_2 = num_str_2.replace('0b','') # 因为Python中二进制前面会用0b表示，我们需要将他去掉
        num_str_8 = num_str_8.replace('0o','') # 八进制则是以0o开头，同样要去掉
        if (num_str_10==num_str_10[::-1]) and (num_str_2==num_str_2[::-1]) and (num_str_8==num_str_8[::-1]):
            '''
            将每个进制的数和其反转后的结果进行比较
            '''
            print("大于20的最小的回文数：", num)
            print('二进制为:',num_str_2)
            print('八进制为:',num_str_8)
            break # 结束循环
        num += 2 # 因为是奇数，所以每次加2

if __name__ == "__main__":hw()
