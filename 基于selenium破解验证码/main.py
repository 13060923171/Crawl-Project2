import re
# 图片处理
from PIL import Image
# 文字识别
import pytesseract
# 浏览器自动化
from selenium import webdriver
import time
#示例网站
url = 'http://lims.gzzoc.com/client'
#调用selenium工具
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",{"profile.mamaged_default_content_settings.images":2})
options.add_experimental_option('excludeSwitches',['enable-automation'])
driver= webdriver.Chrome(executable_path="C:\\Users\\96075\\Desktop\\全部资料\\Python\\爬虫\\chromedriver.exe",options=options)
driver.maximize_window() # 最大化窗口
time.sleep(1)
driver.get(url)
#点击弹出窗口，点击确定
driver.find_element_by_xpath("//div[@class='jconfirm-buttons']/button").click()
#定位到验证码的位置
img =driver.find_element_by_xpath('//img[@id="valiCode"]')
time.sleep(1)
#定位验证码的坐标
location = img.location
#定位验证码的大小
size = img.size
#正常情况直接用下面这四行代码就可以做到截图了，但是为了防止存在误差，需要考虑乘上倍率系数。最后可以再加减数值进行微调
# left = location['x']
# top = location['y']
# right = left+size['width']
# bottom = top+size['height']
left = 2*location['x']
top = 2*location['y']
right = left + 2*size['width'] -20
bottom = top + 2*size['height'] -20
driver.save_screenshot('valicode.png')
page_snap_obj = Image.open('valicode.png')
image_obj = page_snap_obj.crop((left,top,right,bottom))
image_obj.show()

# #转灰度图
# img = image_obj.convert('L')
# pixdata = img.load()
# w,h = img.size
# #阈值为205，
# # 这个阈值需要具体用Photoshop或者其他工具尝试，即找到一个像素阈值能够将灰度图片中真实数据和背景干扰分开，本例经测试阈值为205
# threshod = 205
# #遍历所有像素，大于阈值的为黑色
# for y in range(h):
#     for x in range(w):
#         if pixdata[x,y] < threshod:
#             pixdata[x,y] = 0
#         else:
#             pixdata[x,y] = 255
#
# data = img.getdata()
# w,h = img.size
# black_point = 0
# for x in range(1,w-1):
#     for y in range(1,h-1):
#         mid_pixel = data[w*y+x]
#         if mid_pixel <50:
#             top_pixel = data[w*(y-1)+x]
#             left_pixel = data[w*y+(x-1)]
#             down_pixel = data[w*(y+1)+x]
#             right_pixel = data[w*y+(x+1)]
#             if top_pixel < 10:
#                 black_point += 1
#             if left_pixel < 10:
#                 black_point += 1
#             if down_pixel < 10:
#                 black_point += 1
#             if right_pixel < 10:
#                 black_point += 1
#             if black_point<1:
#                 img.putpixle((x,y),255)
#             black_point =0
# img.show()
# result = pytesseract.image_to_string(img)
# regex = '\d+'
# result = ''.join(re.findall(regex,result))
# print(result)
#
# driver.find_element_by_name('code').send_keys(result)
# driver.find_element_by_name('userName').send_keys('xxx')
# driver.find_element_by_name('password').send_keys('xxx')
# #最后点击确定
# driver.find_element_by_xpath("//div[@class='form-group login-input'][3]").click()
#注意这个并不是百分百正确，需要加一个无限循环以及防错机制才行，
# 这里最难的一点便是怎么定位到验证码的位置，然后再用ps测试它的阈值，进行灰度转化