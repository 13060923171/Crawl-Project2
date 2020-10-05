# import requests
# import re
# url = 'https://ihotel.meituan.com/api/v2/comments/biz/reviewList?referid=169549643&limit=15&start=45&filterid=800&querytype=1&utm_medium=pc'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
#     'Cookie': '_lxsdk_cuid=173e1f47707c8-0dcd4ff30b4ae3-3323765-e1000-173e1f47707c8; _hc.v=5f3d72e8-ba19-4712-5fce-55b10b156df5.1597224599; ci=30; rvct=30%2C1; iuuid=5507984E87AFD6AA06E2F4757AB74FA91C04750435F6A4892A8830402F602188; cityname=%E6%B7%B1%E5%9C%B3; _lxsdk=5507984E87AFD6AA06E2F4757AB74FA91C04750435F6A4892A8830402F602188; IJSESSIONID=1rw0g3kq87i22vq71xmg1yry7; i_extend=E150509991087792305278286805556360001967_c79_e1325181720321422241_anull_b400201_o1_dhotelpoitagb_k1002Gempty__xhotelhomepage__yselect__zday; _lxsdk_s=174f2ce56bb-873-a94-f32%7C%7C10',
#
# }
# html = requests.get(url,headers=headers).text
# #获取评论
# Contents = re.compile('"Content":(.*?)",', re.I | re.S)
# Content = Contents.findall(html)
# print(Content)
# print(len(Content))
