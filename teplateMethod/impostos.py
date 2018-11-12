# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


class TemplateImposto(object):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_taxa_maxima(orcamento):
            return self.taxa_maxima(orcamento)
        else:
            return self.taxa_minima(orcamento)

    @abstractmethod
    def deve_usar_taxa_maxima(self, orcamento):
        pass

    @abstractmethod
    def taxa_maxima(self, orcamento):
        pass

    @abstractmethod
    def taxa_minima(self, orcamento):
        pass


class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(TemplateImposto):
    def deve_usar_taxa_maxima(self, orcamento):
        return orcamento.valor > 500

    def taxa_maxima(self, orcamento):
        return orcamento.valor * 0.07

    def taxa_minima(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateImposto):
    def __tem_item_mais_de_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_taxa_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_mais_de_100(orcamento)

    def taxa_maxima(self, orcamento):
        return orcamento.valor * 0.1

    def taxa_minima(self, orcamento):
        return orcamento.valor * 0.06
