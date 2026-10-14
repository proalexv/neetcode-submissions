class Solution:
    def isValid(self, s: str) -> bool:
        openBraketStack = []
        for char in s: 
            if char in ["{", "(", "["]:
                openBraketStack.append(char)
            if len(openBraketStack) == 0: 
                return False
            elif char == "}":
                if len(openBraketStack) > 0 and openBraketStack.pop() != "{":
                    return False
            elif char == ")":
                if len(openBraketStack) and openBraketStack.pop() != "(":
                    return False
            elif char == "]":
                if len(openBraketStack) and openBraketStack.pop() != "[":
                    return False
        return len(openBraketStack) == 0 
