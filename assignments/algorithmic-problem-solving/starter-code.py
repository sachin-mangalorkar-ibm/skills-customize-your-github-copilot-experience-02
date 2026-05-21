"""Starter code for Algorithmic Problem Solving assignment.

Complete each function and run this file to check your output.
"""


def count_frequencies(numbers):
    """Return a dictionary mapping each number to its count."""
    # TODO: Implement this function.
    return {}


def find_duplicates(numbers):
    """Return a sorted list of values that appear more than once."""
    # TODO: Implement this function.
    return []


def top_students(scores, threshold):
    """Return alphabetically sorted student names with score >= threshold."""
    # TODO: Implement this function.
    return []


if __name__ == "__main__":
    sample_numbers = [3, 1, 2, 3, 2, 3, 5, 1]
    sample_scores = {
        "Amira": 92,
        "Jon": 78,
        "Lina": 88,
        "Marco": 95,
        "Priya": 88,
    }

    print("Task 1 - Frequency Counter")
    print(count_frequencies(sample_numbers))

    print("\nTask 2 - Duplicates")
    print(find_duplicates(sample_numbers))

    print("\nTask 3 - Top Students (threshold = 88)")
    print(top_students(sample_scores, 88))