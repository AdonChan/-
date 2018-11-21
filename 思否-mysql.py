import json
import pymysql
import os
path = r'D:\爬虫\爬虫—思否\json'
for i in os.listdir(path):
    exp = os.path.join(path,i)
    try:
        with open(exp, 'r', encoding='utf-8') as f:
            str_d = json.loads(f.read())
            conn = pymysql.connect(host ='localhost',user = 'root',password = '',database = 'db1')      #连接数据库
            cursor = conn.cursor()
            sql = "insert into sifou(title,tag,context,mainLikeNum,mainBookmarkNum) values(%s,%s,%s,%s,%s)"
            cursor.execute(sql,[str_d['title'],str_d['index'],str_d['content'],str_d['mainLikeNum'],str_d['mainBookmarkNum']])
            conn.commit()
            cursor.close()
            conn.close()
            print(str(i)+'导入成功')
    except:
        print(str(i)+'导入失败')
