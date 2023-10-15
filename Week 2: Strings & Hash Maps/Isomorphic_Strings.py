class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for nums in range(len(s)):
            if s[nums] in a:
                if a.get(s[nums]) != t[nums]:
                    print("false")
                    return False
            if t[nums] in b:        
                if b.get(t[nums]) != s[nums]:
                    print("false")
                    return False
            a.update({s[nums]:t[nums]})
            b.update({t[nums]:s[nums]})
        print("True")
        return True    
