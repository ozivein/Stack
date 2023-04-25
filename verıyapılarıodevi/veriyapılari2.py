num = int(input("Bir sayı girin: "))
stack = list(range(1, num+1))

def pop_from_stack(stack, num):
    if stack[-1] == num:
        return stack.pop()
    else:
        return None

def swap_first_and_last(stack):
    if len(stack) < 2:
        return stack
    else:
        stack[0], stack[-1] = stack[-1], stack[0]
        return stack
print(stack)  # [1, 2, 4, 5]
swap_first_and_last(stack)
print(stack)  # [5, 2, 4, 3, 2, 1 ]
