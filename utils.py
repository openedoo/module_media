from modules.module_eclass.libs.util import unique_code_generator


def random_char(length):
    return unique_code_generator(length).lower()
