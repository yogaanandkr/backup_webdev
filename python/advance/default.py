# # try:
# #     i = 1
# #     while True:
# #         print(i)
# #         i += 1
# # except:
# #     print("error handled")

# numbers = [47, 22, 81, 46, 94, 95, 90, 22, 55, 91, 6, 83, 49, 65, 10, 32, 41, 26, 83, 99, 14, 85, 42, 99, 89, 69, 30, 92, 32, 74, 9, 81, 5, 9]

# # Iterate through the list to find the pair summing up to 182
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == 182:
#             print(f"The pair [{numbers[i]}, {numbers[j]}] sums up to 182.")

def fact(n):
    ans = 1
    for i in range(n):
        ans = ans * n
        n -= 1
    return ans
print(fact(5))