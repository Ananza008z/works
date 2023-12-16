wordle = [str(c) for c in input()]
guess = [str(c) for c in input().split(' ')]
def show_result(result, guess_right, wrong):
    for k, line1 in enumerate(wordle):
        if k != len(wordle)-1:
            if line1 in guess_right:print(line1, end=' ')
            else:print('.', end=' ')
        else:
            if line1 in guess_right:print(line1)
            else:print('.')
    print('guessed:', ' '.join(wrong)) if len(wrong) != 0 else print('guessed: none')
    if result == '':
        return
    else: print(result)

guess_wrong = []
right = []
wrong = 0
for i, index in enumerate(guess):
    if index.upper() in wordle:right.append(index.upper())
    else:
        guess_wrong.append(index)
        wrong += 1
    
    if wrong > 5:
        show_result('John lose', right, guess_wrong)
        break
    elif len(set(right)) == len(set(wordle)):
        show_result('John win', right, guess_wrong)
    elif i == len(guess)-1 and len(right) != len(wordle):
        show_result('', right, guess_wrong)