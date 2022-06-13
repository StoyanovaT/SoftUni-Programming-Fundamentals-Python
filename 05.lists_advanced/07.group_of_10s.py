def group_of_tens(nums):
    boundary = 10

    while len(nums) > 0:
        result = [num for num in nums if num <= boundary]
        print(f"Group of {boundary}'s: {result}")
        nums = [num for num in nums if num not in result]
        boundary += 10


numbers = list(map(int, input().split(", ")))
group_of_tens(numbers)
