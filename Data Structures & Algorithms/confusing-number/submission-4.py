class Solution:
    def confusingNumber(self, n: int) -> bool:
        num_map={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        n_str=str(n)
        res=""
        for i in reversed(n_str):
            if i not in num_map:
                return False
            res+=num_map[i]
        return n_str!=res
