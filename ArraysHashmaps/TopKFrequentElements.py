
class Solution(object):
  
  def topKFrequent(self, nums, k):

    freqMap = {}
    result_list = []

    for i in nums:
      
      if i in freqMap:
        freqMap[i] = freqMap[i] + 1
        
      else:
        freqMap[i] = 1

    sorted_freqMap = sorted(freqMap.items(), key=lambda x: x[1], reverse=True) 
    

    for i in range(k):
      result_list.append(sorted_freqMap[i][0])

    return result_list


solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3,5,5,5,5,5,5,5,5,5],2))
print(solution.topKFrequent([1], 1))
