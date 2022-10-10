class Solution:
    def rank(self, nums) :
        rank_list = []
        flag = 1
        for i in range(0,len(nums)):
            if i == 0 :
                rank_list.append(1)
            else :
                if nums[i-1] > nums[i] :
                    flag = i + 1
                    rank_list.append(i+1)
                else :

                    rank_list.append(flag)
        return rank_list

obj1 = Solution()
list1 = obj1.rank([80,78,77,72,72,72,68,68,60]) # [1, 2, 3, 4, 4, 4, 7, 7, 9]
print(list1)