# 两数之和
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
'''
# 常规思路
'''
从num[0]遍历，每个循环找target-num[i]，找到则返回下标
'''
def twoSum(num, target):
    lens = len(num)
    j = -1
    for i in range(1, lens):# 遍历数组 只需要找到target-num[i]则说明是有解的
        temp = num[:i]
        if(target - num[i]) in temp:# 找到了
            j = temp.index(target - num[i])
            break
    if j >= 0:
        return [j, i]

# 字典模拟哈希过程
'''
为input建立字典的形式，通过下标来找答案
'''
def twoSum1(num, target):
    hashmap = {}
    # 建立字典
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return[i, j]
    '''
    可以进行优化
    hashmap = {}
    for i, num in enumerate(nums):
    在建立索引的过程中就可以找了
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i
    '''

nums = [2, 7, 15, 11]
target = 9
twoSum(nums, target)
twoSum1(nums, target)
