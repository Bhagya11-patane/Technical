from collections import Counter

def min_deletions_and_insertions(str1, str2):
    # Count frequency of each character in both strings
    freq1 = Counter(str1)
    freq2 = Counter(str2)
    
    # Initialize deletion and insertion counts
    deletion_count = 0
    insertion_count = 0
    
    # Characters in str1 that are not in str2
    for char in freq1:
        if char in freq2:
            # Calculate deletions if there's a surplus in str1
            deletion_count += max(0, freq1[char] - freq2[char])
        else:
            # All occurrences of char in str1 need to be deleted
            deletion_count += freq1[char]
    
    # Characters in str2 that are not in str1
    for char in freq2:
        if char in freq1:
            # Calculate insertions if there's a shortage in str1
            insertion_count += max(0, freq2[char] - freq1[char])
        else:
            # All occurrences of char in str2 need to be inserted
            insertion_count += freq2[char]

    return deletion_count, insertion_count

# Example usage
str1 = "heap"
str2 = "pea"
deletion_count, insertion_count = min_deletions_and_insertions(str1, str2)

print(f"Minimum Deletion = {deletion_count}")
print(f"Minimum Insertion = {insertion_count}")
