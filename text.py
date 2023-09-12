menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать все заметки',
        'Добавить заметку',
        'Найти заметку',
        'Изменить заметку',
        'Удалить заметку',
        'Выход'
        ]

invalid_selection = f'Ошибка ввода. Введите число от 1 до {len(menu) - 1}: '

select_menu = 'Выберите пункт меню: '

load_successful = 'Loading'
error_load = 'not loading'

save_successful = 'Saving'
error_save = 'not saving'

empty_node = 'Empty Nodes'

def add_successful(title: str) -> str:
    return f'Заметка {title} успешно добавлена!'


new_node = {
    'title': 'Введите заголовок: ',
    'body': 'Введите тело заметки: '
}