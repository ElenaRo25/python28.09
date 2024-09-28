from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print('День недели:', now.strftime('%A'))
print('Номер недели в году:', now.strftime('%U'))