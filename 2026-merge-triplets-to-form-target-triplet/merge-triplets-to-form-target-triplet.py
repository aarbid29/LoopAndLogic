class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        col1_set = set()
        col2_set = set()
        col3_set = set()

        for row in triplets:
            if row[0] <= target[0] and row[1] <= target[1] and row[2] <= target[2]:
                col1_set.add(row[0])
                col2_set.add(row[1])
                col3_set.add(row[2])

        if target[0] not in col1_set or target[1] not in col2_set or target[2] not in col3_set:
            return False

        return True