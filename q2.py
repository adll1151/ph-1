def solution(numbers):
    sum = 0
    for i in range(1,10):
        if i not in numbers:
            sum += i  
    return sum
numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)