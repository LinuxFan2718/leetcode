# google code jam for women
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000005102c
# https://code.google.com/codejam/contest/8384486/dashboard#s=p0

class Solution:
    # employee_levels = [
    #   [num_employees, level],
    #   [num_employees, level],
    #   [num_employees, level]
    # ]
    # returns minimum possible experience level for the new CEO
    def ceoSearch(self, employee_levels):
        # two constraints. return max() of these two constraints.
        # 1. ceo level must be > than highest existing level
        outrank_highest_existing = 1 + max([x[1] for x in employee_levels])
        # 2. ceo level must be large enough to handle overflow reports 
        #    from lower levels and all highest level employees

        # assume these are sorted with lowest levels first
        reports_need_managers = 0
        for employee_level in employee_levels:
            num_employees = employee_level[0]
            level = employee_level[1]
            reports_capacity = num_employees * level
            overflow_reports = reports_need_managers - reports_capacity
            reports_need_managers = num_employees + overflow_reports

        return max(outrank_highest_existing, reports_need_managers)

solution = Solution()
num_test_cases = int(input())
for test_case in range(1, 1 + num_test_cases):
    num_experience_levels = int(input())
    employee_levels = []
    for i in range(0, num_experience_levels):
        num_employees, level = [int(x) for x in input().split(' ')]
        employee_levels.append([num_employees, level])
    min_experience_level = solution.ceoSearch(employee_levels)
    print("Case #", test_case, ": ", min_experience_level, sep='')
