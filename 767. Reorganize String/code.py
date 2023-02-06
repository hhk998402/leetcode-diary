import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        #Create the heap
        string_heap = [[-freq,c] for c,freq in Counter(s).items()]
        print(string_heap)
        heapq.heapify(string_heap)
        res = ""
        prev_char = None
        while(string_heap or prev_char):
            print(prev_char, res)
            #Only one set of character remaining, so will repeat
            if not string_heap and prev_char:
                return ''
            freq,c = None, None
            if(string_heap):
                freq,c = heapq.heappop(string_heap)
            if freq != None:
                res += c
                freq += 1 #One char consumed
                if(prev_char):
                    heapq.heappush(string_heap,prev_char)
                    prev_char = None
                if freq != 0:
                    prev_char = [freq,c]
        return res
