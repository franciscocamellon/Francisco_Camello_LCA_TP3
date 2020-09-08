# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 01                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : TP 03 - Lógica, Computação e Algoritmos         *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_01.py                                   *
***************************************************************************/
"""

import locale

print('===' * 21)
print('{:^63}'.format('Questão 01'))
print('===' * 21)


# -*- coding: utf-8 -*-


def people_validation():
    people = int(input("Informe o total de pessoas: "))
    while people <= 0:
        print("Digite um número de pessoas maior que zero")
        people = int(input("Informe o total de pessoas: "))
    else:
        return people


def tip_validation():
    tip = int(input("Informe o percentual do serviço, entre 0 e 100: "))
    while tip not in range(101):
        print("Taxa de serviço deve estar entre 0 e 100%")
        tip = int(input("Informe o percentual do serviço, entre 0 e 100: "))
    else:
        return tip


def bill_validation():
    bill = int(input("Informe o valor total do consumo: "))
    while bill <= 0:
        print("Digite um valor total do consumo maior que zero")
        bill = int(input("Informe o valor total do consumo: "))
    else:
        return bill


def bill_divide_by(bill, people, tip):
    total_bill = bill*(1+(tip/100))
    bill_by_people = total_bill/people
    return total_bill, bill_by_people


def print_result(people, bill_divide_by):
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    a = locale.currency(bill_divide_by[1])
    b = locale.currency(bill_divide_by[0])
    print('---' * 21,
          'O valor total da conta, com a taxa de serviço, \n será de {}'.format(b), sep="\n")
    print('Dividindo a conta por {} pessoa(s), cada pessoa deverá \n pagar {}'.format(
        people, a))


bill = bill_validation()
people = people_validation()
tip = tip_validation()
divide = bill_divide_by(bill, people, tip)
print_result(people, divide)
print('---' * 21)
