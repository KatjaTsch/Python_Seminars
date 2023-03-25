while True:    
    choise = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Вывести всех \n 3 - Поиск  \n 4 - Выход \n'))
    match choise:
        case 1:
            import Task_0050file
            Task_0050file.Input(input ('Введите имя: '), input('Введите номер: ')) 
        case 2:
            from Task_0050Output import OutputAll
            OutputAll()
        case 3:
            from Task_0050Search import Search
            Search(input('Введите фамилию: '))
        case 4: break