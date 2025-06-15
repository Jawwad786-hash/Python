print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
from __future__ import print_function, division
class Time:
    """Represents the time of day as seconds since midnight."""
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour * 3600 + minute * 60 + second
    def __str__(self):
        h, rem = divmod(self.seconds, 3600)
        m, s = divmod(rem, 60)
        return '%.2d:%.2d:%.2d' % (h, m, s)
    def print_time(self):
        print(str(self))
    def time_to_int(self):
        """Returns seconds since midnight."""
        return self.seconds
    def is_after(self, other):
        return self.seconds > other.seconds
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
        return self.__add__(other)
    def add_time(self, other):
        assert self.is_valid() and other.is_valid()
        return int_to_time(self.seconds + other.seconds)
    def increment(self, seconds):
        return int_to_time(self.seconds + seconds)
    def is_valid(self):
        return 0 <= self.seconds < 24 * 3600
def int_to_time(seconds):
    """Creates a Time object from seconds since midnight."""
    return Time(0, 0, seconds)
def main():
    start = Time(9, 45, 0)
    start.print_time()
    end = start.increment(1337)
    end.print_time()
    print('Is end after start?')
    print(end.is_after(start))
    print('Using __str__')
    print(start, end)
    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)
    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)
if __name__ == '__main__':
    main()
