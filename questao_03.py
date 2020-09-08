# -*- coding: utf-8 -*-
"""
/***************************************************************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : TP 03 - Lógica, Computação e Algoritmos         *
*        Professor       : Carlos Pivotto                                  *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""

print('===' * 21)
print('{:^63}'.format('Questão 03'))
print('===' * 21)


def vote():
    """
    This function record the candidates and your grades for a
    costume contest.
    """
    contest_dict = {}
    for i in range(5):
        name = input(
            "Informe nome do {}º participante: ".format((i+1)))
        grade = float(input(
            "Informe nota do {}º participante: ".format((i+1))))
        if grade in range(11):
            contest_dict[name] = grade
        else:
            print("Informe um número maior que 0 e menor que 10!")
            grade = float(input(
                "Informe a nota do {}º participante: ".format((i+1))))
            contest_dict[name] = grade
    return contest_dict


def chicken_dinner():
    """
    This function shows the costume contest winner.
    """
    contest = vote()
    winner_grade = max({v: k for k, v in contest.items()})
    winner_name = [k for k, v in contest.items() if winner_grade == v]
    return print('---' * 21,
                 "O(a) vencedor(a) foi {} com nota {}!".format(
                     winner_name[0], winner_grade),
                 '---' * 21, sep="\n")


chicken_dinner()
