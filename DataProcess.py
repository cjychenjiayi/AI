import csv
import numpy as np

def split( x ) ->list:
    x = str(x)
    x = x.split(" ")
    return [ int(x[0]), int(x[1]), int(x[2]), int(x[3]), float(x[4]), float(x[5]), int(x[6]) ]

# with open('ing.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     data = [split(row[0]) for row in reader]
data = [[205421000, 1620717008, 0, 10, -92.663696, 24.532267, 0], [205421000, 1620717669, 0, 9, -92.66552, 24.534849, 90], [205421000, 1620719003, 0, 10, -92.669563, 24.539316, 0], [205421000, 1620721234, 0, 9, -92.676865, 24.547518, 0], [205421000, 1620721254, 0, 9, -92.676918, 24.547583, 0]]

def makeUnique( data )->list:
    unique_data = list(set(data))
    mapping = {value: i for i, value in enumerate(unique_data)}
    result = [mapping[value] for value in data]
    print(len(mapping))
    return result

def seperate( data )->list :
    ret = []
    for i in range(7) :
        x = [row[i] for row in data ]
        ret.append(x)
    return ret

sep_data = seperate(data)
'''
mmsi
时间：Unix时间戳（秒）
航行状态
速度
经度
纬度
吃水
'''
mmsi = sep_data[0]
timestamp = sep_data[1]
speed = sep_data[2]
longitude = sep_data[3]
latitude = sep_data[4]
draft = sep_data[5]

mmsi = makeUnique(mmsi)
timestamp = np.array(timestamp)
timestamp = (timestamp - np.min(timestamp))

print(min(speed))
print(max(speed))




