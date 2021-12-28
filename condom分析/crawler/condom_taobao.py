# -*- coding: utf-8 -*-
# @Time :    2021/12/4  16:08
# @Author :  Eleven
# @Site :    
# @File :    test01.py
# @Software: PyCharm
import re
import  requests
import xlsxwriter
import  time

def Get_intoExcel(html):
    global count
    #查看源码找到对应数据的标题
    a = re.findall(r'"raw_title":"(.*?)"', html)
    b = re.findall(r'"view_price":"(.*?)"', html)
    c = re.findall(r'"item_loc":"(.*?)"', html)
    d = re.findall(r'"view_sales":"(.*?)"', html)
    x = []
    #循环添加
    for i in range(len(a)):
        try:
            x.append((a[i],b[i],c[i],d[i]))
        except IndexError:
            break
    i = 0
    #写入格式的对应
    for i in range(len(x)):
        worksheet.write(count + i + 1, 0, x[i][0])
        worksheet.write(count + i + 1, 1, x[i][1])
        worksheet.write(count + i + 1, 2, x[i][2])
        worksheet.write(count + i + 1, 3, x[i][3])
    count = count +len(x)#下次写入的行数是这次的长度+1

#获取搜索数据的url
def Geturls(q, x):
    url = "https://s.taobao.com/search?q=" + q + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm" \
                                                 "=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306 "
    urls = []
    urls.append(url)
    #判断爬取页数
    if x == 1:
        return urls
    for i in range(1, x):
        url = "https://s.taobao.com/search?q="+ q + "&commend=all&ssid=s5-e&search_type=item" \
                                                    "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306" \
                                                    "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(i * 44)#乘44是因为页面变化是44的倍数
        urls.append(url)
    return urls

#获取html数据
def GetHtml(url):
    r = requests.get(url,headers =headers)
    r.raise_for_status()#判断状态200/404
    r.encoding = r.apparent_encoding
    return r

if __name__ == "__main__":
    count = 0
    #头文件
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ,"cookie":"cna=sjcWGhywZ1gCAWpVTtHcR1U0; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=E100nrEULpex7G67h%2FsrCkjRjbX8dp4gdyZpQLf4SCJzr6mY%2BoId4XndrN1w0Y76k0T7D8vk8vhCEOmt3ioG4L4eXz%2FZnrt%2BZIJ%2BoR0gGfg4L0w%3D; uc3=id2=UNN%2BxywbWY3%2Big%3D%3D&vt3=F8dCvUj48Dv8WV7Gx58%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D; uc4=id4=0%40UgQ2gbehJFA8tC%2BRmm4nls2UIh33&nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKmqEBpALIZ; _cc_=URm48syIZQ%3D%3D; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; mt=ci=-1_0; cookie2=1dee91c6b379cf5b1beecffb28f5e592; t=b8a7d834ecf92000456345bdec65ec54; _tb_token_=331e5e3877ee8; xlly_s=1; _samesite_flag_=true; _m_h5_tk=505dd6a76fc41d772e689009a4d24c1e_1638617273627; _m_h5_tk_enc=1d5b220b0041bab3b1e32482a60431a0; uc1=cookie14=Uoe3f4Y%2Bw92rPg%3D%3D; tfstk=cdThBQvWZHSIPljMc2_B6qRZ2ioOZwzPnU867EoiSZn1oM8Nieqa0-BSs9DjLu1..; l=eBOQYmJ4gpCHlLuaBOfZourza779SIRf_uPzaNbMiOCP_Yfp5fDCW6IGaFT9CnGVHsmDR3uQQyaYBxLFNyCq0-Y3LAaZk_Do3dC..; isg=BJOTzusr9hH8eLp9uanWixEqIhe9SCcKobsxYUWwJ7LpxLJmzBlYWpJS_jSq438C"
    }
    q = input("输入商品名称：")
    x = int(input("输入爬取页数："))
    urls = Geturls(q,x)
    workbook = xlsxwriter.Workbook("../crawler_data/"+q+".xlsx")
    #基于xlsxwrite的写入操作
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.write('A1', '名称')
    worksheet.write('B1', '价格')
    worksheet.write('C1', '地区')
    worksheet.write('D1', '付款人数')
    #for循环写入
    for (i,url) in zip(range(1,len(urls)+1),urls):
        html = GetHtml(url)
        s = Get_intoExcel(html.text)
        print("第%s页写入成功！"%i)
        #sleep是必要的，防止被认为是爬虫
        time.sleep(5)
    workbook.close()
