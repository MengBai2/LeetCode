# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        st = []
        lsub = 0
        msub = 0
        for char in s:
            if char not in st:
                st.append(char)    
            else:
                # find where it starts
                j = st.index(char)
                if j == len(st) - 1:
                    st = []
                else:
                    st = st[j+1:]     
                st.append(char)
            lsub = len(st)
            msub = max(lsub,msub)
        return msub