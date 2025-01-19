import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if len(line) == 0:
                break
            all_data.append(line)


if __name__ == '__main__':
    files = [f'file {i+1}.txt' for i in range(4)]

    # start_time = time.time()
    # for file in files:
    #     read_info(file)
    # stop_time = time.time()
    # print(f'Время выполнения без multiprocessing {stop_time - start_time} секунд')

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, files)
    stop_time = time.time()
    print(f'Время выполнения с multiprocessing {stop_time - start_time} секунд')
