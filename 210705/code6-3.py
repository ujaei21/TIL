def isStackFull():
    global size,stack,top
    if (top >= size-1):
        return True
    else:
        return False


def push(data):
    global size, stack, top
    if isStackFull():
        print('Stack is Full')
        return
    top += 1
    stack[top] = data


def isStackEmpty():
    global size, stack, top
    if top == -1:
        return True
    else:
        return False


def pop():
    global size, stack, top
    #  비었는지 확인
    if isStackEmpty():
        print('Stack is Empty')
        return None
    #  데이터 추출해서 리턴
    data=stack[top]
    stack[top] = None
    top -= 1
    return data
size = 5
# stack=[None  for _ in range(size)]
stack=['커피', '녹차', '꿀물', '콜라', None]
top = 3

print(stack)
push('환타')
print(stack)
push('사이다')

retData = pop()
print('pop()-->'+retData)
print(stack)