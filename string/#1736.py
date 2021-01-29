class Solution:
    def maximumTime(self, time: str) -> str:
        newt = ''
        if time[0] == '?':
            if time[1] == '?':
                newt += '23'
            elif time[1] > '3':
                newt += '1' + time[1]
            else:
                newt += '2' + time[1]
        else:
            if time[1] == '?':
                if time[0] == '2':
                    newt += '23'
                else:
                    newt += time[0] + '9'
            else:
                newt += time[:2]
        newt += ':'
        if time[3] == '?':
            newt += '5'
        else:
            newt += time[3]
        if time[4] == '?':
            newt += '9'
        else:
            newt += time[4]
        return newt