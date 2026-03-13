import random

# Generate 10 random scores
scores = [random.randint(0, 100) for _ in range(10)]
print("Original Scores:", scores)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge two sorted halves
    sorted_arr = []
    i = j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    
    # Append any remaining elements
    sorted_arr.extend(left_half[i:])
    sorted_arr.extend(right_half[j:])
    
    return sorted_arr

# Sort the scores
sorted_scores = merge_sort(scores)
print("Sorted Scores:", sorted_scores)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0  # Count steps for illustration
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"Step {steps}: Checking index {mid} (score {arr[mid]})")
        
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Not found

# Ask user for a score to search
user_score = int(input("Enter a candidate score to find: "))

index = binary_search(sorted_scores, user_score)

if index != -1:
    print(f"Candidate with score {user_score} found at rank {index + 1}.")
else:
    print(f"Candidate with score {user_score} not found.")