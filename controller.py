import model
import view


# Функция чтения справочника из файла
def open_reference( file_name: str = "test.txt" ) -> list:
    reference, status = model.read_reference_from_file( file_name )
    if status:
        view.display_message( "Чтение справочника из файла {} выполнено успешно".format( file_name ) )
    else:
        view.display_error( "Ошибка чтения справочника из файла: {}".format( file_name ) )
    return reference


# Функция записи справочника в файл
def save_reference( file_name: str = "test.txt", reference: list = model.reference ) -> None:
    status = model.write_reference_from_file( file_name, reference )
    if status:
        view.display_message( "Контакты, записанны в файл {} успешно".format( file_name ) )
    else:
        view.display_error( "Ошибка записи контактов на файл: {}".format( file_name ) )


# Функция просмотра всех контактов
def show_contacts( count: int = 0 ) -> list:
    reference, status = model.get_reference(count)
    if not status:
        view.display_error("Внимание: Количество записей в справочнике меньше запрошенного")
    return reference


# Функция добавления нового контакта
def add_contact(record: dict) -> list:
    reference, status = model.add_reference(record)
    if status:
        view.display_message("Контакт успешно создан")
    else:
        view.display_error("Создать контакт не удалось: {}".format(reference))
    return reference


# Функция обновления контакта
def update_contact( id: int, record: dict ) -> list:
    reference, status = model.update_reference(id, record)
    if status:
        view.display_message("Контак с id {} успешно обновлен".format(id + 1))
#   else:
#       view.display_error("Ошибка обновления контакта с id {}: элемент не найден".format(id))
    return reference


# Функция удаления контакта
def delete_contact(id: int) -> list:
    reference, status = model.delete_reference(id)
    if status:
        view.display_message("Контак с id {} успешно удаление".format(id + 1))
#   else:
#       view.display_error("Ошибка удаления контакта с id {}: элемент не найден".format(id))
    return reference


# Функция нахождения в справочнике контакта с указанными параметрами
def find_contact(parameters: dict = {}) -> list:
    reference, status = model.find_records(parameters)
    if status:
        view.display_message("Запись найдена успешно")
    else:
        view.display_error("Ошибка поиска записи с параметрами {}: запись не найдена".format(parameters))
    return reference


# Функция нахождения в справочнике контакта по id
def find_contact_by_id(id: int) -> (id, dict):
    record, status = model.find_record_from_id(id)
    if status:
        view.display_message("Запись с id {} успешно найдена".format(id + 1))
    else:
        view.display_error("Ошибка поиска записи по id {}: запись не найдена".format(id + 1))
    return id, record


def input_handler(inp: int):
    # 3.8 нет поддержки match / case
    if inp == 1:  # +
        open_reference( 'test.txt' )
        # Имя файла для открытия от пользователя

    elif inp == 2:  # сохранить контакт +
        save_reference( 'test.txt', model.reference )
        # Имя файла для сохранения от пользователя

    elif inp == 3:  # Вывести список контактов +
        view.show_all( show_contacts(  ) )
        # Запрос, сколько шт. вывести на экран
        # 2.0 срез списка контактов с x1 по x2

    elif inp == 4:  # Добавить контакт +
        view.show_all(
            add_contact( view.create_contact() ) )

    elif inp == 5:  # Обновить контакт
        id, rec = view.change_contact( len(model.reference) )
        view.show_all( update_contact( id, rec ) )

    elif inp == 6:  # Удилить контакт +
        delete_contact(view.delete_contact(len(model.reference)))

    elif inp == 7:
        id, rec = find_contact_by_id(view.get_id(len(model.reference)) - 1)
        view.show_contact( id, rec )

    elif inp == 8:
        find_contact({})

    elif inp == 0:  # выход
        if view.exit_program():
            exit()


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
