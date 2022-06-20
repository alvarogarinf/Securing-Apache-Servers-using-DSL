import json_manager

import ctypes
import locale
import distro

"""
This module is used as a utils module, meaning that it will store the terms of the language, but it will also
check the operating system and get the running language of the outer system.
"""


def check_os():
    """Check which OS is being used by the system

    Parameters:
    none

    Returns:
    int: Returns 1 if it is windows or 0 if it is not

   """
    return 1 if __import__('os').name == 'nt' else 0


def check_linux_os():
    """Check which linux system is being run

    Parameters:
    none

    Returns:
    String:Return the linux distribution

   """
    dist = 'Ubuntu'
    if distro.linux_distribution()[0] == 'Ubuntu':
        dist = 'Ubuntu'
    if distro.linux_distribution()[0] == 'CentOS Linux':
        dist = 'Centos'
    return dist


os = "Windows" if check_os() else check_linux_os()

mensajes_español = {
    "WELCOME_MESSAGE": "Bienvenido al DSL version " + os,
    "START_MESSAGE": "Escriba a continuación las órdenes del lenguaje (help para ayuda)",
    "EXIT_MESSAGE": "Pulsa la letra x para cerrar la aplicación o ENTER para continuar escribiendo: ",
    "CHECK_NAME_IS_UNIQUE": "El nombre del comando debe ser unico, ya existe un comando con el nombre ",
    "INTRODUCE_DESC": "Introduce una descripción del nuevo comando: ",
    "INTRODUCE_ORDERS": "Introduce las ordenes exactas que debe ejecutar el sistema ",
    "PARAM_ADVISE": "(si tiene algún parámetro variable el comando, recuerda escribir PARAM en el sitio donde se situe el parámetro):",
    "HELP_1": "En caso de necesitar ayuda sobre un comando cualquiera X, escribir help X",
    "HELP_2": "En caso de querer definir una actualización sobre un comando Y, escribir create Y",
    "HELP_3": "En caso de querer usar un comando, escribir primero el nombre del grupo de comando por ejemplo: AppArmor, después el comando concreto por ejemplo: Ensure_AppArmor_Is_Enabled",
    "HELP_4": "En caso de desconocer el sistema, existe una opción de correr un conjunto de comandos con la orden: run level1 o run level2",
    "HELP_5": "En caso de querer exportar un comando o conjunto de comandos usar la orden: export nombre_del_comando_1, nombre_del_comando2, ... into nombre_del_archivo",
    "HELP_6": "En caso de querer importar un comando usar la orden: import from nombre_del_archivo_1 nombre_del_comando_1, nombre_del_comando2, ... . Si no se especifica que comandos importar, se importarán todos",
    "HELP_7": "Para ejecutar todos los comandos, pulsar la tecla ENTER dos veces, con una vez se cambia de línea",
    "HELP_8": "Si quieres cambiar el idioma escribir set language LANGUAGE. Siendo LANGUAGE el mensaje al que cambiar (Solo están disponibles Español e Inglés)",
    "EXECUTED_ORDER_IS": "La orden ejecutada es la siguiente: ",
    "THERE_IS_NOT_FILE": "No existe ningun archivo: ",
    "YOU_NEED_ROOT": "Para ejecutar el comando especificado, se necesita ser root",
    "IMPORT_PROBLEM": "Hubo un problema al importar el comando: ",
    "IMPORT_ALREADY_EXISTS": " ,ya existe un comando con ese nombre en la sección Imported",
    "ADD_COMMAND_MANUALLY": "Agregar el comando de forma manual modificando el JSON: ",
    "TOO_LITTLE_TERMS": '\nMuy pocos términos, solo el mensaje general de ayuda debe estar definido por un único comando help',
    "CREATE_PROBLEM": "En caso de necesitar crear un comando se usa create X, siendo X el nombre del comando",
    "HELP_PROBLEM": "En caso de necesitar usar ayuda de un comando se usa help X, siendo X el nombre del comando",
    "RUN_GRAMMAR": "En caso de querer combinaciones de paquetes, necesitas especificar que combinacion: level1 o level2",
    "RUN_PROBLEM": "Las combinaciones de paquete solo pueden ser o level1 o level2",
    "EXPORT_PROBLEM": "El comando export debe tener la siguiente estructura: export nombre_del_comando_1, nombre_del_comando2, ... into nombre_del_archivo",
    "FIRST_TERM_DOES_NOT_MATCH": "El primer término no corresponde con ninguno del lenguaje",
    "FIRST_TERM_DOES_NOT_MATCH_MAYBE": "El primer término no corresponde con ninguno del lenguaje. Quizás quisiste decir: ",
    "SECOND_TERM_DOES_NOT_MATCH": "\nEl segundo término no corresponde con ninguno del lenguaje",
    "SECOND_TERM_DOES_NOT_MATCH_MAYBE": "\nEl segundo término no corresponde con ninguno del lenguaje. Quizás quisiste decir: ",
    "PARAM_ERRORS": "Se ha producido un error con el número de parámetros, la función en la línea: ",
    "MUST_HAVE": " debe tener ",
    "PARAMS": " parámetros",
    "LANGUAGE_PROBLEM": "Si quieres cambiar el idioma escribir set language LANGUAGE. Siendo LANGUAGE el mensaje al que cambiar (Solo están disponibles Español e Inglés)"

}

