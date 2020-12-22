class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals)
        output = []
        current_interval = []
        for i in range(0, len(intervals)):
            if i == 0:
                current_interval = intervals[0]
            elif i == len(intervals) - 1:
                if current_interval[1] >= intervals[i][0]:
                    current_interval = [current_interval[0], max(current_interval[1], intervals[i][1])]
                    output.append(current_interval)
                    return output
                else:
                    output.append(current_interval)
                    output.append(intervals[i])
                    return output
            
            if current_interval[1] >= intervals[i+1][0]:
                current_interval = [current_interval[0], max(current_interval[1], intervals[i+1][1])]
            else:
                output.append(current_interval)
                current_interval = intervals[i+1]
                
        return output
