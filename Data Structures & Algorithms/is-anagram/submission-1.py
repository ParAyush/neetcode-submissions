class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for char in s:
            if char in s_freq:
                s_freq[char] +=1

            else:
                s_freq[char] = 1

        
        for char in t:
            if char in t_freq:
                t_freq[char] +=1

            else:
                t_freq[char] = 1

        s_sorted = dict(sorted(s_freq.items()))
        t_sorted = dict(sorted(t_freq.items()))

        for chars in s_sorted:
            if (s_sorted == t_sorted):
                return True
            else:
                return False
        
            


