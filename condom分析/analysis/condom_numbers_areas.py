# -*- coding: utf-8 -*-
# @Time :    2021/12/6  13:44
# @Author :  Eleven
# @Site :    
# @File :    condom_numbers_areas.py
# @Software: PyCharm
import pandas as pd

PATH_ORG = '../condom_data/condom.xlsx'

def change_data():
    '''
    处理付款人数
    1.5万人付款  ->   15000
    6000+人付款  ->   6000
    '''
    #
    data = pd.read_excel(PATH_ORG)
    raw_sales = data['付款人数'].values
    #存放处理好的付款人数
    new_sales = []
    for sale in raw_sales:
        #将“人付款”后缀去除，只留下数字
        sale = sale[:-3]
        #将'+'替换为''
        sale = sale.replace('+','')
        #处理‘万’字，用数字替换
        if '万' in sale:
            sale = sale[:-1]
            #考虑小数点，如1.2万人
            if '.' in sale:
                sale = sale.replace('.', '') + '000'
            else:
                sale = sale + '0000'
        sale = int(sale)
        new_sales.append(sale)
    #赋值
    data['付款人数'] = new_sales

    '''
    处理地区名字，只保留省级名字
    江苏 苏州  ->  江苏
    '''
    raw_location =data['地区'].values
    new_location = []
    for location in raw_location:
        if ' ' in location:
            #只选择' '之前的数据保留
            location = location[:location.find(' ')]
        new_location.append(location)
    data['地区'] = new_location
    print(new_location)
    #保存到csv文件
    data.to_csv('./data/new_condom_data.csv',index=False)

if __name__ == '__main__':
    change_data()