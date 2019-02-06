'''
一个n(n>=3)位正整数，
如果等于它的n个数的n次幂之和，
那么这个数就是n位的兰德尔数，
又称自次幂数。
'''

def main(start_num, x):
    for i in range(start_num,start_num * 10):
        temp = list(str(i))
        temp_num = x-1
        count_num = 0
        while temp_num >=0:
            count_num += int(temp[temp_num]) ** x
            temp_num -=1 # temp_num = temp_num -1
        #temp_count = int(temp[0]) ** x + int(temp[1]) ** x + int(temp[2]) ** x
        if i == count_num:
            print(i)
        #print("{}的百位数：{},十位数{},个位数{}".format(i,i // 100, i % 100 // 10, i % 10))

def strt():
    j = 1
    for i in range(3, 9):
        k = j * 100
        j *= 10
        print("-------------------",i,"位-------------------")
        main(k, i)




if __name__ == "__main__":strt()