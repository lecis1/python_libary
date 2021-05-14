from datetime import datetime


data_list =  [
        ['jack', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ['lucy', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ['andy', '普通', '普通', '没有描述', '%s' % datetime.now()],
        ]

for file in data_list:
    for index, file in enumerate(file):
        print(index, file )