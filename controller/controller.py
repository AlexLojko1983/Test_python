import text
import view
import model


def start():
    na = model.NotesApp()
    while True:
        select = view.menu()
        match select:
            case 1:
                if na.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if na.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(na.get(), text.empty_book)
            case 4:
                new = view.add_contact()
                na.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.view_input(text.search_word)
                result = na.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                index = view.view_input(text.index_update)
                book = view.add_contact()
                na.update_contact(book, index)
            case 7:
                word = view.view_input(text.search_word)
                result = na.search(word)
                view.show_contacts(result, text.empty_search(word))

                name = na.remove(index)
                view.print_message(text.remove_contact(name))

            case 8:
                if na.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        na.save_file()
                view.print_message(text.goodbay)
                break
