# -*- coding: utf-8 -*-
# @Time :    2021/12/7  20:01
# @Author :  Eleven
# @Site :    
# @File :    message_deal.py
# @Software: PyCharm
import jieba
from collections import Counter
import pandas as pd
import xlsxwriter

PATH = '../crawler_data/condom.xlsx'

def message_deal():
    phrase = []
    #求词频用的
    c = Counter()
    data = pd.read_excel(PATH)
    #转换成列表形式
    data = list(data['名称'])
    #循环读取，将数据加入phrase列表
    for i in data:
        tmp = jieba.cut(i)
        #获取的tmp是一个地址，需要通过循环才能获取数据
        for j in tmp:
            phrase.append(j)
    #统计词频
    for x in phrase:
        #判断词组长度，标点符号不计入
        if len(x) > 1:
            #将词组x传入Counter，统计个数
            c[x] += 1
    workbook = xlsxwriter.Workbook("../jieba_data/condom_message.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.write('A1', '词组')
    worksheet.write('B1', '频率')
    #写入数据
    for i,(k,v) in zip(range(70),c.most_common(70)):
        # print('%s  %d' % (k, v))
        worksheet.write('A%s'%(i+2),k)
        worksheet.write('B%s'%(i+2),v)
    workbook.close()
    return print('写入成功！')

if __name__ == '__main__':
    #关闭日志,防止报出警告
    jieba.setLogLevel(jieba.logging.INFO)
    message_deal()