import json
import requests
import csv


file = open("G:\\meituancom.csv", "w", encoding='utf-8-sig', newline='')
writer = csv.writer(file, delimiter=',')


def Get_results(Json_data):
    ALL = Json_data['data']['comments']
    Res = []
    for i in range(0, 10):
        PRS = ALL[i]
        userId = PRS['userId']
        userName = PRS['userName']
        comment = PRS['comment']
        star = PRS['star']
        Res.append([userId, userName, comment, star])
    return Res


def main(num):
    RES = []
    for i in range(1, num):
        print("当前完成第" + str(i) + "页")
        url = "https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=3cf995a6-a997-41b6-8243-fc3eaa0415b0" \
              "&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F1496465%2F&riskLevel=1" \
              "&optimusCode=10&id=1496465&userId=&offset="+ str((i-1)*10) +"&pageSize=10&sortType=1."
        user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        headers = {"User-Agent": user_agent}
        response = requests.get(url, timeout=10, headers=headers)
        res = json.loads(response.text)
        ReS = Get_results(res)
        RES.append(ReS)
    print("全部完成")
    return RES


def fwrite(file, Res, Label):
    writer = csv.writer(file)
    writer.writerow(Label)
    for Data in Res:
        for row in Data:
            writer.writerow(row)

if __name__ == '__main__':
    Res = main(11)  # 获取数据
    Label = ["userId", "userName", "comment", "star"]
    fwrite(file, Res, Label)
