#Given an array "nums" containing n + 1 integers where each integer is between
# 1 and n (inclusive), prove that at least one duplicate number must exist.
#Assume that there is only one duplicate number, find the duplicate one.
#Constraints: Read only array ,complexity must be constant space & sub-quadratic time.
#There is only one duplicate number, but it may appear more than twice.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        else:
            slow = nums[0]
            fast = nums[0]

            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break

            slow = nums[0]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow

# Proof:

# Trivial by the Pigeonhole Principle, n + 1 objects cannot be placed
# into n holes without one of the holes having at least two objects.

# Solution:

# Solve by turning the array into a linked list (LL). If there are duplicate numbers,
# there will be a cycle present in the LL. Given that a duplicate number is guaranteed
# by the constraints, we can use Floyd's Tortoise and Hare Algorithm to locate both
# the beginning of the cycle and where the duplicate number is located in the LL.
# Instantiate a slow pointer (tortoise) and a fast pointer (hare). Move the slow pointer
# one element per "turn" and the fast pointer two elements per "turn" through the LL.
# When the two pointers collide, send the tortoise back to the beginning of the LL and
# keep the hare in the spot spot, but reduce his speed to the same as the tortoise.
# Start both pointers moving again and return the spot of their next collision.
# This spot is both the beginning of the cycle and also the duplicate number in the LL!
# Linear time complexity and constant space complexity. 
