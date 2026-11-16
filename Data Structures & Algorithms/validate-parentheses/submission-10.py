class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for c in s: 
            if c == '{' or c == '[' or c=='(':
                lst.append(c)
            elif (c== ']' or c=='}' or c == ')'):
                tmp=''
                if len(lst)!=0:
                    tmp = lst.pop()
                if tmp == None:
                    return False
                if c == ']':
                    if tmp != '[':
                        return False
                elif c == '}':
                    if tmp != '{':
                        return False
                elif c == ')':
                    if tmp != '(':
                        return False
        if len(lst)==0:
            return True
        return False



        