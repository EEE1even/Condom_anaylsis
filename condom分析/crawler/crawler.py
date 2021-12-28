# -*- coding: utf-8 -*-
# @Time :    2021/10/25  17:35
# @Author :  Eleven
# @Site :    
# @File :    crawler.py
# @Software: PyCharm
#导入需要的库
import random

import requests
import time
import re
#ip池
# proxies = {'http':'182.138.139.128:7890',
#            'https':'59.37.18.243:3128'
#            }

#杜蕾斯焕金超薄
def durex_thin(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=37475960084&spuId=1946452586&sellerId=1986899349&order=3&currentPage='
    urllast = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvdvvovZ9vUvCkvvvvvjiWPsLZtj3CnLF90jD2PmPwgj3CPLzvsjEbPFzOQj1h9vhv8cafmP%2FCzHi47edozAcjdbSRStUF4KefA%2BuMoMImII0oFtn1IpnkyI%2FLRvhvChCvvvmvvpvW7Dr9M0jw7Di4OFqN9vhv2HifhP%2FmzHi47Dz6zgOCvvBvppvvi9hvChCvCCpgvpvhphvvvvvCvvXvppvvvvmgvpvIphvvvvvvphCvpvBzvvC2gyCvjvUvvhBGphvwv9vvBh1vpCQmvvChL89Cvv3vpvLlQ739hU9CvvXmp99h5C%2BUvpCWpOXGv8ROwDg0747BhC3qVmHoDOvXecIUExjxALwp8BpDNr1ljdUf836s%2BXZz%2BsBwN6qhQCu4JytQoWkQRqwiL7CpYNZZReQ2flzpGpgCvvpvvPMMdvhvmZCC3v1svhCCv8QCvvDvpo9pF9Cvpehgvpvhphvvv8QCvvDvpL9pe9CvBAOgvpvhphvvvv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638593999171_1357&callback=jsonp1358'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=37475960084&spuId=1946452586&sellerId=1986899349&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvdvvovZ9vUvCkvvvvvjiWPsLZtj3CnLF90jD2PmPwgj3CPLzvsjEbPFzOQj1h9vhv8cafmP%2FCzHi47edozAcjdbSRStUF4KefA%2BuMoMImII0oFtn1IpnkyI%2FLRvhvChCvvvmvvpvW7Dr9M0jw7Di4OFqN9vhv2HifhP%2FmzHi47Dz6zgOCvvBvppvvi9hvChCvCCpgvpvhphvvvvvCvvXvppvvvvmgvpvIphvvvvvvphCvpvBzvvC2gyCvjvUvvhBGphvwv9vvBh1vpCQmvvChL89Cvv3vpvLlQ739hU9CvvXmp99h5C%2BUvpCWpOXGv8ROwDg0747BhC3qVmHoDOvXecIUExjxALwp8BpDNr1ljdUf836s%2BXZz%2BsBwN6qhQCu4JytQoWkQRqwiL7CpYNZZReQ2flzpGpgCvvpvvPMMdvhvmZCC3v1svhCCv8QCvvDvpo9pF9Cvpehgvpvhphvvv8QCvvDvpL9pe9CvBAOgvpvhphvvvv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638593999171_1357&callback=jsonp1358',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; xlly_s=1; sgcookie=E100nrEULpex7G67h%2FsrCkjRjbX8dp4gdyZpQLf4SCJzr6mY%2BoId4XndrN1w0Y76k0T7D8vk8vhCEOmt3ioG4L4eXz%2FZnrt%2BZIJ%2BoR0gGfg4L0w%3D; uc1=cookie14=Uoe3f4US%2FMOa1Q%3D%3D; uc3=id2=UNN%2BxywbWY3%2Big%3D%3D&vt3=F8dCvUj48Dv8WV7Gx58%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D; t=b8a7d834ecf92000456345bdec65ec54; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=id4=0%40UgQ2gbehJFA8tC%2BRmm4nls2UIh33&nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKmqEBpALIZ; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; _tb_token_=331e5e3877ee8; cookie2=1dee91c6b379cf5b1beecffb28f5e592; _m_h5_tk=2443a2e120930625cf52018332906920_1638601167356; _m_h5_tk_enc=ac0dd2e29588c286f7ef7543064cf439; tfstk=cTOCBpjsqkqBudkzTega8D8VTxCOZ9afPvsHRLdoEdnZk9YCitVVcQvMEuCPyN1..; l=eBLwFerIg2dIF8ovBO5aKurza77OyIdfGrVzaNbMiInca6_dGeTCENCdbJV2PdtjgtfxaeKrRRzQkRU6-P4T5E_ceTwhKXIpBRvw-; isg=BMDAsM5VtSkD0kkYszmXWk1OkU6SSaQTBkqiSDpQPlt3tWTf41hyoQvDzR11A1zr',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16179729556.49.18e1628a8dvMr3&id=37475960084&rn=c8a8a7d28d59eb192111fa8f86007657&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }

        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text

        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(8,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/durex_thin.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

#杜蕾斯延时持久
def durex_lasting(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=37452863348&spuId=1970086832&sellerId=1986899349&order=3&currentPage='
    urllast  = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvgvvXvwWvUvCkvvvvvjiWPsLZtjimP2Sp0jEUPmP9Aj1HR2cy6jDbPLMOzjtURvhvCvvvphm%2BvpvEvU25givvvCNudvhvmpmvei%2Fgvvvcd4QCvChhvxHZZvvvDShDj6KHkoVQR4QCvvyvvwLvEQvvDd6gvpvhvvCvpUvCvCB47gyvcr147DiqzRNGvHAu7K2No8QCvCoH9vvhyQvvhnODj6AH%2Bf83rqOkL4QCvvyvvo%2BSp9vvF%2Fm%2BvpvEvUCGJLvvvUzfdvhvhpovFIKIvvvnXoZNog7EUfvtC9hvmx14zYMwcRSjAs9CvvpvvhCvmvhvLUVahBhaeByKK33sHix1K3kXWzwdlwmXWsUKnpcWyfUKK33sHXH1K3kXWzUKlwmXWtIKnpcWefhBHdUf8zc6hBh7%2B3%2B%2BaNpOHdoJayJIvpvUvvCCPvTTzzJUvpvVvpCmp%2FLOKvhv8vvvphvvvvvvvvCj1Qvv9avvvhNjvvvmjvvvBGwvvvUhvvCj1Qvvv9pvvpvVvUCvpvvv29hvCvvvMM%2FevpvhvvCCBUOCvvpv9hCvRvhvCvvvphm%2BvpvEvUvRmigvvCv9dvhvmpmvajHpvvmpjUvCvmDz71vvhn147DuWqrGD1TAqsd%2FoU0dieGd8S6STvu8nyI%2FLOX5kQITpFv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638591820578_1264&callback=jsonp1265'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=37452863348&spuId=1970086832&sellerId=1986899349&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvgvvXvwWvUvCkvvvvvjiWPsLZtjimP2Sp0jEUPmP9Aj1HR2cy6jDbPLMOzjtURvhvCvvvphm%2BvpvEvU25givvvCNudvhvmpmvei%2Fgvvvcd4QCvChhvxHZZvvvDShDj6KHkoVQR4QCvvyvvwLvEQvvDd6gvpvhvvCvpUvCvCB47gyvcr147DiqzRNGvHAu7K2No8QCvCoH9vvhyQvvhnODj6AH%2Bf83rqOkL4QCvvyvvo%2BSp9vvF%2Fm%2BvpvEvUCGJLvvvUzfdvhvhpovFIKIvvvnXoZNog7EUfvtC9hvmx14zYMwcRSjAs9CvvpvvhCvmvhvLUVahBhaeByKK33sHix1K3kXWzwdlwmXWsUKnpcWyfUKK33sHXH1K3kXWzUKlwmXWtIKnpcWefhBHdUf8zc6hBh7%2B3%2B%2BaNpOHdoJayJIvpvUvvCCPvTTzzJUvpvVvpCmp%2FLOKvhv8vvvphvvvvvvvvCj1Qvv9avvvhNjvvvmjvvvBGwvvvUhvvCj1Qvvv9pvvpvVvUCvpvvv29hvCvvvMM%2FevpvhvvCCBUOCvvpv9hCvRvhvCvvvphm%2BvpvEvUvRmigvvCv9dvhvmpmvajHpvvmpjUvCvmDz71vvhn147DuWqrGD1TAqsd%2FoU0dieGd8S6STvu8nyI%2FLOX5kQITpFv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638591820578_1264&callback=jsonp1265',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; xlly_s=1; sgcookie=E100nrEULpex7G67h%2FsrCkjRjbX8dp4gdyZpQLf4SCJzr6mY%2BoId4XndrN1w0Y76k0T7D8vk8vhCEOmt3ioG4L4eXz%2FZnrt%2BZIJ%2BoR0gGfg4L0w%3D; uc1=cookie14=Uoe3f4US%2FMOa1Q%3D%3D; uc3=id2=UNN%2BxywbWY3%2Big%3D%3D&vt3=F8dCvUj48Dv8WV7Gx58%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D; t=b8a7d834ecf92000456345bdec65ec54; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=id4=0%40UgQ2gbehJFA8tC%2BRmm4nls2UIh33&nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKmqEBpALIZ; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; _tb_token_=331e5e3877ee8; cookie2=1dee91c6b379cf5b1beecffb28f5e592; _m_h5_tk=2443a2e120930625cf52018332906920_1638601167356; _m_h5_tk_enc=ac0dd2e29588c286f7ef7543064cf439; tfstk=cFjNBPZhilEaNsxbyht45MWoZ-eOZvBGnDJWSNkTD9DmzaYGi-cvKmp6LKMEiFf..; l=eBLwFerIg2dIFsXNBO5Bnurza779gQObzrVzaNbMiInca6tFGelx3NCdb7AXPdtjgt5AzeKrRRzQkRU9-j4T5E_ceTwhKXIpBepM8e1..; isg=BJWVzxHeWH5uuny33pJqLZj1pJFPkkmkUyF3pxc5QIxobrdg3uNedkZoOHJY6GFc',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16179729556.59.18e1628a8dvMr3&id=37452863348&rn=c8a8a7d28d59eb192111fa8f86007657&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/durex_lasting.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

def siki(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=658644415283&spuId=2169555128&sellerId=2212660367727&order=3&currentPage='
    urllast  = '&append=0&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvmpvLv7UvUvCkvvvvvjiWPsLZtjEjPsd9gj3mPmPpgjtRRsc90jEmn2dp6jtbdvhvmpvvX9U6nvC6zIvCvv147MbzaY147Di6Jr%2F%2BvpvEvvog9fmQvV2KdvhvmpvhPvE0a9vvRgOCvvpvCvvvRvhvCvvvvvmIvpvUvvmvS%2BL9QrJUvpvVmvvC9jDPKvhv8vvvvvCvpvvvvvmvqyCv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvUvpCWvEHTvvwYAXcBlLyzOvxrAnCl5dUfbjxrD70OjClvIExrACeK4Z7DYExrVBIaUrLZ6RpajjXRtb2XSfpAOH2%2BFOcn%2B3CAoWex6aZtnQvCvvOvCvvvphvRvpvhvv2MMTOCvvpvvUmmdvhvhovhlOV9IvCw%2FAeS8kH2mOcERvhvCvvvvvm%2BvpvEvvo19XTJvjCodvhvmpvhH9EYNpC62OvCvm1T7dfMor147DiqBaGD1TAqsd%2FoU0diIWPVs9ndmV5VktmneOh2vg%2FnyE8BeL9Cvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638599545594_599&callback=jsonp600'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=658644415283&spuId=2169555128&sellerId=2212660367727&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvmpvLv7UvUvCkvvvvvjiWPsLZtjEjPsd9gj3mPmPpgjtRRsc90jEmn2dp6jtbdvhvmpvvX9U6nvC6zIvCvv147MbzaY147Di6Jr%2F%2BvpvEvvog9fmQvV2KdvhvmpvhPvE0a9vvRgOCvvpvCvvvRvhvCvvvvvmIvpvUvvmvS%2BL9QrJUvpvVmvvC9jDPKvhv8vvvvvCvpvvvvvmvqyCv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvUvpCWvEHTvvwYAXcBlLyzOvxrAnCl5dUfbjxrD70OjClvIExrACeK4Z7DYExrVBIaUrLZ6RpajjXRtb2XSfpAOH2%2BFOcn%2B3CAoWex6aZtnQvCvvOvCvvvphvRvpvhvv2MMTOCvvpvvUmmdvhvhovhlOV9IvCw%2FAeS8kH2mOcERvhvCvvvvvm%2BvpvEvvo19XTJvjCodvhvmpvhH9EYNpC62OvCvm1T7dfMor147DiqBaGD1TAqsd%2FoU0diIWPVs9ndmV5VktmneOh2vg%2FnyE8BeL9Cvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638599545594_599&callback=jsonp600',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; xlly_s=1; sgcookie=E100nrEULpex7G67h%2FsrCkjRjbX8dp4gdyZpQLf4SCJzr6mY%2BoId4XndrN1w0Y76k0T7D8vk8vhCEOmt3ioG4L4eXz%2FZnrt%2BZIJ%2BoR0gGfg4L0w%3D; uc1=cookie14=Uoe3f4US%2FMOa1Q%3D%3D; uc3=id2=UNN%2BxywbWY3%2Big%3D%3D&vt3=F8dCvUj48Dv8WV7Gx58%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D; t=b8a7d834ecf92000456345bdec65ec54; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=id4=0%40UgQ2gbehJFA8tC%2BRmm4nls2UIh33&nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKmqEBpALIZ; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; _tb_token_=331e5e3877ee8; cookie2=1dee91c6b379cf5b1beecffb28f5e592; _m_h5_tk=2443a2e120930625cf52018332906920_1638601167356; _m_h5_tk_enc=ac0dd2e29588c286f7ef7543064cf439; l=eBLwFerIg2dIFrqMBO5Bnurza77TqIdbzRVzaNbMiInca1POaF-siNCdjiLJudtxgt5vjetrRRzQkRnJJ4a38E_ceTwhKXIpBGv68e1..; tfstk=ci1NBAVhm5FaaXRbeCO4C_rVtzZOZLbGoX8WIOuH_gUtfMpGiEmv-jL68EgEmdf..; isg=BI-P3EMRMi1mQTblyLSwP6ZLHiOZtOPWPW-9laGd-_4YcK1yqYSoJ94mc6BOMbtO',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-24057155397.52.677424833Rg8Iq&id=658644415283&rn=cb409cc3f793ecb6c38179bc76b1af6b&abbucket=17&skuId=4918955902702',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #ratecontent项的后面是评论，将评论提取添加到
        con.extend(re.findall('"rateContent":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"rateContent":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/siki.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

#杜蕾斯air
def durex_air(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=44140405751&spuId=1959439776&sellerId=1986899349&order=3&currentPage='
    urllast  = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hv%2BpvovoGvUvCkvvvvvjiWPsLwzjYbR2SWAjnEPmPO6jrnRFSh1jrmRsMhAjlWRvhvCvvvvvm%2BvpvEvvp7vlxxvmFZdvhvmpvhjvWlnpv9XTQCvvyvCEg2FIgvUW0%2BvpvEvvCGviVBvCmcdvhvmpvh0Q8j3QvvFF9CvvpvvvvvmvhvLvm6e9vj49033we3rABCIExr18TZfvDrAjc6%2BulAbTAxfwmKHkyZgnLyzCOqb64B9W2%2B%2BfvsxI2UTWeARFxjKOmDYb8raoFQD7zvdi%2FIvpvUvvmvS%2BtNwIJUvpvVmvvC9jDPKvhv8vvvvvCvpvvvvvmvJ6Cv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvvvpvVvvpvvhCv29hvCvvvMM%2Fevpvhvvmv9IOCvvpvCvvvdvhvmpvhyO8a5pvOS8QCvvyvCEW2CpZvEP7vvpvWzPAvOVFNznswcxD4&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774450759_1280&callback=jsonp1281'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=44140405751&spuId=1959439776&sellerId=1986899349&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hv%2BpvovoGvUvCkvvvvvjiWPsLwzjYbR2SWAjnEPmPO6jrnRFSh1jrmRsMhAjlWRvhvCvvvvvm%2BvpvEvvp7vlxxvmFZdvhvmpvhjvWlnpv9XTQCvvyvCEg2FIgvUW0%2BvpvEvvCGviVBvCmcdvhvmpvh0Q8j3QvvFF9CvvpvvvvvmvhvLvm6e9vj49033we3rABCIExr18TZfvDrAjc6%2BulAbTAxfwmKHkyZgnLyzCOqb64B9W2%2B%2BfvsxI2UTWeARFxjKOmDYb8raoFQD7zvdi%2FIvpvUvvmvS%2BtNwIJUvpvVmvvC9jDPKvhv8vvvvvCvpvvvvvmvJ6Cv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvvvpvVvvpvvhCv29hvCvvvMM%2Fevpvhvvmv9IOCvvpvCvvvdvhvmpvhyO8a5pvOS8QCvvyvCEW2CpZvEP7vvpvWzPAvOVFNznswcxD4&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774450759_1280&callback=jsonp1281',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; _m_h5_tk=3149af29ba1541f861125f69757fa002_1638610306945; _m_h5_tk_enc=22fa5fd7e0b312eb13729e9108fd3e17; xlly_s=1; dnk=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&pas=0&existShop=false&cookie21=W5iHLLyFe3xm&cookie14=Uoe3f4dko4pMSw%3D%3D; uc3=vt3=F8dCvUmgynpARfD%2BOqQ%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNN%2BxywbWY3%2Big%3D%3D; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKp2M0KT62T&id4=0%40UgQ2gbehJFA8tC%2BRmm4owWUnkKE8; _l_g_=Ug%3D%3D; unb=3331147902; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; cookie1=UtVufEJltUr%2FEQtmL74YC6KuXWRZyeztGN6m9f50pNw%3D; login=true; cookie17=UNN%2BxywbWY3%2Big%3D%3D; cookie2=1dfc51061c4449ea1b1ac5a7b5f1eb6d; _nk_=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; sgcookie=E100TOjbbC06JpKJ16gtvp9qdyzME%2BrOE8CPgbCUmPC4lyvdgXoYYqn6clntRQvby9WdMILgE0i1St162PceCJl4KYw1F9vZFAzjm4n7Zv5DeKk%3D; cancelledSubSites=empty; t=ab26e699ce3bec0a14c58e1066a5f1b3; sg=421; csg=6389a29a; _tb_token_=f175ebe0b835f; tfstk=ccRABOf-_0m0_x_J8KHk1dkitS1OZwoOVrsg64NZcYWUqHFOiNOH9RUrhNsFD4C..; l=eBLwFerIg2dIFjsUBO5Churza779fQObzsPzaNbMiInca1olGUQN8NCdAA0HPdtjgt5ApeKrRRzQkRe6-AULRE_ceTwhKXIpBT9w8e1..; isg=BLCw_8_8pR7Qf3koA4mHat2-gX4C-ZRD9rqyGKoCHotEZVIPUwhC0_gTvW0FdUwb',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16179729556.54.18e1628a8dvMr3&id=44140405751&rn=c8a8a7d28d59eb192111fa8f86007657&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/durex_air.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

#冈本001
def okamoto_001(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=41762748280&spuId=1690887414&sellerId=2032870312&order=3&currentPage='
    urllast  = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvZvvpvL9vUvCkvvvvvjiWPsLwzjYPPL5yAjrCPmP9QjDPR2qWljtbR2zy1j3E9vhv8cMGOHt3zYswzPl57kdoE93ukbj2J1%2BhTKuUAbt3kZbFQ%2B8RkeVCvQbk39hvCvvhvvmevpvhvvmv99vCvvOvCvvvphvUvpCWCb3KvvakfwCldChBfvDr1jc6d4t%2Bm7zwaNpOHkyZ1WFZgC97nDeDyO2v5fh3Zi7v0R9t%2BFBCAfevD40Xjo2h%2B8c6et107reYiXhpVU9CvvOUvvVvJZ%2FIvpvUvvmvS%2BtHjW4gvpvIvvvvvhCvvvvvvUCqphvW39vv96CvpC29vvm2phCvhmvvvUnvphvpUvgCvvpvvPMMRvhvCvvvvvmvvpvZzPA1casNznswP2lft%2F2wVnA%2B7e9gvpvhvvvvv8QCvvyvCbRCeXyvHje%2BvpvEvvo1vylnvCBNdvhvmpvhC9EacpvO8F9Cvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774018344_578&callback=jsonp579'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=41762748280&spuId=1690887414&sellerId=2032870312&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvZvvpvL9vUvCkvvvvvjiWPsLwzjYPPL5yAjrCPmP9QjDPR2qWljtbR2zy1j3E9vhv8cMGOHt3zYswzPl57kdoE93ukbj2J1%2BhTKuUAbt3kZbFQ%2B8RkeVCvQbk39hvCvvhvvmevpvhvvmv99vCvvOvCvvvphvUvpCWCb3KvvakfwCldChBfvDr1jc6d4t%2Bm7zwaNpOHkyZ1WFZgC97nDeDyO2v5fh3Zi7v0R9t%2BFBCAfevD40Xjo2h%2B8c6et107reYiXhpVU9CvvOUvvVvJZ%2FIvpvUvvmvS%2BtHjW4gvpvIvvvvvhCvvvvvvUCqphvW39vv96CvpC29vvm2phCvhmvvvUnvphvpUvgCvvpvvPMMRvhvCvvvvvmvvpvZzPA1casNznswP2lft%2F2wVnA%2B7e9gvpvhvvvvv8QCvvyvCbRCeXyvHje%2BvpvEvvo1vylnvCBNdvhvmpvhC9EacpvO8F9Cvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774018344_578&callback=jsonp579',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; _m_h5_tk=3149af29ba1541f861125f69757fa002_1638610306945; _m_h5_tk_enc=22fa5fd7e0b312eb13729e9108fd3e17; xlly_s=1; dnk=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&pas=0&existShop=false&cookie21=W5iHLLyFe3xm&cookie14=Uoe3f4dko4pMSw%3D%3D; uc3=vt3=F8dCvUmgynpARfD%2BOqQ%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNN%2BxywbWY3%2Big%3D%3D; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKp2M0KT62T&id4=0%40UgQ2gbehJFA8tC%2BRmm4owWUnkKE8; _l_g_=Ug%3D%3D; unb=3331147902; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; cookie1=UtVufEJltUr%2FEQtmL74YC6KuXWRZyeztGN6m9f50pNw%3D; login=true; cookie17=UNN%2BxywbWY3%2Big%3D%3D; cookie2=1dfc51061c4449ea1b1ac5a7b5f1eb6d; _nk_=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; sgcookie=E100TOjbbC06JpKJ16gtvp9qdyzME%2BrOE8CPgbCUmPC4lyvdgXoYYqn6clntRQvby9WdMILgE0i1St162PceCJl4KYw1F9vZFAzjm4n7Zv5DeKk%3D; cancelledSubSites=empty; t=ab26e699ce3bec0a14c58e1066a5f1b3; sg=421; csg=6389a29a; _tb_token_=f175ebe0b835f; tfstk=cCjABAt8b7VD0vvRLZUlfNrXAVBOZ0V9NxOiX8iaIUpiNpoOiOshvVHzldOeM8C..; l=eBLwFerIg2dIFFjhBO5Zourza77OBIRbzsPzaNbMiInca1rlZFT4pNCdAACHodtjgt5vfetrRRzQkRU6-x438E_ceTwhKXIpBav68e1..; isg=BI2N1crE0MEOTHTfZrqSxVCdnKkHasE8C_l_T88SNCSSxq94l7vXDa4QMFqgBtn0',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-21743799364.52.532b2edeiqDDDT&id=41762748280&rn=ffeeb704211e2a294fb62f6c59b9da85&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/okamoto_001.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

def okamoto_lasting(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=44953265864&spuId=1681472318&sellerId=2032870312&order=3&currentPage='
    urllast  = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvy9vnvp%2BvUvCkvvvvvjiWPsLwzjYnn25h0jnEPmP9ljl8P2dvsjYPRLcOAj1hRvhvCvvvvvmvvpviNM1kcDfNznswM7x48rUemVuU%2BwnqVQLuTIFUSeVEpKPmQITWeOhmIk8%2BvpvEvvp7vI4Vvv3udvhvmpvhVvbiTpvvFQvCvvOvCvvvphmUvpvVmvvC9jDPuvhvmvvv9bqRpOsHKvhv8vvvvvCvpvvvvvmvJ6Cv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvUvpCWCVkjvvw%2FaNoxfBeXjLPBtwVxHdUf8%2B3lYUk0r0ERiNoxfX9XjobWzn2pjX36Lf2XS4ZAhjCbFOcnDBmXJ9kx6acEn1vDN%2B1lYE7re9gCvvpvvPMMRvhvCvvvvvmevpvhvvmv9IOCvvpvCvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774287566_628&callback=jsonp629'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=44953265864&spuId=1681472318&sellerId=2032870312&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvy9vnvp%2BvUvCkvvvvvjiWPsLwzjYnn25h0jnEPmP9ljl8P2dvsjYPRLcOAj1hRvhvCvvvvvmvvpviNM1kcDfNznswM7x48rUemVuU%2BwnqVQLuTIFUSeVEpKPmQITWeOhmIk8%2BvpvEvvp7vI4Vvv3udvhvmpvhVvbiTpvvFQvCvvOvCvvvphmUvpvVmvvC9jDPuvhvmvvv9bqRpOsHKvhv8vvvvvCvpvvvvvmvJ6Cv2UOvvUnvphvpgvvv96CvpCv9vvm2phCvhmvUvpCWCVkjvvw%2FaNoxfBeXjLPBtwVxHdUf8%2B3lYUk0r0ERiNoxfX9XjobWzn2pjX36Lf2XS4ZAhjCbFOcnDBmXJ9kx6acEn1vDN%2B1lYE7re9gCvvpvvPMMRvhvCvvvvvmevpvhvvmv9IOCvvpvCvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638774287566_628&callback=jsonp629',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; _m_h5_tk=3149af29ba1541f861125f69757fa002_1638610306945; _m_h5_tk_enc=22fa5fd7e0b312eb13729e9108fd3e17; xlly_s=1; dnk=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&pas=0&existShop=false&cookie21=W5iHLLyFe3xm&cookie14=Uoe3f4dko4pMSw%3D%3D; uc3=vt3=F8dCvUmgynpARfD%2BOqQ%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNN%2BxywbWY3%2Big%3D%3D; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKp2M0KT62T&id4=0%40UgQ2gbehJFA8tC%2BRmm4owWUnkKE8; _l_g_=Ug%3D%3D; unb=3331147902; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; cookie1=UtVufEJltUr%2FEQtmL74YC6KuXWRZyeztGN6m9f50pNw%3D; login=true; cookie17=UNN%2BxywbWY3%2Big%3D%3D; cookie2=1dfc51061c4449ea1b1ac5a7b5f1eb6d; _nk_=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; sgcookie=E100TOjbbC06JpKJ16gtvp9qdyzME%2BrOE8CPgbCUmPC4lyvdgXoYYqn6clntRQvby9WdMILgE0i1St162PceCJl4KYw1F9vZFAzjm4n7Zv5DeKk%3D; cancelledSubSites=empty; t=ab26e699ce3bec0a14c58e1066a5f1b3; sg=421; csg=6389a29a; _tb_token_=f175ebe0b835f; isg=BHR0ral-qQo8bj10570b_mGCRTLmTZg3mhZ2JA7UD_-BeRbDNlxgx8I_-bGhgdCP; tfstk=cn2OBOMd3wbgkaiL45C3hSWIsjkOZabxRhgDHM9VqxzMbA9AimwueIKF1mgrWMC..; l=eBLwFerIg2dIFZ1fBO5anurza77OmIObzsPzaNbMiInca1zlaFaWGNCdAAf2udtjgtfvretrRRzQkRUk-XzLRZ_ceTwhKXIpBxv6-',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-21743799364.62.532b2edeiqDDDT&id=44953265864&rn=ffeeb704211e2a294fb62f6c59b9da85&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/okamoto_lasting.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

#杰士邦001持久
def jissbon_001lasting(num):
    #url列表
    PAGE_URL = []
    #拼接url
    urlfirst = 'https://rate.tmall.com/list_detail_rate.htm?itemId=40022007471&spuId=936212402&sellerId=2115733820&order=3&currentPage='
    urllast  = '&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hv9QvovLZvUpCkvvvvvjiWPsLOQjDRRsFp6jivPmPUgjt8PLdwtjl8PssUtjYUR8QCvvyvCEGmxxZvRcV%2BvpvEvvpf9NMMv27ARvhvCvvvvvm%2BvpvEvvBb9Lwzvmj039hvCvvhvvmevpvhvvmv99gCvvLMMQvvvvhvC9vhvvCvpb9Cvm9vvvvvphvvvvvv9W1vpvAVvvm2phCvhRvvvUnvphvpUvvv96CvpCv9uvhvmvvv9bqhyDAukvhvC99vvOCtLQ9CvhQWGCWvCld6D7zhV4t%2FLdmDYE7rejpiMWshzCyaaZL9gb2XrqpyCW2%2BFO7t%2BeCoARFEDLuTWDAviNoxdBD68Nmxfw9XdegmDfea6LoNRvhvCvvvvvm%2BvpvEvvo39NdTvm7V9vhvHnsGeHzazYswzmcx7%2FN9jmzwdHiIdvhvmpvhH9Umv9vYFOvCvvswMUxJTaMwznQV1DIgvpvhvvvvvv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638602795406_606&callback=jsonp607'
    #将页数用range生成循环，将生成的页数不同的url网址存放在列表中
    for i in range(0,num):
        PAGE_URL.append(urlfirst+str(1+i)+urllast)
    #评价列表
    con = []

    for i in range(num):
        #在F12开发者模式中都可以找到这些参数信息
        headers = {
            'authority': 'rate.tmall.com',
            'method': 'GET',
            'path':'/list_detail_rate.htm?itemId=40022007471&spuId=936212402&sellerId=2115733820&order=3&currentPage=1&append=1&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hv9QvovLZvUpCkvvvvvjiWPsLOQjDRRsFp6jivPmPUgjt8PLdwtjl8PssUtjYUR8QCvvyvCEGmxxZvRcV%2BvpvEvvpf9NMMv27ARvhvCvvvvvm%2BvpvEvvBb9Lwzvmj039hvCvvhvvmevpvhvvmv99gCvvLMMQvvvvhvC9vhvvCvpb9Cvm9vvvvvphvvvvvv9W1vpvAVvvm2phCvhRvvvUnvphvpUvvv96CvpCv9uvhvmvvv9bqhyDAukvhvC99vvOCtLQ9CvhQWGCWvCld6D7zhV4t%2FLdmDYE7rejpiMWshzCyaaZL9gb2XrqpyCW2%2BFO7t%2BeCoARFEDLuTWDAviNoxdBD68Nmxfw9XdegmDfea6LoNRvhvCvvvvvm%2BvpvEvvo39NdTvm7V9vhvHnsGeHzazYswzmcx7%2FN9jmzwdHiIdvhvmpvhH9Umv9vYFOvCvvswMUxJTaMwznQV1DIgvpvhvvvvvv%3D%3D&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1638602795406_606&callback=jsonp607',
            'cheme': 'https',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'cookie':'hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%8C%97%E4%BA%AC%E6%AC%A2%E8%BF%8E%E4%BD%A0248514; enc=yMcjgQsdFXMXysrimFBr2GCz2Vhhl8P%2BFNHXjdsWt9sD3ReN8BoNlP%2FskHyoCfw1%2Bc53TSlc75gL7lgLm%2FKhYQ%3D%3D; cna=sjcWGhywZ1gCAWpVTtHcR1U0; xlly_s=1; sgcookie=E100nrEULpex7G67h%2FsrCkjRjbX8dp4gdyZpQLf4SCJzr6mY%2BoId4XndrN1w0Y76k0T7D8vk8vhCEOmt3ioG4L4eXz%2FZnrt%2BZIJ%2BoR0gGfg4L0w%3D; uc1=cookie14=Uoe3f4US%2FMOa1Q%3D%3D; uc3=id2=UNN%2BxywbWY3%2Big%3D%3D&vt3=F8dCvUj48Dv8WV7Gx58%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=0vR4jdz0p5LBno1Q%2ByLESg%3D%3D; t=b8a7d834ecf92000456345bdec65ec54; tracknick=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; uc4=id4=0%40UgQ2gbehJFA8tC%2BRmm4nls2UIh33&nk4=0%400EUOpTdnsRz27EQfh1s5WLKONzKmqEBpALIZ; lgc=%5Cu5317%5Cu4EAC%5Cu6B22%5Cu8FCE%5Cu4F60248514; _tb_token_=331e5e3877ee8; cookie2=1dee91c6b379cf5b1beecffb28f5e592; _m_h5_tk=3149af29ba1541f861125f69757fa002_1638610306945; _m_h5_tk_enc=22fa5fd7e0b312eb13729e9108fd3e17; tfstk=c-M1BA4BoNb1k-OVQctFbE5U7SedayS7cCaifjH8gXzNrdn_JsmhUzMmtjbY3oEC.; l=eBLwFerIg2dIFyJ3BO5Bourza77TWIRbzFVzaNbMiInca14PGF9NuNCdjZjyPdtxgt5vietrRRzQkReJ-rUg7E_ceTwhKXIpBM968e1..; isg=BKurcKBiTlkxL5I5VCDcC2IHOs-VwL9CebPZqR0ofOpBvMkepZFkkV9aF_zSqRc6',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'referer':'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-23001239991.66.6987639fbqt5QP&id=40022007471&rn=9a3c34bfea0d6d49f0d5c6a3ed216994&abbucket=17&sku_properties=21845:37023;31889:107474',
            'accept': '*/*',
            'accept-encoding':'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
        }
        #解析js文件内容
        content = requests.get(PAGE_URL[i],headers=headers,timeout=30).text
        #加入时间停顿，防止被认为是爬虫
        time.sleep(random.randint(7,12))
        #content项的后面是评论，将评论提取添加到
        con.extend(re.findall('"content":"(.*?)"', content))
        #输出看看有没有被盾
        print(re.findall('"content":"(.*?)"', content))

    #将数据写入text文件中
    for i in list(range(0,len(con))):
        text = ''.join((con[i])) + '\n'
        with open(r"../crawler_data/jissbon_001lasting.txt", 'a+', encoding='UTF-8') as file:
            file.write(text + ' ')
            # print(i+1,":写成功")
    print('写入成功！')

#主函数
if __name__ == "__main__":
    siki(6)
    durex_thin(100)
    durex_lasting(100)
    durex_air(100)
    okamoto_001(100)
    okamoto_lasting(100)
    jissbon_001lasting(100)