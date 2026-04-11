class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i, currTemp in enumerate(temperatures):
            days = 1
            print(i, days)
            
            for temp in temperatures[i + 1:]:
                if temp > currTemp:
                    res[i] = days
                    break
                else:
                    days += 1
                print(i, temp, days)
        
        return res