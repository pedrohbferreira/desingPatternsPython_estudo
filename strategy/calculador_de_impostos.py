from impostos import calcula_ICMS, calcula_ISS

class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, strategy):
        importo_calculado = strategy(orcamento)
        print(importo_calculado)

if __name__ == "__main__":
    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, calcula_ICMS)
    calculador.realiza_calculo(orcamento, calcula_ISS)
