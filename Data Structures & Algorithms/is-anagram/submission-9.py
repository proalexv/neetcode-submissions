class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
             # return sorted(s) == sorted(t)
            freq_s = defaultdict(int)
            freq_t = defaultdict(int)
            for num_s, num_t in zip(s,t):
                freq_s[num_s] += 1
                freq_t[num_t] += 1
            return freq_s == freq_t
        else: 
            return False
        