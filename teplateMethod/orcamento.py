# -*- coding: UTF-8 -*-
from typing import Tuple


class Item(object):
    def __init__(self, nome: str, valor: float):
        self.__nome = nome
        self.__valor = valor
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    @property
    def nome(self) -> str:
        return self.__nome


class Orcamento(object):
    def __init__(self):
        self.__itens = []   # type: list
    
    @property
    def valor(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total
    
    def obter_itens(self) -> Tuple[Item, ...]:
        return tuple(self.__itens)
    
    @property
    def total_itens(self) -> int:
        return len(self.__itens)
    
    def adiciona_itens(self, item: Item):
        self.__itens.append(item)
