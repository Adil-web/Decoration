import time

class Timing:
    def __init__(self, func_to_run):
        self.num_runs = 10
        self.func_to_run = func_to_run

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        fn = self.func_to_run.__name__
        print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, self.num_runs, avg_time))
        with open("avg_time.txt", "w", encoding="utf-8") as avg:
            avg.write("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, self.num_runs, avg_time))
            print("Файл txt успешно создан!")
        return self.func_to_run(*args, **kwargs)

@Timing
def function_example():
    for j in range(1000000):
        pass


function_example()