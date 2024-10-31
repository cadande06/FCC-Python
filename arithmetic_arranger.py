def arithmetic_arranger(problems, show_answers=False):
#problems must be <= 5
    if len(problems)>5:
        print('Error: Too many problems.')
        return 'Error: Too many problems.'
#creating lists for diff parts of equation
    first_operands=[]
    operators=[]
    second_operands=[]
    answers=[]
    max_widths=[] 
#splitting problems into smaller parts
    for problem in problems:
        parts=problem.split()
#making sure of length of parts
        if len(parts) != 3:
            print('Error: Invalid format.')
            return 'Error: Invalid format.'
        first_operand, operator, second_operand = parts
# making sure of correct operators
        if operator not in ['+', '-']:
            print("Error: Operator must be '+' or '-'.") 
            return "Error: Operator must be '+' or '-'."
#making sure of numbers        
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
#making sure digits<=4
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
#appending operands and operators       
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
#calculation and appending
        if operator == '+':
            answer = str(int(first_operand) + int(second_operand))
        elif operator == '-':
            answer = str(int(first_operand) - int(second_operand))
        
        answers.append(answer)
        max_widths.append(max(len(first_operand), len(second_operand)) + 2)
    
    first_line = ''
    second_line = ''
    dashes_line = ''
    answers_line = ''
#indexes for problems and formatting
    for i in range(len(problems)):
        width = max_widths[i]
        first_line += first_operands[i].rjust(width) + '    '
        second_line += operators[i] + ' ' + second_operands[i].rjust(width - 2) + '    '
        dashes_line += '-' * width + '    '
        if show_answers:
            answers_line += answers[i].rjust(width) + '    '
    
    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes_line.rstrip()
    
    if show_answers:
        arranged_problems += '\n' + answers_line.rstrip()
    
    return arranged_problems





print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')