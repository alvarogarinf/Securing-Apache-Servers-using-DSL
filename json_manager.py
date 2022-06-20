# json_manager.py

import json
import io
import lang


file = "comandosApacheWindows.json" if lang.check_os() else "comandosApache" + lang.check_linux_os() + ".json"


"""
This module is used to work with the json files and help other modules that need this task.
"""

def get_modules_json():
    """Get the modules from the json file of the commands

    Parameters:
    none

    Returns:
    dict:All the modules that are inside the json file

    @author: Álvaro García Infante
   """
    with io.open(file, 'r', encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data


def get_modules(module_to_use):
    """Get all the modules as a list, which name is the same as the parameter

    Parameters:
    module_to_use (string): The module which name is used to extract th

    Returns:
    list: Returns the modules that are inside the module which is the parameter

    @author: Álvaro García Infante
   """
    modules_json = get_modules_json()
    dictionary = dict()
    modules = list()
    for namespace, modulesList in modules_json.items():
        for module in modulesList:
            module['namespace'] = module_to_use
            dictionary[module['namespace']] = dict()
            modules.append(module)
    return modules


def get_all_modules():
    """Get all the modules as a list

    Parameters:
    none

    Returns:
    list: Return all the modules of the system as a list

    @author: Álvaro García Infante
   """
    modules_json = get_modules_json()
    modules = list()
    for namespace, modulesList in modules_json.items():
        for module in modulesList:
            modules.append(module)
    return modules


def write_new_command(name, desc, comando):
    """This method will write the new command into the JSON file

    Parameters:
    name (String): Name of the command that needs to be written
    desc (String): Description of the command
    comando (String): Actual command that will be run

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    entry = {
        "nombre": name,
        "desc": desc,
        "comando": comando
    }

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        others = data.get("Others")
        others.append(entry)
        data.update()
        new_data = data.copy()

    with open(file, "w", encoding="utf-8") as f:
        json.dump(new_data, f)


def append_import_to_file(entries, filename):
    """Method to append to the file "Import" zone, which will add in the "Import" section the needed entries

    Parameters:
    entries (array of json): Entries that will be append into the file
    filename (String): Name of the file

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        others = data.get("Imported")
        for entry in entries:
            if entry not in others:
                others.append(entry)
            else:
                print(lang.get_mensajes("IMPORT_PROBLEM") + entry[
                    'nombre'] + lang.get_mensajes("IMPORT_ALREADY_EXISTS"))
                print(lang.get_mensajes("ADD_COMMAND_MANUALLY + filename"))
        data.update()
        new_data = data.copy()

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(new_data, f)


def export_into(list, filename):
    """Export list of commands into the file

    Parameters:
    list (list): List of commands that will be exported
    filename (String): Name of the file that will receive the commands

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    entries = []
    for module in get_all_modules():
        for command in list:
            if module['nombre'].lower() == command.lower():
                entry = {
                    "nombre": module['nombre'],
                    "desc": module['desc'],
                    "comando": module['comando']
                }
                entries.append(entry)
    append_import_to_file(entries, filename)


def import_into(command_list, filename):
    """Import command list into the json file

    Parameters:
    command_list (list): List of commands that will be imported
    filename (String): Name of the file that the commands will be imported into

    Returns:
    none

    @author: Álvaro García Infante
   """
    with io.open(filename, 'r', encoding="utf-8") as json_file:
        modules_json = json.load(json_file)

    modules = list()
    for namespace, modulesList in modules_json.items():
        for module in modulesList:
            modules.append(module)

    entries = []
    for module in modules:
        if len(command_list) == 0:
            entry = {
                "nombre": module['nombre'],
                "desc": module['desc'],
                "comando": module['comando']
            }
            entries.append(entry)
        else:
            for command in command_list:
                if module['nombre'].lower() == command.lower():
                    entry = {
                        "nombre": module['nombre'],
                        "desc": module['desc'],
                        "comando": module['comando']
                    }
                    entries.append(entry)

    append_import_to_file(entries, file)


def conf(term):
    """This methods is used to get the specific paths of the apache folder to run the commands

    Parameters:
    term (String): Term that will be checked for keywords in case it needs to change a path

    Returns:
    string: the term corrected with the actual path

    @author: Álvaro García Infante
   """
    f = open(("conf/configuration"+lang.os))
    apache = f.readline()
    password = f.readline()
    if term == "APACHE":
        apache = apache.replace("APACHE=", "")
        apache = apache.replace("\n", "")
        apache = apache.replace(" ", "")
        return apache
    if term == "PASSWORD":
        password = password.replace("PASSWORD=", "")
        password = password.replace("\n", "")
        password = password.replace(" ", "")
        return password

