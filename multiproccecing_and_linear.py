import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open("./Files/" + name, "r", encoding="utf-8") as f:
        x = f.readline()
        while x != "":
            all_data.append(x)
            x = f.readline()


if __name__ == '__main__':
    names = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]
    start = datetime.now()
    for name in names:
        read_info(name)
    end = datetime.now()
    print(end - start, "(линейный)")

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, names)

    end = datetime.now()
    print(end-start, "(многопроцессорный)")
