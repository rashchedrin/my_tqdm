from my_tqdm import my_tqdm

if __name__ == '__main__':
    gg = my_tqdm(range(1005000))
    for i in gg:
        print(len(gg) + i - next(gg), end='\r')
