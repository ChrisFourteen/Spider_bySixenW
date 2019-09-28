import urllib.request
import csv
import re
import json

file = open("G:\\meituan.csv", "w", encoding='utf-8-sig', newline='')
writer = csv.writer(file, delimiter=',')
writer.writerow(["poiID", "title", "address", "avgScore", "avgPrice"])  # 确定格式


class Spider_info:
    def loadPage(self, page):
        url = "https://wh.meituan.com/meishi/pn" + str(page) + "/"

        user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        headers = {"User-Agent": user_agent}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)  # 返回的是http.client.HTTPResponse对象
        html = str(response.read(), 'utf-8')
        pattern = re.compile(r'{"poiId":.*?}', re.S)
        list = pattern.findall(html)  # 获取数据,返回的是正则表达式在字符串中所有匹配结果的列表

        for data in list:
            infos = json.loads(data)
            writer.writerow([infos["poiId"], infos["title"], infos["address"], infos["avgScore"], infos["avgPrice"]])


if __name__ == "__main__":
    mySpider = Spider_info()
    for i in range(1, 68):  # 网页上显示67页
        print("当前完成第" + str(i) + "页")
        mySpider.loadPage(i)
    file.close()
