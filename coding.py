def boas_vindas(nome):
    return f"Olá, {nome}! Seu ambiente de desenvolvimento está pronto"

def calcular_requisicoes(sucesso, falhas):
    total = sucesso + falhas
    taxa_sucesso = (sucesso / total) * 100
    return total, taxa_sucesso

if __name__ == "__main__":
    usuario = "Edoardo"
    print(boas_vindas(usuario))

    total_reqs, taxa = calcular_requisicoes(95, 5)
    print(f"Total de requisições: {total_reqs}")
    print(f"Taxa de sucesso: {taxa:.1f}%")
