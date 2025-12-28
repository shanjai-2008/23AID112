nums = [23, 67, 12, 89, 45, 3, 78, 56]

biggest = nums[0]
smallest = nums[0]

for n in nums:
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n

print("Biggest:", biggest)
print("Smallest:", smallest)
