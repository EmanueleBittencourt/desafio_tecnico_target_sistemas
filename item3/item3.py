# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('item3/dados.json', 'r') as file:
    dados = json.load(file)


dados_dias_validos = [dia for dia in dados if dia["valor"] > 0]

menor_valor = round(min(dia["valor"] for dia in dados_dias_validos), 2)

maior_valor = round(max(dia["valor"] for dia in dados_dias_validos), 2)

media_faturamento = sum(dia["valor"] for dia in dados_dias_validos) / len(dados_dias_validos)

quantidade_dias_acima_media = len([dia for dia in dados_dias_validos if dia["valor"] > media_faturamento])


print(f'Menor valor de faturamento ocorrido em um dia do mês: R$ {menor_valor}')
print(f'Maior valor de faturamento ocorrido em um dia do mês: R$ {maior_valor}')
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {quantidade_dias_acima_media}")
