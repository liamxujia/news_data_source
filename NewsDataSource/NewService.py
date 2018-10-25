

import requests
import pymysql.cursors
import json

# "posterId": null,
#             "content": "最新的剧情中,陆晨曦(",///
#             "posterScreenName": "腾讯",///
#             "tags": null,
#             "url": "http:\/\/ent.qq.com\/a\/20170508\/023354.htm",///
#             "publishDateStr": "2017-05-08T03:46:00",
#             "title": "白百何陷医患风波 《外科》靳东职业生涯遇危机",///
#             "publishDate": 1494215160,///
#             "commentCount": null,
#             "imageUrls": null,
#             "id": "c028fc8126658124bc8f21a13650d51b"///

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "xj1992928", "news")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS news")
# 如果表存在，则跳过创建表操作
# 使用预处理语句创建表
sql = """CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        newsId CHAR(255) ,
        title  CHAR(255),
        content CHAR(255),
        url CHAR(255),
        posterId CHAR(255),
        posterScreenName CHAR(255),
        publishDate INT
        )"""
cursor.execute(sql)
# 关闭数据库连接

print("CREATE TABLE OK")

params = {
    "apikey": "Pe2bj27PF0F5JfUvOKHd07zbx6BTRowGSJ7d1bcefzai1ed6OCsQrU02JF86vAFZ", "kw": "lol"}
r = requests.get("http://api01.idataapi.cn:8000/news/qihoo", params=params)
print(r.url)
response = json.loads(r.content.decode())
data = response.get("data")
print(data[0].get("title"))

for item in data:
    sql = """INSERT INTO news (newsId, title, content, url, posterId, posterScreenName, publishDate) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (item["id"], item["title"], item["content"], item["url"],
                         item["posterId"], item["posterScreenName"], item["publishDate"]))
db.commit()
db.close()
