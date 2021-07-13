import multiprocessing as mp
import numpy as np 

def square(x):
    return x**2


if __name__ == '__main__':
    mp.freeze_support()  # windows 10

    ncpus = mp.cpu_count()
    print('ncpus: ', ncpus)
    pool = mp.Pool(ncpus)

    x = np.arange(ncpus*8)

    squared = pool.map(square, [x[ncpus*i:ncpus*(i+1)] for i in range(ncpus)])
    