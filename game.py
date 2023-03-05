#importações de bibliotecas
from random import randint
from time import sleep

#criação da classe principal
class App:
    def __init__(self):
        #laço principal
        while True:
            print('-'*30)
            print('[1] - JOGO PAR OU ÍMPAR\n'
                '[2] - JOGO DA ADIVINHAÇÃO\n'
                '[3] - JOKENPO\n'
                '[4] - TABUADA\n'
                '[5] - CAlCULADORA\n'
                '[0] - \033[31mEncerrar programa!\033[m')
            print('-'*30)
            self.choice_app = int(input('Escolha um app: '))
            self.stop = self.choice_games(self.choice_app)
            if self.stop == True:
                break
            
    def choice_games(self, game):
        while game > 5:
            game = int(input('Selecção inválida, Escolha um app:'))
        if game == 1:
            ParImpar()
        if game == 2:
            Adivinhacao()
        if game == 3:
            Jokenpo()
        if game == 4:
            Tabuada()
        if game == 5:
            Calculadora()
        if game == 0:
            return True


class ParImpar:
    def __init__(self):
        #declaração de variáveis
        self.acertos = 0

        #instruções do jogo
        print('-=-' * 15)
        print('PAR OU ÍMPAR: JOGO')
        print('-=-' * 15)
        print('')
        print('Instruções: Digite um valor para ser somado ao valor que o computador vai escolher.\n'
              'Depois tente adivinhar se o valor resultante é par ou ímpar.\n'
              'Enquanto você acertar o jogo continuará, e só se encerrá quando você perder.')
        print('')

        #laço principal
        while True:
            self.final = self.escolhas()
            self.choice_PI = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
            while self.choice_PI not in 'PI':
                self.choice_PI = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
            stop = self.verificador()
            if stop == True:
                break
        print(f'você acertou {self.acertos} vezes!')

    def verificador(self):
        if self.final % 2 == 0 and self.choice_PI == 'P':
            print(f'Você acertou, o computador escolheu {self.sort_pc} e você {self.player_number}, logo {self.result} é Par.')
        elif self.final % 2 == 0 and self.choice_PI == 'I':
            print(f'Você errou, o computador escolheu {self.sort_pc} e você {self.player_number}, logo {self.result} é Par.')
            return True
        elif self.final % 2 != 0 and self.choice_PI == 'P':
            print(f'Você errou, o computador escolheu {self.sort_pc} e você {self.player_number}, logo {self.result} é Ímpar.')
            return True
        elif self.final % 2 != 0 and self.choice_PI == 'I':
            print(f'Você acertou, o computador escolheu {self.sort_pc} e você {self.player_number}, logo {self.result} é Ímpar .')
        self.acertos += 1

    def escolhas(self):
        self.sort_pc = randint(1, 10)
        self.player_number = int(input('Digite um valor para jogar: '))
        self.result = self.sort_pc + self.player_number
        return self.result

class Adivinhacao:
    def __init__(self):
        self.sort_pc = randint(0, 10)
        self.acerto = False
        self.tentativas = 0
        while not self.acerto:
            self.choice_adv = int(input('Tente acertar o número que o computador vai pensar, de 0 a 10: '))
            self.verificador(self.choice_adv)
        print('\033[34mParabéns você acertou!\033[m')
        print(f'Você precisou de {self.tentativas} tentativas')

    def verificador(self, numb):
        if numb == self.sort_pc:
                self.acerto = True
        else:
            if numb > self.sort_pc:
                print('')
                print('\033[31mMenos amigão, tente novamente!\033[m')
                print('')
            elif numb < self.sort_pc:
                print('')
                print('\033[31mMais amigão, tente novamente\033[m')
                print('')
        self.tentativas += 1

class Jokenpo:
    def __init__(self):
        #declaração de variáveis
        self.sort_pc = randint(1, 3)
        #loop principal
        print('Escolha pedra papel ou tesoura:\n'
              'pedra - 1\n'
              'papel - 2\n'
              'tesoura - 3')
        self.choice_jkp = int(input('Escolha: '))
        self.verificador(self.choice_jkp)
        
    def verificador(self, opc):
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        if opc == 1:
            if self.sort_pc == 1:
                print('Empate! você escolheu pedra e o computador escolheu pedra')
            elif self.sort_pc == 2:
                print('Você perdeu! você escolheu pedra e o computador escolheu papel')
            elif self.sort_pc == 3:
                print('Você ganhou! Você escolheu pedra e computador escolheu tesoura')
        elif opc == 2:
            if self.sort_pc == 1:
                print('Você ganhou! você escolheu papel e o computador escolheu pedra')
            elif self.sort_pc == 2:
                print('Empate! você escolheu papel e o computador escolheu papel')
            elif self.sort_pc == 3:
                print('Você perdeu! Você escolheu papel e computador escolheu tesoura')
        elif opc == 3:
            if self.sort_pc == 1:
                print('Você perdeu! você escolheu tesoura e o computador escolheu pedra')
            elif self.sort_pc == 2:
                print('Você ganhou! você escolheu tesoura e o computador escolheu papel')
            elif self.sort_pc == 3:
                print('Empate! Você escolheu tesoura e computador escolheu tesoura')
        else:
            print('\033[1:31mIsso não é uma escolha válida\033[m')

class Tabuada:
    def __init__(self):
        #intruções
        print('-=-' * 15)
        print('Tabuada')
        print('-=-' * 15)
        print('')
        print('Instruções: Digite um valor para ver a sua tabuada.\n'
              'Para encerrar o programa insira um valor negativo.')
        print('')
        #loop principal
        while True:
            n = int(input('Digite um número: '))
            print('-' * 30)
            if n < 0:
                break
            for c in range(1, 11):
                print(f'{n} x {c} = {n * c}')
            print('-' * 30)
        print('')
        print('programa encerrado!')

class Calculadora:
    def __init__(self) -> None:
        self.number1 = int(input('Digite um valor: '))
        self.number2 = int(input('Digite outro valor: '))
        self.option = 0
        self.maior = 0
        while True:
            print('-=-' * 15)
            print('[1]somar\n'
                  '[2]multiplicar\n'
                  '[3]maior número\n'
                  '[4]novos números\n'
                  '[5]sair do programa')
            print('-=-' * 15)
            self.option = int(input('\033[33mEscolha uma das opções: \033[m'))
            match self.option:
                case 1:
                    print('')
                    print(f'\033[34mA soma entre {self.number1} e {self.number2} é {self.number1+ self.number2}\033[m')
                case 2:
                    print('')
                    print(f'\033[34mA multiplicação entre {self.number1} e {self.number2} é {self.number1* self.number2}\033[m')
                case 3:
                    if self.number1 > self.maior:
                        self.maior = self.number1
                        if n2 > self.maior:
                            self.maior = n2
                    print('')
                    print(f'\033[34mO maior valor é {self.maior}\033[m')
                case 4:
                    print('')
                    self.number1 = int(input('Digite um valor: '))
                    n2 = int(input('Digite outro valor: '))
                case _:
                    break
        print('Carregando...')
        sleep(1)
        print('')
        print('Programa encerrado!')

     
if __name__ == '__main__':
    App()