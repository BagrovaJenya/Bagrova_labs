salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


money_capital = 0

while months > 0:
    months -= 1
    money_capital += salary - spend
    spend *= (1 + increase)

money_capital = -1 * round(money_capital, 2)

months = 10

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

