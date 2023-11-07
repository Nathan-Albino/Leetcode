class Solution(object):
    def productExceptSelf(self, nums):
      """
      :type nums: List[int]
      :rtype: List[int]
      """
       
      answer = []
        
      for i in range(0, len(nums)):
        leftSum = self.multiplyLeft(nums, i)
        # print(leftSum)
        rightSum = self.multiplyRight(nums, i)
        # print(rightSum)
        answer.append(leftSum * rightSum)

      return answer

    def multiplyLeft(self, nums, i):

      sum = 1

      for x in range(0, i): 
        
        sum *= nums[x]

      return sum


    def multiplyRight(self, nums, i):

      sum = 1

      for x in range(i + 1, len(nums)):

        sum *= nums[x]

      return sum

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))