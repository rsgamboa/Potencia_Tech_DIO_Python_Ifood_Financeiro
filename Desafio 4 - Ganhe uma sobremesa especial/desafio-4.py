def verifica_brinde(valor_pedido):
  """
  Verifica se o usuário ganhou um brinde especial.

  Args:
    valor_pedido (int): O valor total do pedido.

  Returns:
    str: Uma mensagem informando se o usuário ganhou um brinde ou não.
  """

  # Verificamos se o valor do pedido é maior ou igual a R$ 50,00.

  if valor_pedido >= 50:
    mensagem = f"Parabéns! Você ganhou uma sobremesa grátis!"
  else:
    mensagem = "Que pena, você não ganhou nenhum brinde especial."

  return mensagem


if __name__ == "__main__":
  # Entrada
  valor_pedido = int(input("Informe o valor total do pedido: "))

  # Saída
  mensagem = verifica_brinde(valor_pedido)
  print(mensagem)
