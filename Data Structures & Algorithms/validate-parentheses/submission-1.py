class Solution:
    def isValid(self, s: str) -> bool:
        pMap={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in pMap:
                if stack and stack[-1]==pMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False 


            