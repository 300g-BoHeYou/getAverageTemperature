from requests import get


def getAverageTemperature(city, date):
    # 爬取网页
    url = r"https://www.tianqishi.com/"+city+"/"+date+".html"
    html = get(url).text

    # 获取逐小时温度
    temperatures = []
    String_list = html.split('<td width="8%">')
    for i in String_list[1:]:
        temperatures.append(int(i[:2]))
    # 获取平均温度
    average_temperature = str(sum([temperatures[1],temperatures[7],temperatures[13],temperatures[19]]) / 4)

    return average_temperature


#获取气温
# 济南
jinan_average_temperature = []
# 7月
for day in range(15,32):
    jinan_average_temperature.append(getAverageTemperature("jinan","202207"+'%02d'%day ))
# 8月
for day in range(1,16):
    jinan_average_temperature.append(getAverageTemperature("jinan","202208"+'%02d'%day))

# 青岛
qingdao_average_temperature = []
# 7月
for day in range(15,32):
    qingdao_average_temperature.append(getAverageTemperature("qingdao","202207"+'%02d'%day))
# 8月
for day in range(1,16):
    qingdao_average_temperature.append(getAverageTemperature("qingdao","202208"+'%02d'%day))


#写入文件
with open("济南.txt",'w') as f:
    f.write("\n".join(jinan_average_temperature))
with open("青岛.txt",'w') as f:
    f.write("\n".join(qingdao_average_temperature))
