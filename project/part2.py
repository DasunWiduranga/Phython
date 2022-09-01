scores = [0, 20, 40, 60, 80, 100, 120]
while True:
    print('-' * 100)

    try:
        pass_credit = int(input('Please enter your credits at pass : '))
        if pass_credit not in scores:
            print('Out of range')
            break
        defer_credit = int(input('Please enter your credits at defer : '))
        if defer_credit not in scores:
            print('Out of range')
            break
        fail_credit = int(input('Please enter your credits at fail : '))
        if fail_credit not in scores:
            print('Out of range')
            break

        if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
            print('Progress')

        elif pass_credit == 100 and defer_credit == 20 and fail_credit == 0:
            print('Progress(module trailer)')

        elif pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
            print('Progress(module trailer)')

        elif pass_credit == 80 and defer_credit == 40 and fail_credit == 0:
            print('Do not Progress - module retriever')

        elif pass_credit == 80 and defer_credit == 20 and fail_credit == 20:
            print('Do not Progress - module retriever')

        elif pass_credit == 80 and defer_credit == 0 and fail_credit == 40:
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 60 and fail_credit == 0:
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 40 and fail_credit == 20:
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 20 and fail_credit == 40:
            print('Do not Progress - module retriever')

        elif pass_credit == 60 and defer_credit == 0 and fail_credit == 60:
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 80 and fail_credit == 0:
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 60 and fail_credit == 20:
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 40 and fail_credit == 40:
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 20 and fail_credit == 60:
            print('Do not Progress - module retriever')

        elif pass_credit == 40 and defer_credit == 0 and fail_credit == 80:
            print('Exclude')

        elif pass_credit == 20 and defer_credit == 100 and fail_credit == 0:
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 80 and fail_credit == 20:
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 60 and fail_credit == 40:
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 40 and fail_credit == 60:
            print('Do not Progress - module retriever')

        elif pass_credit == 20 and defer_credit == 20 and fail_credit == 80:
            print('Exclude')

        elif pass_credit == 20 and defer_credit == 0 and fail_credit == 100:
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 120 and fail_credit == 0:
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 100 and fail_credit == 20:
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 80 and fail_credit == 40:
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 60 and fail_credit == 60:
            print('Do not Progress - module retriever')

        elif pass_credit == 0 and defer_credit == 40 and fail_credit == 80:
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 20 and fail_credit == 100:
            print('Exclude')

        elif pass_credit == 0 and defer_credit == 0 and fail_credit == 100:
            print('Exclude')

        else:
            print('Exclude')

    except ValueError:
        print('Integer required')

    finally:
        continue
