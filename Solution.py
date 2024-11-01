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