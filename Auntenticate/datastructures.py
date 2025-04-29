class solution(object):
    def countStrings(self):
        nums = [4,6,8]
        
        count = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] + nums[i+1] == nums[1] /2:
                count += 1
        return count

print(solution().countStrings())   

