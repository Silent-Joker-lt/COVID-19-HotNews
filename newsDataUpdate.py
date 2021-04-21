from newsfirstinsert import dataget
import pymysql
def newsUpdate(inOut):
    nowData = dataget(inOut)
    conn = pymysql.connect("localhost", "root", "", charset="utf8")
    cur = conn.cursor()
    conn.select_db("新闻")
    base = ['国内新闻', '国外新闻']
    cur.execute("truncate table {}".format(str(base[inOut])))
    cur.executemany("INSERT INTO {}(时间, 事件简述,事件地址,事件来源) VALUES (%s,%s,%s,%s)".format(str(base[inOut])), nowData)
    conn.commit()
    cur.close()
    conn.close()

