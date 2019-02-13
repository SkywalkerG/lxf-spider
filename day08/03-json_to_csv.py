import json
import csv

json_fp = open('a.json', 'r')
json_data_list = json.load(json_fp)
json_fp.close()
# 取表头， 表内容
sheet_title = json_data_list[0].keys()
sheet_data = []
for data in json_data_list:
    sheet_data.append(data.values())

# 将 json 转换成 csv
csv_fp = open('a.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_fp)
writer.writerow(sheet_title)
writer.writerows(sheet_data)

csv_fp.close()