def file_name(file_name):
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        print("File not found!")
    else:
        file_c = f.read()
        f.close()
        return file_c

file_name("Prince.txt")

# shte se realizira greshkata FileNotFound, zashtoto v tekushtata direktoriq ne sushtestvuva tozi fail, koito iskame da otvorim. Nie go zadavame kato parametur na metoda i po tozi nachin ako na negovo mqsto se zadade aktualen fail, programata shte go otvori i samo shte go prochete. Tova se zadava na 3 red v kavichkite "r". Poprincip mojem da si zadadem kakuv exception iskame da zasechem i taka da go printnem na ekrana.