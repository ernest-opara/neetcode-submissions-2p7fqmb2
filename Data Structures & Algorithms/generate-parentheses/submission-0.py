class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        def generate(l,r, path):
            if l > n or r > n or r > l:
                return

            if l == n and r == n:
                combinations.append(path)

            generate(l+1,r,path + "(")
            generate(l, r+1, path + ")")
        
        generate(0,0,"")
        return combinations
            
            