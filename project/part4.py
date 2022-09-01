scores = [0, 20, 40, 60, 80, 100, 120]
student_count = {
    'progress': 0,  # progress
    'trailer': 0,  # progress (module trailer)
    'retriever': 0,  # do not progress - module retriever
    'exclude': 0,  # exclude
    'total': 0,  # total
}


def increment(var):
    student_count[var] = student_count[var] + 1
    student_count['total'] = student_count['total'] + 1


def decrement(var):
    student_count[var] = student_count[var] - 1
    student_count['total'] = student_count['total'] - 1


while True:
    print('-' * 100)

    try:
        pass_credit = int(input('Please enter your credits at pass : '))
        if pass_credit not in scores:
            print('Out of range')
            continue
        defer_credit = int(input('Please enter your credits at defer : '))
        if defer_credit not in scores:
            print('Out of range')
            continue
        fail_credit = int(input('Please enter your credits at fail : '))
        if fail_credit not in scores:
            print('Out of range')
            continue

        if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
            increment('progress')
            print('Progress')

        elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0:
            increment('trailer')
            print('Progress(module trailer)')

        elif pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
            increment('trailer')
            print('Progress(module trailer)')

        elif pass_credit == 80 and defer_credit == 40 and fail_credit == 0:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 80 and defer_credit == 20 and fail_credit == 20:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 80 and defer_credit == 0 and fail_credit == 40:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 60 and fail_credit == 0:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 40 and fail_credit == 20:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 20 and fail_credit == 40:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 0 and fail_credit == 60:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 80 and fail_credit == 0:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 60 and fail_credit == 20:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 40 and fail_credit == 40:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 20 and fail_credit == 60:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 0 and fail_credit == 80:
            increment('exclude')
            print('Exclude')

        elif pass_credit == 20 and defer_credit == 100 and fail_credit == 0:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 80 and fail_credit == 20:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 60 and fail_credit == 40:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 40 and fail_credit == 60:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 20 and fail_credit == 80:
            increment('exclude')
            print('Exclude')

        elif pass_credit == 20 and defer_credit == 0 and fail_credit == 100:
            increment('exclude')
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 120 and fail_credit == 0:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 100 and fail_credit == 20:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 80 and fail_credit == 40:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 60 and fail_credit == 60:
            increment('retriever')
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 40 and fail_credit == 80:
            increment('exclude')
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 20 and fail_credit == 100:
            increment('exclude')
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 0 and fail_credit == 170:
            increment('exclude')
            print('Exclude')

        else:
            print('Exclude')

        command = input('Would you like to enter another set of data? \n'
                        'Enter \'y\' for yes or \'q\' to quit and view results: ')
        if command == 'y':
            continue
        else:
            print('----------------------------------------------------------')
            print('Progress \t Trailer \t Retriever \t Exclude')
            while student_count['total'] != 0:
                statement = ''
                if student_count['progress'] > 0:
                    statement += '* '
                    decrement('progress')
                statement += '\t \t '
                if student_count['trailer'] > 0:
                    statement += '* '
                    decrement('trailer')
                statement += '\t \t '
                if student_count['retriever'] > 0:
                    statement += '* '
                    decrement('retriever')
                statement += '\t \t '
                if student_count['exclude'] > 0:
                    statement += '*'
                    decrement('exclude')
                print(statement)
            print('----------------------------------------------------------')
            break

    except ValueError:
        print('Integer required')
