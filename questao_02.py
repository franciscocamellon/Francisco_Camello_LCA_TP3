# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 02                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : TP 03 - Lógica, Computação e Algoritmos         *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_02.py                                   *
***************************************************************************/
"""

print('===' * 21)
print('{:^63}'.format('Questão 02'))
print('===' * 21)


def vote():
    """
    This function informs if a person is a mandatory voter.
    """
    age = int(input("Informe a idade: "))
    while not(isinstance(age, int) and age > 0):
        print("Por favor digite um número inteiro maior que zero!")
        age = int(input("Informe a idade: "))
    else:
        if age in range(18, 70, 1):
            return print('---' * 21, "Tem obrigação de votar.", sep="\n")
        elif age in range(16, 18, 1) or age >= 70:
            return print('---' * 21, "Não tem obrigação de votar.", sep="\n")
        else:
            return print('---' * 21, "Não tem direito a voto.", sep="\n")


vote()
print('---' * 21)
