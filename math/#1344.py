class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hang = minutes * 30 / 60
        else:
            hang = hour * 30 + minutes * 30 / 60
        mang = minutes * 360 / 60
        # print(hang, mang)
        a = abs(mang - hang)
        return a if a <= 180 else 360 - a