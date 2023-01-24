def main_menu() -> int:  # +
    print('Главное меню.')
    menu_list = ['Открыть справочник',
                 'Сохранить справочник',
                 'Показать все контакты',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт по id',
                 'Поиск контакта по id',
                 'Поиск контакта по параметрам',
                 'Выход']

    for i in range( len(menu_list) - 1  ):
        print( f'\t{i + 1}. {menu_list[i]}' )
    print( f'\t{0}. {menu_list[-1]}' )

    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию

    return user_input


def show_all(db: list):  # +
    for i in range(len(db)):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in db[i].values():
            print(f'{v}', end=' ')
        print()


def show_contact(id, rec):
    print(f'\t{id + 1}', end='. ')
    for v in rec.values():
        print(f'{v}', end=' ')
    print()


def exit_program():  # +
    print('Завершение программы.')
    n = int(input('Вы уверены что хотите выйти?\n1. Да\n2. Нет \n'))
    if n == 1:
        return 1
    else:
        print('Попробуйте вызвать "Завершение программы" еще раз...')


def create_contact():  # +
    print('Создание нового контакта.')
    new_contact = dict()
    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact


def change_contact( count: int ) -> (int, dict): # Изменение контакта
    id = get_id( count )
    if id != -1:
        if input(f'Вы уверены что хотите изменить контакт № {id}?\n1 - Да\n2 - Нет\n') == '1':

            print('Изменение контакта.')
            contact = {}
            keys = ['lastname', 'firstname', 'phone', 'comment']

            for key in keys:
                if key == 'lastname':
                    if input(f'Изменить поле "Фамилия"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['lastname'] = input('\tВведите фамилию >: ')
                if key == 'firstname':
                    if input(f'Изменить поле "Имя"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['firstname'] = input('\tВведите имя >: ')
                if key == 'phone':
                    if input(f'Изменить поле "Телефон"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['phone'] = input('\tВведите телефон >: ')
                if key == 'comment':
                    if input(f'Изменить поле "Комментарий"?{id}?\n1 - Да\n2 - Нет\n') == '1':
                        contact['comment'] = input('\tВведите комментарий >: ')
            return id - 1, contact
    else:
        print('\nДействие отменено')
        return -1, {}


def delete_contact(count: int) -> int:  # +
    id = get_id(count)
    if id != -1:
        if input(f'Уверены что хотите удалить контакт № {id}?\n1 - Да\n2 - Нет\n') == '1':
            return id - 1
    print('\nДействие отменено')
    return -1


def get_id(count):  # +
    ans = int(input('Введите номер записи (id) в справочнике:\n'))
    if 0 < int(ans) <= count:
        return ans
    print('\nТакого контакта не существует\n')
    return -1

def display_message( message: str ):
    print("[+]", message)

def display_error( message: str ):
    print("[!]", message)