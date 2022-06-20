# dsl.py

import sys
import lexer
import keyboard
import lang
from time import sleep

FLECHA_ARRIBA = 'flecha arriba'
FLECHA_ABAJO = 'flecha abajo'
ENTER = 'enter'
ESPACIO = 'space'
DELETE = 'backspace'
SHIFT = 'right shift'
TAB = 'tab'

FLECHA_ARRIBA_L = 'up'
FLECHA_ABAJO_L = 'down'
ENTER_L = 'enter'
ESPACIO_L = 'space'
DELETE_L = 'backspace'
TAB_L = 'tab'

"""
This module is used to connect the whole application and made the calls to all the different parts that run in the project.
It will control the input of the user and show whatever is necessary, then it will call the lexer to check the grammar.
"""


def welcome_message():
    """ This method is used to inform that the application is running by printing the welcome message

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    print("\t" + lang.get_mensajes("WELCOME_MESSAGE"))


def start_writing_message():
    """This method is used to inform that the command line is active to receive code by printing the start message

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    print("\t" + lang.get_mensajes("START_MESSAGE"))


def delete_keys_character_up():
    """This method is used to correct the buffer output when the up arrow is pressed so it does not print its code on the console

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    sleep(0.035)
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sleep(0.035)


def delete_keys_character_down():
    """This method is used to correct the buffer output when the down arrow is pressed so it does not print its code on the console

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    sleep(0.035)
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    sys.stdout.write('\b')
    sleep(0.035)


def delete_keys_character_tab():
    """This method is used to correct the buffer output when the tab key is pressed so it does not print its code on the console

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    sleep(0.035)
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sys.stdout.write('\b')
    sleep(0.035)


def delete_line(length):
    """This method is used to correct the buffer output when the line needs to be deleted

    Parameters:
    length (int): Length of the line that needs to be deleted

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    sys.stdout.write('\b')
    sys.stdout.write(' ')
    for i in range(0, length):
        sys.stdout.write('\b')
        sys.stdout.write('\b')
        sys.stdout.write(' ')
    sys.stdout.flush()


def get_input():
    """This method is created as our own version of the native method input(), the main difference with the mentioned method is that
    this method does not stop the execution of the machine. We need this in order to access the history of the machine if the user
    press the arrow keys or to predict the written word if the user press the TAB key.

    Parameters:
    none

    Returns:
    String:Returning string

    @author: Álvaro García Infante
   """
    count = 0
    word_selected = ""
    word_written = ""

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if lang.os == 'Windows':
                if key == ENTER:
                    break
                elif key == FLECHA_ARRIBA:
                    count = count + 1
                elif key == FLECHA_ABAJO:
                    count = count - 1
                elif key == ESPACIO:
                    word_written = word_written + " "
                elif key == DELETE:
                    word_written = word_written[:-1]
                else:
                    if len(key) == 1:
                        word_written = word_written + key
            else:
                if key == ENTER_L:
                    break
                elif key == FLECHA_ARRIBA_L:
                    count = count + 1
                elif key == FLECHA_ABAJO_L:
                    count = count - 1
                elif key == ESPACIO_L:
                    word_written = word_written + " "
                elif key == DELETE_L:
                    word_written = word_written[:-1]
                else:
                    if len(key) == 1:
                        word_written = word_written + key

            if count > len(lexer.history):
                count = len(lexer.history)
            elif count < 0:
                count = 0
            elif count == 0:
                word_selected = word_written
            else:
                if key == FLECHA_ARRIBA or key == FLECHA_ARRIBA_L or key == FLECHA_ABAJO or key == FLECHA_ABAJO_L:
                    word_selected = lexer.history[len(lexer.history) - count]
                    delete_line(len(word_written) - 4)
                    word_written = word_selected
                else:
                    word_selected = word_written

            if key == FLECHA_ARRIBA or key == FLECHA_ARRIBA_L:
                sys.stdout.flush()
                delete_keys_character_up()
                sys.stdout.flush()
            if key == FLECHA_ABAJO or key == FLECHA_ABAJO_L:
                sys.stdout.flush()
                delete_keys_character_down()
                sys.stdout.flush()

            if key == TAB or key == TAB_L:
                word_selected = lexer.predict(word_written)
                aux = word_written.split()
                if len(aux) > 1:
                    word_selected = aux[0] + ' ' + word_selected
                sys.stdout.flush()
                delete_keys_character_tab()
                delete_line(len(word_written) - 4)
                word_written = word_selected
                sys.stdout.flush()

            sys.stdout.write('\r')
            sys.stdout.write(word_selected)

            if key == FLECHA_ARRIBA or key == FLECHA_ARRIBA_L or key == FLECHA_ABAJO or key == FLECHA_ABAJO_L:
                sys.stdout.write(' ')
            if (key != DELETE_L or key != DELETE) and (key != TAB or key != TAB_L):
                if lang.os != 'Windows':
                    sys.stdout.write('\b')
            elif key == TAB or key == TAB_L:
                sys.stdout.flush()
            else:
                if lang.os == 'Windows':
                    sys.stdout.write(' ')
                    sys.stdout.write('\b')
                else:
                    sys.stdout.write('  ')
                    sys.stdout.write('\b')

            sys.stdout.flush()
            sleep(0.01)

    if word_written != word_selected and word_selected != "":
        return word_selected
    else:
        return word_written


def read_input():
    """This method is used to read the console input by lines

    Parameters:
    none

    Returns:
    String:Returning the output

    @author: Álvaro García Infante
   """
    output = []
    count = 0
    while True:
        aux = get_input()
        if aux:
            output.append(aux)
        else:
            break
        count = count + 1
    return output


def main_loop():
    """This is the main method. It will read the input of the console and then check the grammar with the lexer before calling the interpreter

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    start_writing_message()
    lines = read_input()
    read_text = '\n'.join(lines)
    lexer.check_grammar(read_text)



welcome_message()

while True:
    try:
        main_loop()
    except AssertionError as error:
        print(error)

    print(lang.get_mensajes("EXIT_MESSAGE"))
    x = ''
    while x == '':
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            x = event.name
            if x == 'x':
                break
    if x == 'x':
        break

