def outcomes():
    pass_credit = int(input('Please enter your credits at pass : '))
    defer_credit = int(input('Please enter your credits at defer : '))
    fail_credit = int(input('Please enter your credits at fail : '))

    if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
        print('Progress')

    if pass_credit == 100 and defer_credit == 20 and fail_credit == 0:
        print('Progress(module trailer)')

    if pass_credit == 100 and defer_credit == 0 and fail_credit == 20:
        print('Progress(module trailer)')

    if pass_credit == 80 and defer_credit == 40 and fail_credit == 0:
        print('Do not Progress - module retriever')

    if pass_credit == 80 and defer_credit == 20 and fail_credit == 20:
        print('Do not Progress - module retriever')

    if pass_credit == 80 and defer_credit == 0 and fail_credit == 40:
        print('Do not Progress - module retriever')

    if pass_credit == 60 and defer_credit == 60 and fail_credit == 0:
        print('Do not Progress - module retriever')

    if pass_credit == 60 and defer_credit == 40 and fail_credit == 20:
        print('Do not Progress - module retriever')

    if pass_credit == 60 and defer_credit == 20 and fail_credit == 40:
        print('Do not Progress - module retriever')

    if pass_credit == 60 and defer_credit == 0 and fail_credit == 60:
        print('Do not Progress - module retriever')

    if pass_credit == 40 and defer_credit == 80 and fail_credit == 0:
        print('Do not Progress - module retriever')

    if pass_credit == 40 and defer_credit == 60 and fail_credit == 20:
        print('Do not Progress - module retriever')

    if pass_credit == 40 and defer_credit == 40 and fail_credit == 40:
        print('Do not Progress - module retriever')

    if pass_credit == 40 and defer_credit == 20 and fail_credit == 60:
        print('Do not Progress - module retriever')

    if pass_credit == 40 and defer_credit == 0 and fail_credit == 80:
        print('Exclude')

    if pass_credit == 20 and defer_credit == 100 and fail_credit == 0:
        print('Do not Progress - module retriever')

    if pass_credit == 20 and defer_credit == 80 and fail_credit == 20:
        print('Do not Progress - module retriever')

    if pass_credit == 20 and defer_credit == 60 and fail_credit == 40:
        print('Do not Progress - module retriever')

    if pass_credit == 20 and defer_credit == 40 and fail_credit == 60:
        print('Do not Progress - module retriever')

    if pass_credit == 20 and defer_credit == 20 and fail_credit == 80:
        print('Exclude')

    if pass_credit == 20 and defer_credit == 0 and fail_credit == 100:
        print('Exclude')

    if pass_credit == 0 and defer_credit == 120 and fail_credit == 0:
        print('Do not Progress - module retriever')

    if pass_credit == 0 and defer_credit == 100 and fail_credit == 20:
        print('Do not Progress - module retriever')

    if pass_credit == 0 and defer_credit == 80 and fail_credit == 40:
        print('Do not Progress - module retriever')

    if pass_credit == 0 and defer_credit == 60 and fail_credit == 60:
        print('Do not Progress - module retriever')

    if pass_credit == 0 and defer_credit == 40 and fail_credit == 80:
        print('Exclude')

    if pass_credit == 0 and defer_credit == 20 and fail_credit == 100:
        print('Exclude')

    if pass_credit == 0 and defer_credit == 0 and fail_credit == 120:
        print('Exclude')


while True:
    print('-' * 100)
    outcomes()

print('-' * 100)




