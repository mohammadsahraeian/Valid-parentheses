open_list = ["(", "[", "{"]
close_list = [")", "]", "}"]

def check(string):
    stack = []
    for sign in string:
        if sign in open_list:
            stack.append(sign)
        elif sign in close_list:
            close_index = close_list.index(sign)
            if len(stack) > 0 and (open_list[close_index] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Invalid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"

first = '({([])}{[}])'
print(check(first))
second = '{({)}}'
print(check(second))
third = '[{([()])}]'
print(check(third))
