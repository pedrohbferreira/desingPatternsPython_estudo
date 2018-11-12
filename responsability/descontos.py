# -*- coding: UTF-8 -*-
class SemDesconto(object):
    def calcula(self, orcamento) -> float:
        return 0


class DescontoPorCincoItems(object):

    def __init__(self, proximo_desconto=SemDesconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento) -> float:
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoAcima500Reais(object):

    def __init__(self, proximo_desconto=SemDesconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento) -> float:
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)
