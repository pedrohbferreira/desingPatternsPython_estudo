from impostos import ISS, ICMS, IKCV, ICPP


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == "__main__":
    from orcamento import Orcamento, Item

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('Item 1', 50))
    orcamento.adiciona_itens(Item('Item 1', 200))
    orcamento.adiciona_itens(Item('Item 1', 250))

    print("ICMS e ISS")
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, ISS())

    print("ICPP e IKCV")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
