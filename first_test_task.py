from typing import List
def solution(nums: List[int]) -> List[List[int]]:
    res = []
    res_test = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i]*nums[j]*nums[k]
                if sum == 0:
                    res_test.append([(i,nums[i]), (j,nums[j]), (k,nums[k])])   
                    res.append([nums[i], nums[j], nums[k]]) 
    return res
print(solution([1,2,0,3,0,4]))
