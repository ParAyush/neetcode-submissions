class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_t = {}
        seen_s = {}

        for x in t:
            if x in seen_t:
                seen_t[x] +=1
                continue
            else:
                seen_t[x] =1

        for x in s:
            if x in seen_s:
                seen_s[x] +=1
                continue
            else:
                seen_s[x] =1            


        if seen_t == seen_s:
            return True
        else:
            return False    

            



            



        