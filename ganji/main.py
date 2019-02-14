from get_extract import channel_extract
from multiprocessing import Pool
from parse import get_one_cate

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_one_cate, channel_extract.split())