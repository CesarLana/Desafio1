import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)