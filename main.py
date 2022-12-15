from FileMaker.AverageFileMaker import AverageFileMaker

if __name__ == '__main__':
    analisi = AverageFileMaker(["2018", "2019", "2020", "2021"],
                               ["01", "02", "03", "04", "05", "06",
                                "07", "08", "09", "10", "11", "12"])
    analisi.fillDataFrames()
    # print(analisi.getYearDataFrame('2018'), "\n")
    # print(analisi.getYearDataFrame('2019'))
    analisi.writeFiles()
