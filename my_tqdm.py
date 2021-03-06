from __future__ import print_function
import time
from datetime import datetime, timedelta


def time_human_readable(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    if days > 0:
        return "%dd %d:%d:%d" % (days, hours % 60, minutes % 60, seconds % 60)
    if hours > 0:
        return "%d:%d:%d" % (hours % 60, minutes % 60, seconds % 60)
    if minutes > 0:
        return "%dm %ds" % (minutes % 60, seconds % 60)
    return "%ds" % seconds


def time_per_iter_human_readable(t):
    if t < 1:
        return "%.3f ops/sec" % (1.0 / t)
    return "%.3f sec per op" % t


class Stopwatch:
    def __init__(self, total_ops=None):
        self.then = time.time()
        self.initial_time = self.then
        self.queue = []
        self.done = 0
        self.total_ops = total_ops

    def tick(self):
        elapsed = time.time() - self.then
        self.done = self.done + 1
        self.then = time.time()
        return elapsed

    def total_time(self):
        return time.time() - self.initial_time

    def avg(self):
        return self.total_time() * 1.0 / self.done

    def status(self):
        if self.total_ops:
            return "{done} / {total}. " \
                   "{speed}. Expected end: {end}. " \
                   "Left: {left}. Spent: {spent}.".format(
                done=self.done,
                total=self.total_ops,
                speed=time_per_iter_human_readable(self.avg()),
                end=self.expected_end().strftime("%Y-%m-%d %H:%M:%S"),
                left=time_human_readable(self.eta()),
                spent=time_human_readable(self.total_time())
            )
        else:
            return "%d / ?. %s. Spent: %s." % (
                self.done,
                time_per_iter_human_readable(self.avg()),
                time_human_readable(self.total_time())
            )

    def tick_and_status(self):
        self.tick()
        return self.status()

    def eta(self):
        return (self.total_ops - self.done) * self.avg()

    def expected_end(self):
        return datetime.now() + timedelta(seconds=self.eta())


def my_tqdm_(generator, min_print_interval_sec=1.0, total=None):
    total_ops = total or (
        len(generator) if hasattr(generator, '__len__') else None)
    stopwatch = Stopwatch(total_ops)
    last_print = time.time()
    for e in generator:
        stopwatch.tick()
        if time.time() - last_print > min_print_interval_sec:
            print("\r" + stopwatch.status(), end='')
            last_print = time.time()
        yield e
    print("\r%s" % stopwatch.status())


class my_tqdm(object):
    def __init__(self, generator, min_print_interval_sec=1.0, total=None):
        self.generator = my_tqdm_(generator, min_print_interval_sec, total)
        self.total_ops = total or (
            len(generator) if hasattr(generator, '__len__') else None)

    def __len__(self):
        return self.total_ops

    def __iter__(self):
        return self.generator

    def __next__(self):
        return next(self.generator)

    # python 2 compatibility
    def next(self):
        return self.__next__()
