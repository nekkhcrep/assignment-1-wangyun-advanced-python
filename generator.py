class Countdown:

    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

class EvenNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


class InfiniteCycle:

    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.lst[self.index]
        self.index +=1
        if self.index == len(self.lst):
            self.index =0
        return value
if __name__ == "__main__":
    print("Countdown(6):", list(Countdown(6)))
    print(("Evennumbers(15):"), list(EvenNumbers(15)))
    cycle_test = InfiniteCycle([1, 3, 1, 4])
    cycle_results = [next(cycle_test) for _ in range(10)]
    print("InfiniteCycle([1,3,1,4]) the first 10 times:", cycle_results)
