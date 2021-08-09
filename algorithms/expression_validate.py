from datastructures.stack import Stack

opens = "([{"
closers = ")]}"


def is_valid_expression(expression):
    stack = Stack(len(expression))

    for symbol in expression:
        if symbol in opens:
            stack.insert(symbol)

        if symbol in closers:
            if not stack.is_empty():
                value = str(stack.remove())

                if opens.index(value) == closers.index(symbol):
                    continue

            return False

    if stack.is_empty():
        return True

    return False
