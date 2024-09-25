from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-09-10 20:30"
mascara_br = '%d/%m/%Y'
print(data_hora_atual.strftime(mascara_br))