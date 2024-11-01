# 1957. Delete Characters to Make Fancy String

__Type:__ Easy <br>
__Topics:__ String <br>
__Companies:__ Wayfair <br>
__Leetcode Link:__ [Delete Characters to Make Fancy String](https://leetcode.com/problems/delete-characters-to-make-fancy-string)
<hr>

A __fancy string__ is a string where no __three consecutive__ characters are equal.

Given a string `s`, delete the minimum possible number of characters from `s` to make it __fancy__.

Return _the final string after the deletion_. It can be shown that the answer will always be __unique__.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ s = "leeetcode" <br>
__Output:__ "leetcode" <br>
__Explanation:__ <br>
Remove an 'e' from the first group of 'e's to create "leetcode". <br>
No three consecutive characters are equal, so return "leetcode".

- __Example 2:__ <br>
__Input:__ s = "aaabaaaa" <br>
__Output:__ "aabaa" <br>
__Explanation:__ <br>
Remove an 'a' from the first group of 'a's to create "aabaaaa". <br>
Remove two 'a's from the second group of 'a's to create "aabaa". <br>
No three consecutive characters are equal, so return "aabaa".

- __Example 3:__ <br>
__Input:__ s = "aab" <br>
__Output:__ "aab" <br>
__Explanation:__ No three consecutive characters are equal, so return "aab".
<hr>

### Constraints:
- <code>1 <= s.length <= 10<sup>5</sup></code>
- `s` consists only of lowercase English letters.

### Hints:
- What's the optimal way to delete characters if three or more consecutive characters are equal?
- If three or more consecutive characters are equal, keep two of them and delete the rest.