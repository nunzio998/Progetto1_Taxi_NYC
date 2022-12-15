import time

from FileMaker.AverageFileMaker import AverageFileMaker

if __name__ == '__main__':
    start = time.perf_counter()

    analisi = AverageFileMaker(["2020"], ["03", "04", "05"])
    analisi.writeFiles()

    end = time.perf_counter()

    print(f"Tempo di esecuzione: {round(end - start, 3)}")
