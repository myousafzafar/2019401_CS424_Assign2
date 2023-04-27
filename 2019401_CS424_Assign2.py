
#2019401 CS424 Assignment 2 - The LR(1) Parser

# The LR(1) Parsing Table
lr1_table = {
    0: {'id': 's4', '-': 's3', '*': 's5'},
    1: {'$': 'acc'},
    2: {'-': 'r2', '$': 'r2', 'id': 'r2', '*': 'r2'},
    3: {'id': 's4', '-': 's3', '*': 's5'},
    4: {'$': 'r4', '-': 'r4', 'id': 'r4', '*': 'r4'},
    5: {'id': 's4', '-': 'r1', '$': 'r1', '*': 'r1'},
    6: {'id': 'r3', '-': 'r3', '$': 'r3', '*': 'r3'}
}

# Productions
productions = {
    1: ['E', 'E', '-', 'T'],
    2: ['E', 'T'],
    3: ['T', 'T', '*', 'F'],
    4: ['T', 'F'],
    5: ['F', 'id']
}

#LR(1) parser
def lr1_parser(input_string):
    stack = [0]
    input_list = input_string.split()
    i = 0
    while True:
        state = stack[-1]
        lookahead = input_list[i]
        action = lr1_table[state].get(lookahead)
        if action is None:
            return False
        elif action == 'acc':
            return True
        elif action[0] == 's':
            stack.append(int(action[1:]))
            i += 1
            print(stack, input_list[i:], "Shift", lookahead)
        elif action[0] == 'r':
            prod_num = int(action[1:])
            rhs_len = len(productions[prod_num]) - 1
            for j in range(rhs_len):
                stack.pop()
            state = stack[-1]
            lhs = productions[prod_num][0]
            stack.append(int(lr1_table[state][lhs]))
            print(stack, input_list[i:], "Reduce", productions[prod_num])
        else:
            return False

# Input string "a b c d"
input_string = "a b c d"
stack = [0]
input_list = input_string.split()
i = 0
print("Stack    Input   Action")

while True:
    state = stack[-1]
    lookahead = input_list[i]
    action = lr1_table[state].get(lookahead)
    if action is None:
        print(stack,  input_list[i:], "Error")
        break
    elif action == 'acc':
        print(stack,  input_list[i:], "Accept")
        break
    elif action[0] == 's':
        stack.append(int(action[1:]))
        i += 1
        print(stack,  input_list[i:], "Shift", lookahead)
    elif action[0] == 'r':
      prod_num = int(action[1:])
      rhs_len = len(productions[prod_num]) - 1
    for j in range(rhs_len):
        stack.pop()
    state = stack[-1]
    lhs = productions[prod_num][0]
    stack.append(int(lr1_table[state][lhs]))
    print(stack, input_list[i:], "Reduce", productions[prod_num])

