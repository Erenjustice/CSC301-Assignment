# 1. Recursion to sum the first 10 natural numbers
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

print("1. Sum of first 10 numbers =", recursive_sum(10))


# 2. Fibonacci series of 8 terms
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("2. Fibonacci series of 8 terms =", fibonacci(8))


# 3. Dynamic array simulation (capacity starts at 2)
class DynamicArray:
    def __init__(self):
        self.array = [None] * 2
        self.capacity = 2
        self.size = 0

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1

dyn = DynamicArray()
for val in [10, 20, 30, 40, 50]:
    dyn.insert(val)

print("3. Dynamic array contents:", dyn.array[:dyn.size])
print("   Final capacity:", dyn.capacity)


# 4. Linear search (target = 20)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr1 = [2, 5, 7, 10, 14, 20]
target1 = 20
print("4. Linear search index:", linear_search(arr1, target1))
print("   Time: O(n), Space: O(1)")


# 5. Binary search trace (target = 9)
def binary_search_trace(arr, target):
    low, high = 0, len(arr) - 1
    steps = []

    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high, arr[mid]))

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps

arr2 = [1, 3, 5, 7, 9, 11, 13]
target2 = 9
index, trace_steps = binary_search_trace(arr2, target2)

print("5. Binary search index:", index)
print("   Trace steps:")
for step in trace_steps:
    print("   low =", step[0], "mid =", step[1], "high =", step[2], "mid_value =", step[3])
print("   Time: O(log n), Space: O(1)")





