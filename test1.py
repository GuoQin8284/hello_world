from datetime import datetime

from user1 import User1

try:
    x=User1("root","root")

except Exception as x :
    with open("./data/log.txt","a",encoding="utf-8") as f:
        f.write("错误时间:{}\n错误信息：{}\n".format(datetime.today(),x))
