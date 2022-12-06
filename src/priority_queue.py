import heapq
import time
from dataclasses import field, dataclass
from typing import Any


@dataclass(order=True)
class QueueItem:
    data: Any = field(compare=False)
    delay_sec: int


class Queue:
    def __init__(self, unix_time: int):
        self.store = []
        self.unix_time = unix_time

    def __len__(self):
        return len(self.store)

    def get(self):
        return heapq.heappop(self.store)

    def put(self, data: Any, delay_sec: int = 0):
        heapq.heappush(self.store, QueueItem(data, delay_sec))


if __name__ == '__main__':
    unix = int(time.time())
    q = Queue(unix)

    q.put("a", 9)
    q.put("mahhhhh", 10)
    q.put("b", 3)
    q.put("c", 400)
    q.put("5 ", 7)
    q.put("4", 2)
    q.put("4")

    for i in range(len(q)):
        print(q.get())
