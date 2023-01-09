class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        travel_days = set(days)

        @cache
        def dp(day):
            if day == 0:
                return 0

            if day not in travel_days:
                return dp(day-1)

            else: # it's a travel day
                with_1_day_pass = dp(day-1) + costs[0]
                with_7_day_pass = dp(max(day-7,0)) + costs[1]
                with_30_day_pass = dp(max(day-30,0)) + costs[2]
                
                return min(with_1_day_pass, with_7_day_pass, with_30_day_pass)

        return dp(days[-1])
