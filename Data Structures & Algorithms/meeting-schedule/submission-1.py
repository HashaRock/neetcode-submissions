"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intvs = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intvs[i - 1].end > intvs[i].start:
                return False
        
        return True

