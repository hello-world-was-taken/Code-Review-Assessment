def is_valid_parenthesis(s):
    parntehisis = {
        '(': ')','{': '}','[': ']' }
    stack = []
    for element in s:
        if element in parntehisis.keys(): stack.append(i)
        else:
            if len(stack) == 0:
                return False
            

            poped = stack.pop()
            if parntehisis[poped] != element:
                return False
    if len(stack) != 0:
        return False
    
    return True