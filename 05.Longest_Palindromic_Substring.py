# Longest Palindromic Substring

# initial thoughts:
# find the centric of Palindrom
# then expand from that centric

class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        
        
        if s == "":
            return ""
        elif len(s) == 1:
            return s
        elif s[0] == s[1] and len(s) == 2:
            return s
        elif s[0] != s[1] and len(s) == 2:
            return s[0]

        else:
            dp = [s[0]]
            if s[0] == s[1]:
                dp.append(s[0:2])
            for i in range(2,len(s)):
                if s[i] == s[i-2]:
                    dp.append(s[i-2:i+1])
                   
                    j = 1 # expand step
                    while i+j < len(s) and i-2-j >= 0:
                        if s[i+j] == s[i-2-j]:
                            dp.append(s[i-2-j:i+1+j])
                            
                            j += 1
                        else:
                            break
                if s[i] == s[i-1]:
                    dp.append(s[i-1:i+1])
                    
                    j = 1 # expand step
                    
                    while i+j < len(s) and i-1-j >= 0:
                        if s[i+j] == s[i-1-j]:
                        
                            #print(s[i-1-j:i+1+j])
                            dp.append(s[i-1-j:i+1+j])
                            
                            j += 1
                        else:
                            break
        #print(dp)
        return max(dp,key = len)