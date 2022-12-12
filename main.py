from AverageFileMaker import AverageFileMaker

if __name__ == '__main__':
    analisi = AverageFileMaker(["2018", "2019"], ["01", "02"])
    analisi.fillDataFrames()
    # print(analisi.getYearDataFrame('2018'), "\n")
    # print(analisi.getYearDataFrame('2019'))
    analisi.writeFiles()
