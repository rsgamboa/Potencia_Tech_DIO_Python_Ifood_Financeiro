def exibe_tempo_estimado_entrega(nome_restaurante, tempo_estimado_entrega):
  """
  Exibe o tempo estimado de entrega de um restaurante.

  Args:
    nome_restaurante (str): O nome do restaurante desejado.
    tempo_estimado_entrega (str): O tempo estimado de entrega em minutos.

  Returns:
    str: Uma mensagem informando o tempo estimado de entrega do restaurante.
  """

  # Verificamos se o tempo estimado de entrega é negativo.

  if tempo_estimado_entrega < 0:
    return "O tempo estimado de entrega não é válido."

  # Tentamos converter o tempo estimado de entrega em um número.

  try:
    tempo_estimado_entrega = int(tempo_estimado_entrega)
  except ValueError:
    return "O tempo estimado de entrega deve ser um número."

  # Utilizamos interpolação de strings para formatar a saída.

  mensagem = f"O restaurante {nome_restaurante} entrega em {tempo_estimado_entrega} minutos."

  return mensagem

if __name__ == "__main__":
  # Exemplos de entrada e saída.

  entrada_1 = ("McDonalds", 10)
  saida_1 = "O restaurante McDonalds entrega em 10 minutos."

  entrada_2 = ("KFC", 25)
  saida_2 = "O restaurante KFC entrega em 25 minutos."

  entrada_3 = ("Burger King", 5)
  saida_3 = "O restaurante Burguer King entrega em 5 minutos."

  entrada_4 = ("Bar do Zinho", "dez")
  saida_4 = "O tempo estimado de entrega deve ser um número."

  # Testamos o programa com os exemplos.

  assert exibe_tempo_estimado_entrega(*entrada_1) == saida_1
  assert exibe_tempo_estimado_entrega(*entrada_2) == saida_2
  assert exibe_tempo_estimado_entrega(*entrada_3) == saida_3
  assert exibe_tempo_estimado_entrega(*entrada_4) == saida_4

  # Solicitamos ao usuário a entrada dos dados.

  nome_restaurante = input("Informe o nome do restaurante: ")
  tempo_estimado_entrega = input("Informe o tempo estimado de entrega em minutos: ")

  # Exibimos o tempo estimado de entrega.

  print(exibe_tempo_estimado_entrega(nome_restaurante, tempo_estimado_entrega))
