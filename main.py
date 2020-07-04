import function

print('Witaj w programie liczącym samogłoski lub/i spółgłoski.')

while True:
    print('*'*80, end='')

    mode = input('Wybierz tryb, który ciebie interesuje:\nSamogłoski - Tryb 1'
                 '\nSpółgłoski - Tryb 2\nSamogłoski i Spółgłoski - Tryb 3'
                 '\nTwój Wybór (podaj cyfrę):\nTryb ')

    while True:
        try:
            print('*' * 80, end='')
            mode = int(mode)
            if 1 <= mode <= 3:
                break
        except ValueError:
            mode = input('Wstawiono niepoprawne dane, spróbuj raz jeszcze:\nTryb ')
        else:
            mode = input('Jako tryb musisz podać cyfrę 1, 2 lub 3\n')

    user_string = input('Podaj wyraz:\n')
    print('*' * 80, end='')

    if mode == 1:
        if function.count_vowels(user_string) >= 5 or function.count_vowels(user_string) == 0:
            print('W wyrazie {} jest {} samogłosek'.format(user_string, function.count_vowels(user_string)))
        else:
            print('W wyrazie {} są {} samogłoski'.format(user_string, function.count_vowels(user_string)))

    elif mode == 2:
        if function.count_consonants(user_string) >= 5 or function.count_consonants(user_string) == 0:
            print('W wyrazie {} jest {} spółgłosek'.format(user_string, function.count_consonants(user_string)))
        else:
            print('W wyrazie {} są {} spółgłoski'.format(user_string, function.count_consonants(user_string)))

    elif mode == 3:
        if (function.count_consonants(user_string) >= 5 or function.count_consonants(user_string) == 0) and \
                (function.count_vowels(user_string) >= 5 or function.count_vowels(user_string) == 0):

            print('W wyrazie {} jest {} spółgłosek i {} samogłosek'
                  .format(user_string, function.count_consonants(user_string), function.count_vowels(user_string)))

        elif function.count_consonants(user_string) < 5 and function.count_vowels(user_string) < 5:

            print('W wyrazie {} są {} spółgłoski i {} samogłoski'
                  .format(user_string, function.count_consonants(user_string), function.count_vowels(user_string)))

        else:
            if (function.count_consonants(user_string) >= 5 or function.count_consonants(user_string) == 0) and \
                    function.count_vowels(user_string) < 5:

                print('W wyrazie {} jest {} spółgłosek i {} samogłoski'
                      .format(user_string, function.count_consonants(user_string), function.count_vowels(user_string)))
            else:

                print('W wyrazie {} są {} spółgłoski i {} samogłosek'
                      .format(user_string, function.count_consonants(user_string), function.count_vowels(user_string)))

    print('*'*80, end='')
    Working = input('Czy chcesz podać kolejny wyraz?(T/N):\n').upper()
    if Working == 'N':
        break
