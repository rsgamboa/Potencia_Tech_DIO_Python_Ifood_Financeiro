def calcula_desconto(valor, tipo_desconto):
  """
  Calcula o desconto de um pedido.

  Args:
    valor (float): O valor do pedido.
    tipo_desconto (str): O tipo de desconto (10% ou 20%).

  Returns:
    float: O valor do desconto.
  """

  if tipo_desconto == "10%":
    return valor * 0.1
  elif tipo_desconto == "20%":
    return valor * 0.2
  else:
    raise ValueError(f"Tipo de desconto inválido: {tipo_desconto}")


def calcula_valor_total(pedidos, tipo_desconto):
  """
  Calcula o valor total de todos os pedidos com o desconto aplicado.

  Args:
    pedidos (list): Uma lista de pedidos.
    tipo_desconto (str): O tipo de desconto (10% ou 20%).

  Returns:
    float: O valor total de todos os pedidos com o desconto aplicado.
  """

  valor_total = 0
  for pedido in pedidos:
    item, valor = pedido
    valor_total += valor

  desconto = calcula_desconto(valor_total, tipo_desconto)
  valor_total -= desconto

  return valor_total


def main():
  """
  Programa principal.

  Args:
    None

  Returns:
    None
  """

  # Leitura da entrada
  n = int(input())
  pedidos = []
  for _ in range(n):
    item, valor = input().split()
    pedidos.append((item, float(valor)))

  # Tratamento de erros
  try:
    tipo_desconto = input()
  except ValueError:
    print("O tipo de desconto deve ser 10% ou 20%.")
    sys.exit(1)

  # Cálculo do valor total
  valor_total = calcula_valor_total(pedidos, tipo_desconto)

  # Formatação da saída
  print(f"Valor total: R$ {valor_total:.2f}")


if __name__ == "__main__":
  main()
