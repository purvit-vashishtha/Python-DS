class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    result = []
    curstring = ["("]
    
    def dfs(openparens, closingparens):
      if closingparens == n: result.append("".join(curstring))
      else:
        if openparens - closingparens > n:
          curstring.append(")")
          dfs(openparens,closingparens+1)
          curstring.pop()
        if openparens < n:
                    currString.append("(")
                    dfs(openparens+1, closingparens)
                    curstring.pop()
        dfs(1, 0)
        return result
