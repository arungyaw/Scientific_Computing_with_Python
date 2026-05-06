def arithmetic_arranger(problems, show_answers=False):
    # if more than 5 problems are given, stop and return this error.
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Thses variables store each row of the final output.
    first_line = ''
    second_line = ''
    dashes = ''
    answers = ''
    
    
    #Go through each math problem one at a time.
    for problem in problems:
        #Example: "32 + 698 becomes:
        # first = 32, operator = + , second = 698
        first, operator, second = problem.split()
        
        # only + and - are allowed.
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        #Both numbers must contain digits only.
        # Example: "698" is valid , but "6a5" is not valid
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        
        #Each niumber can be at most 4 digits long.
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        #width is the total space needed for one problem.
        # We take the longer number and add 2:
        # 1 space for the operator and 1 space between operator and number.
        #
        # Example:
        # first = "32"
        #second = "698"
        #longest length = 3
        #width = 3 + 2 = 5
        
        width = max(len(first), len(second)) + 2
        
        #rjust(width) means "right-align inside this many spaces.
        # Example:
        #"32".rjust(5) becomes "   32"
        #So the first number lines up correctly on the right.
        # The '    ' adds 4 space between separate problems.

        first_line += first.rjust(width) + '    '
        second_line += operator + second.rjust(width -1) + '    '
        #Make the dash line the same width as the problem.
        #Example:
        #width = 5
        # '-'*5 becomes '_____'
        dashes += "-" * width + '    '

        if operator == '+':
            result = int(first) + int(second)
        else:
            result = int(first) - int(second)
        
        answers += str(result).rjust(width) + '    '
        
        #rstrip removes the extra space at the end of each row.

    arranged = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()

    if show_answers:
        arranged += '\n' + answers.rstrip()

    return arranged

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')