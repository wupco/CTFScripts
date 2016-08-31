import multiprocessing
from os import urandom
from hashlib import md5
import sys

def work(cipher):
    for i in range(100):
        plain = urandom(16).encode('hex')
        if md5(plain).hexdigest()[:6] == cipher:
            print plain
            sys.exit(0)




if __name__ == '__main__':
    cipher = raw_input('md5:')
    print multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=8)
    while True:
        plain = urandom(16).encode('hex')
        pool.apply_async(work, (cipher, ))
    pool.close()
    pool.join()