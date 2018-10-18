# 动态规划程序

from dynamicModel import DynamicModel

filename = "p.192-8.2.dat"
try:
    with open(filename) as sourceFile:
        dataLines = sourceFile.readlines()
        print(dataLines)
    dynamicModel = DynamicModel()
    dynamicModel.initModel(dataLines)
    dynamicModel.optimization()
    dynamicModel.displayResult()
    print("计算完成...")
except IOError:
    print("文件不存在...")
print("Bye...")
