while True:
    def write(txt):
        print(f'{len(txt) * '-'}')
        print(txt)
        print(f'{len(txt) * '-'}')


    given = str(input(' Type anything you want: '))
    write(given)
