def generateParentheses(n):
    result = []
    def generate(open_rem, close_rem, current_string):
        if open_rem == 0 and close_rem == 0:
            result.append(current_string)
            return

        if open_rem > 0:
            generate(open_rem - 1, close_rem, current_string + "(")

        if close_rem > 0 and close_rem > open_rem:
            generate(open_rem, close_rem - 1, current_string + ")")

    generate(n, n, "")
    return result

print(generateParentheses(3))
