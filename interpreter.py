# interpreter.py
import os

import dsl
import json_manager
import subprocess
import lang
from deep_translator import GoogleTranslator
from time import sleep

translator = GoogleTranslator(source='es', target='en')
password = ""

"""
This module is used to make use of the corrected grammar by the lexer and to execute the orders.
"""


def check_name_is_unique(name):
    """This method will check the uniqueness of the name inside the section Others of the JSON file

    Parameters:
    name (String): Name to be checked

    Returns:
    boolean: Returning whether the name is true or false

    @author: Álvaro García Infante
   """
    list = json_manager.get_modules("Others")
    ret = True
    for aux in list:
        if aux['nombre'].lower() == name.lower():
            ret = False
    return ret


def create_new_command(name):
    """This method will be used to create a new command in the JSON file

    Parameters:
    name (String): Name of the command

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    assert check_name_is_unique(
        name), lang.get_mensajes("CHECK_NAME_IS_UNIQUE") + name
    sistema = lang.os
    print("\n")
    print(lang.get_mensajes("INTRODUCE_DESC"))
    desc = dsl.get_input()

    print("\n"+lang.get_mensajes("INTRODUCE_ORDERS") + sistema + lang.get_mensajes("PARAM_ADVISE"))
    comando = dsl.get_input()
    json_manager.write_new_command(name, desc, comando)


def help_message():
    """This method will print the general help for the application when the command help is used

    Parameters:
    none

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    print("\n")
    print(lang.get_mensajes("HELP_1"))
    print(lang.get_mensajes("HELP_2"))
    print(
        lang.get_mensajes("HELP_3"))
    print(
        lang.get_mensajes("HELP_4"))
    print(
        lang.get_mensajes("HELP_5"))
    print(
        lang.get_mensajes("HELP_6"))
    print(lang.get_mensajes("HELP_7"))
    print(lang.get_mensajes("HELP_8"))


def run_combination(modules, level):
    """This method will run combinations of packages. It is called when run level1 or run level2 is called

    Parameters:
    modules (dict): Dictionary that contains the all the modules of the system
    level (String): It indicates which level will be executed

    Returns:
    int:Returning value

    @author: Álvaro García Infante
   """
    print("\n")
    for module in modules:
        if "remediate" in module['nombre'].lower():
            command_to_use = module['comando'].replace("!", "\!")
            if module['comando'].count("sudo") == 1:
                print(lang.get_mensajes("YOU_NEED_ROOT"))
            if module['comando'].count("APACHE") > 0:
                command_to_use = command_to_use.replace("APACHE", json_manager.conf("APACHE"))
            if module['comando'].count("PASSWORD") > 0:
                command_to_use = command_to_use.replace("PASSWORD", json_manager.conf("PASSWORD"))
            print(lang.get_mensajes("EXECUTED_ORDER_IS") + command_to_use)
            os.system(command_to_use)


def import_module(args):
    """This method will import commands of a file into another file

    Parameters:
    args (String array): The command import divided into an array in order to process the text

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    nameoffile = args[2]
    if ".json" not in nameoffile:
        nameoffile = nameoffile + ".json"

    commands_list = []
    for x in range(3, len(args)):
        commands_list.append(args[x])

    try:
        json_manager.import_into(commands_list, nameoffile)
    except FileNotFoundError as error:
        print("\n")
        print(lang.get_mensajes("THERE_IS_NOT_FILE") + nameoffile)


def export_module(args):
    """This method will export commands of a file into another file

    Parameters:
    args (String array): The command import divided into an array in order to process the text

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    nameoffile = args[-1]
    if ".json" not in nameoffile:
        nameoffile = nameoffile + ".json"

    commands_list = []
    for x in range(1, len(args) - 2):
        commands_list.append(args[x])

    try:
        json_manager.export_into(commands_list, nameoffile)
    except FileNotFoundError as error:
        print("\n")
        print(lang.get_mensajes("THERE_IS_NOT_FILE") + nameoffile)


def suggestion_printed(desc):
    """This method will print the message showing the user what should be the expected output

    Parameters:
    desc (String): Description of the executed command

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    result = desc.split(". ")
    if len(result) > 1:
        print(result[1])


def run(cmd):
    """This function runs the specified command in PowerShell

    Parameters:
    cmd (String): Command to be executed

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    p = subprocess.Popen(["powershell.exe", cmd], shell=True, stdout=subprocess.PIPE, universal_newlines=True,
                         text=True).communicate()[0]
    p = p.replace(" ", "á")
    p = p.replace("¢", "ó")
    print(p)


def use_module(args):
    """This is the main method of the interpreter class. Its function is to interpret the command that is passed to
    as a parameter and then running it

    Parameters:
    args (String array): The command to be executed

    Returns:
    Nothing

    @author: Álvaro García Infante
   """
    module_to_use = args[0]
    modules = json_manager.get_modules(module_to_use)

    if len(args) == 1 and module_to_use == 'help':
        help_message()
    else:
        command = args[1]
        if module_to_use == 'create':
            create_new_command(command)

        elif module_to_use == 'run':
            run_combination(modules, args[1])

        elif module_to_use == 'import':
            import_module(args)

        elif module_to_use == 'export':
            export_module(args)

        elif module_to_use == 'set':
            lang.set_language(args[2])

        else:
            for module in modules:
                if module['nombre'].lower() == command.lower():
                    if module_to_use == 'help':
                        description = module['desc']
                        print("\n")
                        if lang.detect_language() == 'English':
                            aux = translator.translate(description)
                            print(aux)
                        else:
                            print(description)
                    else:
                        command_to_use = module['comando'].replace("!", "\!")
                        if module['comando'].count("sudo") == 1:
                            print(lang.get_mensajes("YOU_NEED_ROOT"))
                        if module['comando'].count("PARAM") == 1:
                            command_to_use = command_to_use.replace("PARAM", args[2])
                        if module['comando'].count("APACHE") > 0:
                            command_to_use = command_to_use.replace("APACHE", json_manager.conf("APACHE"))
                        if module['comando'].count("PASSWORD") > 0:
                            command_to_use = command_to_use.replace("PASSWORD", json_manager.conf("PASSWORD"))
                        print("\n")
                        print(lang.get_mensajes("EXECUTED_ORDER_IS") + command_to_use)
                        suggestion_printed(module['desc'])
                        if lang.os == 'Windows':
                            run(command_to_use)
                        else:
                            os.system(command_to_use)
    print('\n')
