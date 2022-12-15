from FileMaker.AverageFileMaker import AverageFileMaker

if __name__ == '__main__':
    analisi = AverageFileMaker(["2022"], ["01"])
    analisi.fillDataFrames()
    # print(analisi.getYearDataFrame('2018'), "\n")
    # print(analisi.getYearDataFrame('2019'))
    analisi.writeFiles()
