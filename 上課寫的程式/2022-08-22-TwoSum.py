# class Solution:
#     def twoSum(self, nums, target) :
#         list1 = []
#         for n,item1 in enumerate(nums) :
#             for m,item2 in enumerate(nums[n+1:],start=n+1):
#                 if item1 + item2 == target :
#                     list1.append(n)
#                     list1.append(m)
#                     return list1
#
# obj1 = Solution()
# list1 = obj1.twoSum([2,7,11,15],9)
# print(list1)

class Solution:
    def twoSum(self, nums, target) :
        dict1 = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[target-nums[i]],i]

obj1 = Solution()
list1 = obj1.twoSum([2,7,11,15],22)
print(list1)