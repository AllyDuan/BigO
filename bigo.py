"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, ALLY DUAN and <FULL NAME>, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: amd6894
UT EID 2:
"""



def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """

    max_length = 0   
    for start_index in range(len(s)):
        for current_index in range(start_index + 1, len(s) + 1):
            sub_string = s[start_index:current_index]
            repeating = False
            for char in range(len(sub_string) - 1):
                if sub_string[char] in sub_string[char + 1:]:
                    repeating = True
                    break

            if not repeating and len(sub_string) > max_length:
                max_length = len(sub_string)

    return max_length


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0

    start_index = 0
    length = len(s)
    for current_index in range(start_index, length):
        current_length = 0
        frequency_list = [0] * 256

        for temp_index in range(current_index, length):
            index = ord(s[temp_index])

            if frequency_list[index] >= 1:
                break           
            frequency_list[index] += 1
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length


def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a sliding window approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0
    length = len(s)
    for start_index in range(length):
        frequency_list = [0] * 256
        for current_index in range(start_index, length):
            index = ord(s[current_index])                          
            if frequency_list[index] >= 1:
                break

            frequency_list[index] += 1

            max_length = max(max_length, current_index - start_index + 1)

    return max_length
