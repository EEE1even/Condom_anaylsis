# -*- coding: utf-8 -*-
# @Time :    2021/12/4  16:29
# @Author :  Eleven
# @Site :    
# @File :    comment_deal.py
# @Software: PyCharm
import jieba
from collections import Counter
import codecs
import xlsxwriter

#商品信息追评文件路径
D_thin = '../crawler_data/durex_thin.txt'
D_air = '../crawler_data/durex_air.txt'
D_lasting = '../crawler_data/durex_lasting.txt'
O_001 = '../crawler_data/okamoto_001.txt'
O_lasting = '../crawler_data/okamoto_lasting.txt'
J = '../crawler_data/jissbon_001lasting.txt'
Siki = '../crawler_data/siki.txt'


def jieba_text(PATH,name):
    '''

    :param PATH: 路径
    :param temp: 文件命名
    :return:
    '''
    with codecs.open(PATH, 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt,name)

def get_words(text,name):
    '''
    获取词组对应词频，写入excel表
    '''
    seg_list = jieba.cut(text)
    c = Counter()
    for x in seg_list:
        if len(x) > 1and x != '\r\n':
            c[x] += 1

    workbook = xlsxwriter.Workbook("../jieba_data/"+name+".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.write('A1', '词组')
    worksheet.write('B1', '频率')

    #most_common为统计结果列表，我们输出前一百个
    for i,(k,v) in zip(range(50),c.most_common(50)):

        # print('%s  %d' % (k, v))
        #将前50个词频写入excel表中
        worksheet.write('A%s'%(i+2),k)
        worksheet.write('B%s'%(i+2),v)
    workbook.close()
    return print('%s写入成功！'%name)

if __name__ == '__main__':
    #关闭日志,防止报出警告
    jieba.setLogLevel(jieba.logging.INFO)
    #调用函数写入数据
    jieba_text(D_thin,'D_thin')
    jieba_text(D_lasting,'D_lasting')
    jieba_text(D_air,'D_air')
    jieba_text(O_001,'O_001')
    jieba_text(O_lasting,'O_lasting')
    jieba_text(J,'J')
    jieba_text(Siki,'Siki')