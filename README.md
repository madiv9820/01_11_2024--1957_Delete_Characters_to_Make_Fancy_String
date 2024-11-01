# Approach to Creating a Fancy String: Handling Consecutive Duplicates

- ### Intuition 
    - The goal is to create a new string from the given input string such that no character appears more than twice consecutively. If a character appears three or more times in a row, we only want to keep two of them in the resulting string.

- ### Approach
    1. **Initialization**: Start with an empty string `new_s`, an index to track the current character, and the length of the input string.
    2. **Iterate through the string**: Use a loop to traverse each character of the string:
        - Add the current character to `new_s`.
        - Use a temporary index to count consecutive occurrences of the current character.
        - If the count exceeds 2, add the character once more to ensure that only two consecutive occurrences are kept.
    3. **Update the index**: Move the main index to the next different character.
    4. **Return the result**: Finally, return the modified string.

- ### Time Complexity
    - The time complexity of this approach is **O(n)**, where `n` is the length of the input string. Each character is processed a constant number of times, resulting in linear time complexity.

- ### Space Complexity
    - The space complexity is **O(n)** as well, in the worst case, where the output string `new_s` may end up being of the same length as the input string if there are no consecutive duplicates. This includes the space used to store the new string.

- ### Code
    ```python3 []
    class Solution:
        def makeFancyString(self, s: str) -> str:
            new_s, index, n = '', 0, len(s)  # Initialize the new string, the current index, and the length of the input string.

            # Loop through the input string until the end
            while index < n:
                new_s += s[index]  # Add the current character to the new string.
                temp_index = index + 1  # Set a temporary index to check for consecutive characters.

                # Count consecutive characters that are the same
                while temp_index < n and s[temp_index] == s[index]:
                    temp_index += 1  # Move to the next index while the characters are the same.

                # If more than one consecutive character is found, add it only once
                if temp_index - index > 1:
                    new_s += s[index]  # Add the current character again to new_s to keep at most two consecutive characters.

                index = temp_index  # Move to the next different character.

            return new_s  # Return the modified string with at most two consecutive characters.
    ```