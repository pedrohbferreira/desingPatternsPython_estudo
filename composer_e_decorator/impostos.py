# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


def IPDC(metodo_ou_funcao):
    """
    Cria um decorator, podendo chamar acima dos métodos criados
    :param metodo_ou_funcao: pega qualquer método ou função e seus parametros
    """
    def wrapper(self, parametro_funcao):
        return metodo_ou_funcao(self, parametro_funcao) + 50
    return wrapper


class Imposto(object):
    """
    Classe genérica de imposto \n\r
    Aceita a composição de impostos e obriga implementação de calcula()
    """

    def __init__(self, imposto_composto=None):
        """
        Na implementação da classe, pode passar um outro imposto para calculo composto
        :param imposto_composto: Imposto
        """
        self.imposto_composto = imposto_composto

    def calculo_imposto_composto(self, orcamento):
        """
        Sempre será chamado \n\r
        Caso não tenha um Imposto para calcular retorna 0
        :param orcamento: Orçamento a ser calculado
        """
        if self.imposto_composto is None:
            return 0
        return self.imposto_composto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass


class TemplateImposto(Imposto):
    """
    Classe abstrata que serve como template de calculo do imposto \n\r
    Verifica uma condição e aplica as taxa máxima ou mínima
    """
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        """
        Implementa o cálculo da taxa do imposto \n\r
        Verifica a condição da taxa, e aplica uma mínima ou máxima \n\r
        A cláusula if executa o método de verificação de taxa máxima(regra implementada por quem herda),
        caso True, executa o método com cálculo pra tal (regra implementado por quem herda), ou aplica taxa mínima
        :param orcamento: Orcamento
        :return: float
        """
        if self.deve_usar_taxa_maxima(orcamento):
            taxa = self.taxa_maxima(orcamento)
        else:
            taxa = self.taxa_minima(orcamento)
        return taxa + self.calculo_imposto_composto(orcamento)

    @abstractmethod
    def deve_usar_taxa_maxima(self, orcamento):
        """
        Implementa e executa uma condição booleana \n\r
        :param orcamento: Orcamento
        :return: valor booleano True / False
        """
        pass

    @abstractmethod
    def taxa_maxima(self, orcamento):
        """
        Implementação do cálculo para a taxa máxima
        :param orcamento: Orcamento
        :return: float
        """
        pass

    @abstractmethod
    def taxa_minima(self, orcamento):
        """
        Implementação do cálculo para a taxa mínima
        :param orcamento: Orcamento
        :return: float
        """
        pass


class ISS(Imposto):
    def calcula(self, orcamento):
        return (orcamento.valor * 0.1) + self.calculo_imposto_composto(orcamento)


class ICMS(Imposto):
    def calcula(self, orcamento):
        return (orcamento.valor * 0.06) + self.calculo_imposto_composto(orcamento)


class ICPP(TemplateImposto):
    """
    Herda de TemplateImposto os templates de métodos de aplicação de imposto \n\r
    Implementa os métodos abstratos
    """

    def deve_usar_taxa_maxima(self, orcamento):
        """
        Implementa validação para taxa máxima \n\r
        Devera aplicar taxa caso valor do orçamento seja maior que 500 \n\r
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor > 500

    def taxa_maxima(self, orcamento):
        """
        Taxa máxima será de 7%
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor * 0.07

    def taxa_minima(self, orcamento):
        """
        Taxa mínima será de 5%
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor * 0.05


class IKCV(TemplateImposto):
    """
    Herda de TemplateImposto os templates de métodos de aplicação de impostos \n\r
    Implementa os métodos abstratos
    """

    @staticmethod
    def __tem_item_mais_de_100(orcamento):
        """
        Varre a lista de itens do orçamento procurando item com valor maior que R$ 100
        :param orcamento: Orcamento
        :return: booleano
        """
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_taxa_maxima(self, orcamento):
        """
        Implementa validação para taxa máxima \n\r
        Devera aplicar taxa caso valor do orçamento seja maior que 500 e tenha item maior que 100 reais \n\r
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor > 500 and self.__tem_item_mais_de_100(orcamento)

    def taxa_maxima(self, orcamento):
        """
        Taxa máxima será de 10%
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor * 0.1

    def taxa_minima(self, orcamento):
        """
        Taxa mínima será de 6%
        :param orcamento: Orcamento
        :return: float
        """
        return orcamento.valor * 0.06
