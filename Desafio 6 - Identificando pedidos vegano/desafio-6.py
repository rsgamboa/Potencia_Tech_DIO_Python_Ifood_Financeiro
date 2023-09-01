def solicita_dados_pedido():
  """
  Solicita ao usuário os dados de um pedido.

  Returns:
    dict: Um dicionário contendo os dados do pedido.
  """

  nome_do_prato = input("Nome do prato: ")
  calorias = float(input("Calorias: "))
  vegano = input("Vegano (s/n): ")

  if vegano == "s":
    vegano = True
  else:
    vegano = False

  dados_pedido = {
    "nome_do_prato": nome_do_prato,
    "calorias": calorias,
    "vegano": vegano
  }

  return dados_pedido


def imprime_lista_pedidos(lista_pedidos):
  """
  Imprime uma lista de pedidos.

  Args:
    lista_pedidos (list): Uma lista de pedidos.
  """

  for i, pedido in enumerate(lista_pedidos):
    print(f"Pedido {i + 1}: {pedido['nome_do_prato']} ({'Vegano' if pedido['vegano'] else 'Nao-vegano'}) - {pedido['calorias']} calorias")


if __name__ == "__main__":
  # Solicita ao usuário o número de pedidos
  n = int(input("Quantos pedidos você deseja fazer? "))

  # Cria uma lista vazia para armazenar os pedidos
  lista_pedidos = []

  # Solicita os dados de cada pedido
  for _ in range(n):
    dados_pedido = solicita_dados_pedido()
    lista_pedidos.append(dados_pedido)

  # Imprime a lista de pedidos
  imprime_lista_pedidos(lista_pedidos)
