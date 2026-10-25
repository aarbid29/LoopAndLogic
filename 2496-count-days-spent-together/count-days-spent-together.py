class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        #if arrivebob > leavealice return 0

        # afm = arriveAlice[0:2]
        # afd = leaveAlice[3:5]

        # bfm = arriveBob[0:2]
        # bfd = leavelice[3:5]

        #overlapping intervals 

        #max(arrive of bob , arrival of alice) - min(leave of allice ,leave of bob)

        if arriveAlice > leaveBob or arriveBob > leaveAlice:
            return 0

        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        start_month = int(start[0:2])
        start_day = int(start[3:5])

        end_month = int(end[0:2])
        end_day = int(end[3:5])

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        start_total = sum(month_days[:start_month - 1]) + start_day
        end_total = sum(month_days[:end_month - 1]) + end_day

        return end_total - start_total + 1  










        