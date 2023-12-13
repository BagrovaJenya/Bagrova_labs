list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_of_list = len(list_players) // 2

first_team = list_players[:middle_of_list]
second_team = list_players[middle_of_list:]

print(first_team)
print(second_team)