mensajes_ingles = {
    "WELCOME_MESSAGE": "Welcome to DSL version " + os,
    "START_MESSAGE": "Write here the orders for the language (type help for help)",
    "EXIT_MESSAGE": "Type letter x to close the app or ENTER to continue: ",
    "CHECK_NAME_IS_UNIQUE": "The name of the command must be unique, there is already a command with the name )",
    "INTRODUCE_DESC": "Introduce a description of the new command: ",
    "INTRODUCE_ORDERS": "Introduce the exact orders that the system should execute ",
    "PARAM_ADVISE": "(if the command has any parameter, remember to type PARAM in the correct place):",
    "HELP_1": "In case of needing help of a command X, type Help x",
    "HELP_2": "In case of wanting to define a new command with name Y, write create Y",
    "HELP_3": "If you need to use a command, write first the name of the command, for example: AppArmor, then the concrete command, like this: Ensure_AppArmor_Is_Enabled",
    "HELP_4":
        "In case of not knowing the system, there is an option to run several basic commands at the same time with the order: run level1 o run level2",
    "HELP_5": "In case of wanting to export a command or a set of commands use the order: export name_of_command_1, name_of_command_2, ... into name_of_file",
    "HELP_6":
        "In case of wanting to import a command use the order: import from name_of_file name_of_command_1, name_of_command_2, ... . If the name of the command is not specified, all commands will be imported",
    "HELP_7": "In order to execute all commands, type ENTER two times, with one ENTER you change line",
    "HELP_8": "If you want to change the language write: set language LANGUAGE. LANGUAGE being the desired language (Only English and Spanish are available)",
    "EXECUTED_ORDER_IS": "The executed order is the following one: ",
    "THERE_IS_NOT_FILE": "That file does not exist: ",
    "YOU_NEED_ROOT": "You need to be root to execute the specified command",
    "IMPORT_PROBLEM": "The import command must have the following structure: import from name_of_file_1 name_of_command_1, name_of_command_2, ... . If the commands are not specified, all commands will be imported",
    "IMPORT_ALREADY_EXISTS": " ,there is already a command with that name in section Imported",
    "ADD_COMMAND_MANUALLY": "Add the command manually modifying the JSON: ",
    "TOO_LITTLE_TERMS": "\nVery few terms, only the general help message should be defined by a single command help",
    "CREATE_PROBLEM": "In case you need to create a command you use create x where x is the name of the command",
    "HELP_PROBLEM": "In case you need to use help for a command use help X, being X the name of the command",
    "RUN_GRAMMAR": "In case you want to run combinations of packagesm you need to specify: level1 or level2",
    "RUN_PROBLEM": "The combinations of packages can only be level1 or level2",
    "EXPORT_PROBLEM": "The command export must have the following structure: export name_of_command_1, name_of_command_2, ... into name_of_file_1",
    "IMPORT_PROBLEM": "The import command must have the following structure: import from name_of_file_1 name_of_command_1, name_of_command_2, ... . If the commands are not specified, all commands will be imported",
    "FIRST_TERM_DOES_NOT_MATCH": "The first term does not match any in the language",
    "FIRST_TERM_DOES_NOT_MATCH_MAYBE": "The first term does not match any in the language. Maybe you mean: ",
    "SECOND_TERM_DOES_NOT_MATCH": "\nThe second term does not match any in the language.",
    "SECOND_TERM_DOES_NOT_MATCH_MAYBE": "\nThe second term does not match any in the language. Maybe you mean: ",
    "PARAM_ERRORS": "There has been an error with the number of parameters, the function in the line: ",
    "MUST_HAVE": " must have ",
    "PARAMS": " params",
    "LANGUAGE_PROBLEM": "If you want to change the language write: set language LANGUAGE. LANGUAGE being the desired language (Only English and Spanish are available)",

}

aux = [""]


def get_mensajes(term):
    """Return the message in the correct language

    Parameters:
    term (String): Name of the term to be returned

    Returns:
    String: Message to be returned

   """
    if detect_language() == 'Español' or detect_language() == 'Spanish':
        return mensajes_español.get(term)
    else:
        return mensajes_ingles.get(term)


def detect_language():
    """Method to detect the language of the system

    Parameters:
    none

    Returns:
    String: Language of the system

   """
    if aux[0].lower() == "español" or aux[0].lower() == "spanish":
        return "Español"
    if aux[0].lower() == "english" or aux[0].lower() == "ingles":
        return "English"
    if os == 'Windows':
        windll = ctypes.windll.kernel32
        if locale.windows_locale[windll.GetUserDefaultUILanguage()] == 'es_ES':
            return "Español"
    return "English"


def set_language(param):
    """Set the language of the system

    Parameters:
    param (string): Language

    Returns:
    nothing

   """
    aux[0] = param
