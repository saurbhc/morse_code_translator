from constants import text_to_morse_code_mapping, morse_code_to_text_mapping


def _ask_for_option():
    help_text = """Choose One:

        1: TextCharacter to MorseCode
        2: MorseCode to TextCharacter
        """
    print(help_text)
    option = int(input(">"))

    if option == 1:
        _input = _ask_for_text_characters_input(return_list=True)
        print("!your input is: ", _input)
        mc_obj = MorseCode(_text_character=_input)
        mc_obj.to_morse_code()
        print("!list: ", mc_obj.morse_code)
        print("!comma-separated-text: ", ",".join(mc_obj.morse_code))
        want_more()
    elif option == 2:
        _input = _ask_for_morse_code_input(return_list=True)
        print("!your input is: ", _input)
        mc_obj = MorseCode(_morse_code=_input)
        mc_obj.to_text_characters()
        print("!list: ", mc_obj.text_characters)
        print("!comma-separated-text: ", ",".join(mc_obj.text_characters))
        print("!text: ", "".join(mc_obj.text_characters))
        want_more()
    else:
        print("~~ WRONG, TRY AGAIN ~~")
        _ask_for_option()


def _ask_for_text_characters_input(return_list=False):
    text = input(
        "Enter (A,...,Z) & (a,...,z) (1,...,9) (' ' <- this is space): "
    )
    if not return_list:
        return text

    _temp_text = []
    for in_text in text:
        _temp_text += list(in_text)
    text = _temp_text

    # split by space
    return text


def _ask_for_morse_code_input(return_list=False):
    morse_codes = input(
        "Enter (. <- this is dot) (- <- this is hyphen) (' ' <- this is space) (',' <- separator b/w two words): "
    )

    if not return_list:
        return morse_codes

    morse_codes = morse_codes.split(",")

    # split by space
    return morse_codes


def want_more():
    option_want_more = input("!Do you want more? (y/n)")

    if option_want_more.lower() == "y":
        _ask_for_option()

    return


class MorseCode:
    def __init__(self, _morse_code=None, _text_character=None):
        self.morse_code = _morse_code
        self.text_characters = _text_character

    def to_text_characters(self):
        _converted_to_text_characters = []
        for _morse_code in self.morse_code:
            _converted_to_text_characters.append(
                morse_code_to_text_mapping.get(_morse_code, _morse_code)
            )
        self.text_characters = _converted_to_text_characters

    def to_morse_code(self):
        _converted_to_morse_code = []
        for _text_character in self.text_characters:
            _converted_to_morse_code.append(
                text_to_morse_code_mapping.get(_text_character, _text_character)
            )
        self.morse_code = _converted_to_morse_code


if __name__ == "__main__":
    _ask_for_option()
