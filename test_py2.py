from my_tqdm import my_tqdm, my_tqdm_

if __name__ == '__main__':
    gg = my_tqdm_(range(1005000))
    for i in gg:
        print "\r" + str(i),

    gg = my_tqdm_(range(1005000))
    for i in gg:
        print "\r" + str(next(gg)),

    gg = my_tqdm(range(1005000))
    for i in gg:
        print "\r" + str(len(gg)),

    gg = my_tqdm(range(1005000))
    for i in gg:
        print "\r" + str(i),

    gg = my_tqdm(range(1005000))
    for i in gg:
        print "\r" + str(next(gg)),

