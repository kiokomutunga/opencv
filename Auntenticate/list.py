class Solution(object):
    def countStrings(self, nums):
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] + nums[i + 1] == nums[i] / 2:
                count += 1
        return count

# Get input from the user (comma-separated)
input_list = input("Enter a list of numbers separated by commas (e.g., 4,6,8): ")
nums = list(map(int, input_list.split(',')))

# Create an instance of the class and call the method
sol = Solution()
print("Count:", sol.countStrings(nums))
