import csv


class Imovel:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor = 0

    def calcular_aluguel(self):
        return self.valor


class Apartamento(Imovel):
    def __init__(self, quartos, garagem, possui_criancas):
        super().__init__("Apartamento")
        self.valor = 700

        if quartos == 2:
            self.valor += 200

        if garagem:
            self.valor += 300

        if not possui_criancas:
            desconto = self.valor * 0.05
            self.valor -= desconto


class Casa(Imovel):
    def __init__(self, quartos, garagem):
        super().__init__("Casa")
        self.valor = 900

        if quartos == 2:
            self.valor += 250

        if garagem:
            self.valor += 300


class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__("Estudio")
        self.valor = 1200

        if vagas >= 2:
            self.valor += 250

            if vagas > 2:
                extras = vagas - 2
                self.valor += extras * 60


class Contrato:
    def __init__(self):
        self.valor_contrato = 2000

    def parcelamento(self):
        parcelas = self.valor_contrato / 5
        return parcelas


class Orcamento:
    def __init__(self, imovel):
        self.imovel = imovel
        self.contrato = Contrato()

    def mostrar_orcamento(self):
        print("\n===== ORÇAMENTO =====")
        print(f"Tipo do imóvel: {self.imovel.tipo}")
        print(f"Valor do aluguel mensal: R$ {self.imovel.calcular_aluguel():.2f}")
        print(f"Contrato imobiliário: R$ {self.contrato.valor_contrato:.2f}")
        print(f"Parcelado em 5x de R$ {self.contrato.parcelamento():.2f}")

    def gerar_csv(self):
        valor_mensal = self.imovel.calcular_aluguel()

        with open("parcelas.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow(["Mês", "Valor"])

            for mes in range(1, 13):
                escritor.writerow([f"Mês {mes}", f"R$ {valor_mensal:.2f}"])

        print("\nArquivo parcelas.csv gerado com sucesso!")


print("===== IMOBILIÁRIA R.M =====")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Estudio")

opcao = int(input("Escolha o tipo de imóvel: "))

if opcao == 1:
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = input("Possui garagem? (s/n): ").lower() == 's'
    criancas = input("Possui crianças? (s/n): ").lower() == 's'

    imovel = Apartamento(quartos, garagem, criancas)

elif opcao == 2:
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = input("Possui garagem? (s/n): ").lower() == 's'

    imovel = Casa(quartos, garagem)

elif opcao == 3:
    vagas = int(input("Quantidade de vagas: "))

    imovel = Estudio(vagas)

else:
    print("Opção inválida")
    exit()

orcamento = Orcamento(imovel)
orcamento.mostrar_orcamento()
orcamento.gerar_csv()
