from collections import defaultdict
import heapq
import bisect

class TimeMap:

    def __init__(self):
        self.keyValueMap = defaultdict(list)
        self.keyTimestampMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyTimestampMap[key].append(timestamp)
        self.keyValueMap[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if not len(self.keyTimestampMap[key]):
            return ""
        idx = bisect.bisect_left(self.keyTimestampMap[key], timestamp)
        # print(self.keyTimestampMap[key], idx)
        if idx == 0 and self.keyTimestampMap[key][idx] == timestamp:
            return self.keyValueMap[key][idx]
        elif idx == 0 and self.keyTimestampMap[key][idx] > timestamp:
            return ""
        elif idx < len(self.keyTimestampMap[key]) and self.keyTimestampMap[key][idx] == timestamp:
             return self.keyValueMap[key][idx]
        else:
             return self.keyValueMap[key][idx-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)