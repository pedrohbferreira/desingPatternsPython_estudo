# -*- coding: UTF-8 -*-
from orcamento import Orcamento
from descontos import DescontoPorCincoItems, DescontoAcima500Reais


class CalculadorDdeDescontos(object):
    def calcula(self, orcamento: Orcamento):
        desconto = DescontoPorCincoItems(
            DescontoAcima500Reais()
        ).calcula(orcamento)

        return desconto


if __name__ == '__main__':

    from orcamento import Item

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('Item 1', 100))
    orcamento.adiciona_itens(Item('Item 1', 50))
    orcamento.adiciona_itens(Item('Item 1', 400))

    print(orcamento.valor)

    calculador = CalculadorDdeDescontos()
    desconto_calculado = calculador.calcula(orcamento)

    print("%.2f" % desconto_calculado)
