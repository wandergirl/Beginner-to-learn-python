"""
      通过文件操作将文件中的正式和测试两种类型中的测试筛出只留下正式
"""
fr =open("D:/bill.txt","r",encoding = 'utf-8') # 打开文件读取已存在的文件
fw =open("D:/bill_bak.txt","w",encoding="utf-8")# 打开文件准备写入
for line in fr:  # for循环遍历阅读文件
    line = line.strip() # 去除每一行的开头结尾换行符
    if line.split(",")[4] == "测试": # 这一行以","为分割符分割成列表，其中第四个列表等于测试时则跳过
        continue
    fw.write(line) # 将这行写入到bill_bak.txt文件中
    fw.write("\n")# 再写入换行符
fr.close() #关闭文件fr
fw.close() # 关闭文件fw
fr1 = open("D:/bill_bak.txt","r",encoding = 'utf-8') #打开文件fr1
print(fr1.read()) #将fr1读取到的内容输出出来
print("111")