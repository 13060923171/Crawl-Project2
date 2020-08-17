import re
import requests
def main():
    for i in range(0,91,10):
        url = "https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={}&cselibv=26b8d00a7c7a0812&cx=017476104391584697148:yfiniwqwjp4&q=2020%20election&safe=off&cse_tok=AJvRUv3qKha5AzyLLUMu592n_u7Z:1596906371854&sort=&exp=csqr,cc&callback=google.search.cse.api2105".format(i)
        print(url)
        name = str(i)
        download(url,name)

def download(url,name):
    with open("{}.txt".format(name),"wb")as f:
        f.write(requests.get(url).content)
        print("下载完成第{}页".format(name))

def read():
    for i in range(1,11):
        with open("{}.txt".format(i),"r",encoding="utf8")as f:
            content = f.read()
            href = re.compile('"cacheUrl": "(.*?)",',re.S|re.I)
            result = href.findall(content)
            for r in result:
                with open("新闻的URL.txt","a+",encoding="utf8")as f:
                    f.write(r+"\n")



if __name__ == '__main__':
    main()
    read()