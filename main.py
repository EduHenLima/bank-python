from getpass import getpass
# coding=utf-8
#So de colocar o coding para utf-8 ele já padroniza os acentos. Python2 buga

print('********************************************')
print('***** School of Net - Caixa Eletrônico *****')
print('********************************************')

account_number = input('Info your account: ')
account_pass = getpass('Info your account: ')
print(account_number)
print(account_pass)

account_list = {
    '001':
        {
        'password' : '123',
        'name' : 'Eduardo',
        'value' : 0
        },
}
#Helper para verificar o pass da conta
pass_helper = account_list[account_number]['password']
if account_number in account_list and account_pass == pass_helper:
    print('temos uma conta')
else:
    print('não encontrada')
#Agencia,senha,nome,valor