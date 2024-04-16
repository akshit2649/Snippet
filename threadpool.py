from multiprocessing.pool import ThreadPool

def unit_task(num):
        return num * 2

def process():
        l = [unit_task(1),unit_task(2),unit_task(3),unit_task(4),unit_task(5)]
        p = ThreadPool(processes=2)
        result = p.map(unit_task, l)
        p.close()
        print(result)

if __name__ == "__main__":
        process()
