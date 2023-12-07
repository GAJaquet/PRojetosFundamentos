class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

# Criando instâncias das assinaturas
assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

# Adicionando instâncias no array
assinaturas = [assinatura_simples, assinatura_premium]

# Iterando sobre o array e exibindo informações
for assinatura in assinaturas:
    print(f"Tipo de Assinatura: {assinatura.__class__.__name__}")
    print(f"Preço: R${assinatura.calcular_preco():.2f}")
    assinatura.exibir_detalhes()
    print()
