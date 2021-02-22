'''
    Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.


'''

class Solution:
    def isSubsequence(self, s, t):
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
        return s_i == len(s)
    
    def findLongestWord(self, s, d):
        ans = ""
        for string in d:
            if self.isSubsequence(string, s):
                ans = min(ans, string, key = lambda x: (-len(x), x))
        return ans