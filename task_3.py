from datetime import datetime, timedelta

def future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

# Пример использования
days = 10
result = future_date(days)
print(result)