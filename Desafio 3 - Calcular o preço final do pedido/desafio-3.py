def calcula_preco_final(valor_hamburguer, quantidade_hamburguer, valor_bebida, quantidade_bebida):
  """
  Calcula o preço final de um pedido de hambúrguer e bebida.

  Args:
    valor_hamburguer (float): O valor de um hambúrguer.
    quantidade_hamburguer (int): A quantidade de hambúrgueres.
    valor_bebida (float): O valor de uma bebida.
    quantidade_bebida (int): A quantidade de bebidas.

  Returns:
    float: O preço final do pedido.
  """

  preco_hamburguer = valor_hamburguer * quantidade_hamburguer
  preco_bebida = valor_bebida * quantidade_bebida
  return preco_hamburguer + preco_bebida


def calcula_troco(valor_pago, preco_final):
  """
  Calcula o troco de um pedido.

  Args:
    valor_pago (float): O valor pago pelo usuário.
    preco_final (float): O preço final do pedido.

  Returns:
    float: O troco do pedido.
  """

  return valor_pago - preco_final


def main():
  """
  Programa principal para calcular o preço final e o troco de um pedido de hambúrguer e bebida.

  Args:
    None

  Returns:
    None
  """

  valor_hamburguer = float(input("Informe o valor do hambúrguer: "))
  quantidade_hamburguer = int(input("Informe a quantidade de hambúrgueres: "))
  valor_bebida = float(input("Informe o valor da bebida: "))
  quantidade_bebida = int(input("Informe a quantidade de bebidas: "))
  valor_pago = float(input("Informe o valor pago: "))

  preco_final = calcula_preco_final(valor_hamburguer, quantidade_hamburguer, valor_bebida, quantidade_bebida)
  troco = calcula_troco(valor_pago, preco_final)

  print(f"O preço final do pedido é R$ {preco_final:.2f}.")
  print(f"Seu troco é de R$ {troco:.2f}.")


if __name__ == "__main__":
  main()
