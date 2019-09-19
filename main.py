import numpy as np
import pandas as pd
import json


def formData(data):
  return dict(zip(data['t'], data['c']))


def readData():
  files = ['data2111.json', 'data518880.json',
           'data40820.json', 'data510050.json', 'data510300.json','data510500.json']
  data = []
  sameDate = set()
  for i in files:
    with open(i) as json_file:
      jsonData = json.load(json_file)
      print(len(jsonData['t']))
      sameDate = set(jsonData['t']) if (
          len(sameDate) <= 0) else (sameDate & set(jsonData['t']))
      data.append(formData(jsonData))

  result = []
  for eachData in data:
    tmp = dict()
    for name in sameDate:
       tmp[name] = eachData[name]
    result.append(tmp)
  for index, fileName in enumerate(files):
    with open('raw'+fileName, 'w') as outfile:
      json.dump(result[index], outfile)
  return result
  # for i in range(len(dataUSDCNY)):
  #  arr.append((dataUSDCNY[i], data518880[i]), data2111[i])
  # return arr


def dict2Array(ob):
  arr = []
  for i in ob:
    arr.append(ob[i])
  return arr


def main():
  # readData()
  fiberSplit = [0.236, 0.382, 0.500, 0.618, 0.764, 1]
  fiberSplit.reverse()
  dataResult = readData()
  result = []
  for i in dataResult:
    result.append(dict2Array(i))
  resultDataLen = len(result[0])
  fiberResult = []
  for i in fiberSplit:
    tmp = []
    for k in result:
      tmp.append(k[int((1-i)*(resultDataLen-1)):])
    fiberResult.append(tmp)

  for index,fr in enumerate(fiberResult):
    df = pd.DataFrame(list(zip(*fr)),
    columns=['CNY', '518880', 'SH', '510050', '510300','510500'])
    print(str(fiberSplit[index]*100)+' % '+str(len(fr[0])))
    print(df.corr())





if __name__ == "__main__":
    # execute only if run as a script
    main()
