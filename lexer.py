# lexer.py

import importlib
import json_manager
import interpreter
import lang
from datetime import datetime

history = []
first_methods_list = ['Create', 'Help', 'Run level', 'Import', 'Export']

"""
This module is used to connect to check that the grammar of the user is correct, in case that it is incorrect it will
tell the user why it is incorrect and how he can make it correct. After checking the grammar it will call the interpreter module.
"""


def check_parts(parts, line):
    """This method will check that all the orders from the user are correctly written. In case any of the orders
    is not correctly written it will rise an assertion exception with the message showing what was the problem.

    Parameters:
    parts (array string): Order to be checked
    line (int): Line of the order

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    if len(parts) == 1 and parts[0]!= 'import':
        assert (parts[
                    0] == 'help'), lang.get_mensajes("TOO_LITTLE_TERMS")
    if parts[0] == 'create' and len(parts[1]) > 0:
        assert (
                len(parts) == 2), lang.get_mensajes("CREATE_PROBLEM")
    if parts[0] == 'help' and len(parts) > 1:
        assert (
                len(parts) == 2), lang.get_mensajes("HELP_PROBLEM")
        check_help_terms(parts, line)
    if parts[0] != 'help' and parts[0] != 'create' and parts[0] != 'run' and parts[0] != 'import' and parts[
        0] != 'export' and parts[0] != 'set' and len(parts) > 1:
        check_terms(parts, line)
    if parts[0] == 'run':
        assert len(
            parts) == 2, lang.get_mensajes("RUN_GRAMMAR")
        assert parts[1].lower() == 'level1' or parts[
            1].lower() == 'level2', lang.get_mensajes("RUN_PROBLEM")
    if parts[0] == 'export':
        assert parts[
                   len(parts) - 2].lower() == 'into', lang.get_mensajes("EXPORT_PROBLEM")
    if parts[0] == 'import':
        assert parts[
                   1] == 'from', lang.get_mensajes("IMPORT_PROBLEM")
    if parts[0] == 'set':
        assert parts[1] == 'language' and len(parts) == 3, lang.get_mensajes("LANGUAGE_PROBLEM")


def select_common(terms, word):
    """This method is used to get the term that is similar to the typed word. It is used to predict the input from the user.

    Parameters:
    terms (array): Array of terms that need to be compared
    word (String): Word typed

    Returns:
    String:Predicted word

    @author: Álvaro García Infante
   """
    if len(terms) == 1:
        return terms[0]

    terms.sort(key=len)
    word_to_compare = terms[0]
    current_words = []
    for i in range(1, len(terms)):
        current_word = ''
        for j in range(0, len(word_to_compare)):
            a = word_to_compare[j].lower()
            b = terms[i][j].lower()
            if a == b:
                current_word = current_word + word_to_compare[j]
            else:
                break
        current_words.append(current_word)

    current_word_to_compare = current_words[0]
    for c in current_words:
        if len(c) < len(current_word_to_compare):
            current_word_to_compare = c
    return current_word_to_compare


def select_common_second(terms, word):
    """This method is used to get the term that is similar to the typed word. It is used to predict the input from the user.
    It is similar to the select_common but for the commands inside the packages

    Parameters:
    terms (array): Array of terms that need to be compared
    word (String): Word typed

    Returns:
    String:Predicted word

    @author: Álvaro García Infante
   """
    if len(terms) == 1:
        return terms[0]['nombre']
    if len(terms) == 0:
        return ''
    terms.sort(key=len)
    word_to_compare = terms[0]['nombre']

    current_words = []
    for i in range(1, len(terms)):
        current_word = ''
        for j in range(0, len(word_to_compare)):
            a = word_to_compare[j].lower()
            b = terms[i]['nombre'][j].lower()
            if a == b:
                current_word = current_word + word_to_compare[j]
            else:
                break
        current_words.append(current_word)

    current_word_to_compare = current_words[0]
    for c in current_words:
        if len(c) < len(current_word_to_compare):
            current_word_to_compare = c
    return current_word_to_compare


def predict(term):
    """This method takes a string and predicts the word that the user may refer to

    Parameters:
    tern (String): Current word

    Returns:
    String: Predicted word

    @author: Álvaro García Infante
   """
    word_predicted = term
    terms = term.split()
    predicted_terms = []
    if len(terms) == 1:
        key_list = json_manager.get_modules_json().keys()
        predicted_terms = predict_first_terms(key_list, terms[0].lower())
        word_predicted = select_common(predicted_terms, term)
    if len(terms) == 2:
        if terms[0].lower() == 'help':
            values_list = json_manager.get_all_modules()
        else:
            values_list = json_manager.get_modules(terms[0].lower())
        predicted_terms = predict_second_terms(values_list, terms[1].lower())
        word_predicted = select_common_second(predicted_terms, term)

    return word_predicted


def predict_first_term(list, term):
    """It will predict which first term does the user tries to refer when making an error

    Parameters:
    list (list): List of possible terms
    term (int): Description of arg1

    Returns:
    String: Word predicted

    @author: Álvaro García Infante
   """
    prediction = list
    temp = []
    detected_items_in_the_loop = False
    detected_items_in_this_round = False
    for i in range(0, len(term)):
        b = term.lower()[i:i + 1]
        for item in prediction:
            a = item.lower()[i:i + 1]
            if a == b:
                detected_items_in_this_round = True
                detected_items_in_the_loop = True
                temp.append(item)
        if detected_items_in_this_round:
            prediction = temp
        else:
            break;
        detected_items_in_this_round = False
        temp = []

    if len(prediction) > 0 and detected_items_in_the_loop:
        return prediction[0]
    else:
        return ""


def predict_second_term(list, term):
    """It will predict which second term does the user tries to refer when making an error

    Parameters:
    list (list): List of possible terms
    term (int): Description of arg1

    Returns:
    String: Word predicted

    @author: Álvaro García Infante
   """
    prediction = list
    temp = []
    detected_items_in_the_loop = False
    detected_items_in_this_round = False

    for i in range(0, len(term)):
        b = term.lower()[i:i + 1]
        for aux in prediction:
            a = aux['nombre'].lower()[i:i + 1]
            if a == b:
                detected_items_in_this_round = True
                detected_items_in_the_loop = True
                temp.append(aux)
        if detected_items_in_this_round:
            prediction = temp
        else:
            break;
        detected_items_in_this_round = False
        temp = []

    if len(prediction) > 0 and detected_items_in_the_loop:
        return prediction[0]
    else:
        return ""


def predict_first_terms(l, term):
    """It will predict which first terms does the user tries to refer when making an error

    Parameters:
    l (list): List of possible terms
    term (int): Description of arg1

    Returns:
    String: Word predicted

    @author: Álvaro García Infante
   """
    prediction = list(l)
    prediction.extend(first_methods_list)
    temp = []
    detected_items_in_the_loop = False
    detected_items_in_this_round = False
    for i in range(0, len(term)):
        b = term.lower()[i:i + 1]
        for item in prediction:
            a = item.lower()[i:i + 1]
            if a == b:
                detected_items_in_this_round = True
                detected_items_in_the_loop = True
                temp.append(item)
        if detected_items_in_this_round:
            prediction = temp
        else:
            break;
        detected_items_in_this_round = False
        temp = []

    if len(prediction) > 0 and detected_items_in_the_loop:
        return prediction
    else:
        return ""


def predict_second_terms(l, term):
    """It will predict which second terms does the user tries to refer when making an error

    Parameters:
    l (list): List of possible terms
    term (int): Description of arg1

    Returns:
    String: Word predicted

    @author: Álvaro García Infante
   """
    prediction = list(l)
    temp = []
    detected_items_in_the_loop = False
    detected_items_in_this_round = False

    for i in range(0, len(term)):
        b = term.lower()[i:i + 1]
        for aux in prediction:
            a = aux['nombre'].lower()[i:i + 1]
            if a == b:
                detected_items_in_this_round = True
                detected_items_in_the_loop = True
                temp.append(aux)
        if detected_items_in_this_round:
            prediction = temp
        else:
            break;
        detected_items_in_this_round = False
        temp = []

    if len(prediction) > 0 and detected_items_in_the_loop:
        return prediction
    else:
        return ""


def check_terms(parts, line):
    """It will check the terms over the read line to check for a correct grammar using other methods

    Parameters:
    parts (array String): Read line
    line (int): Line number

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    module_to_use = parts[0]

    first_test = False
    key_list = json_manager.get_modules_json().keys()
    for key in key_list:
        if key.lower() == module_to_use.lower():
            first_test = True
            break;

    message = lang.get_mensajes("FIRST_TERM_DOES_NOT_MATCH")
    if not first_test:
        predicted_word = predict_first_term(key_list, module_to_use.lower())
        if len(predicted_word) > 0:
            message = lang.get_mensajes("FIRST_TERM_DOES_NOT_MATCH_MAYBE + predicted_word")

    assert first_test, message

    second_test = False
    values_list = json_manager.get_modules(module_to_use)
    number_of_parameters = 0
    for term in values_list:
        if term['nombre'].lower() == parts[1].lower():
            second_test = True
            number_of_parameters = term['comando'].count("PARAM")
            break;

    message = lang.get_mensajes("SECOND_TERM_DOES_NOT_MATCH")
    if not second_test:
        predicted_word = predict_second_term(values_list, parts[1].lower())
        if len(predicted_word) > 0:
            message = lang.get_mensajes("SECOND_TERM_DOES_NOT_MATCH_MAYBE") + \
                      predicted_word['nombre']

    assert second_test, message
    assert (number_of_parameters == len(
        parts) - 2), lang.get_mensajes("PARAM_ERRORS") + str(
        line) + lang.get_mensajes("MUST_HAVE") + \
                     str(number_of_parameters) + lang.get_mensajes("PARAMS")


def check_help_terms(parts, line):
    """It will check the terms over the read line to check for a correct grammar in the help method

    Parameters:
    parts (array String): Read line
    line (int): Line number

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    second_test = False
    values_list = json_manager.get_all_modules()

    for term in values_list:
        if term['nombre'].lower() == parts[1].lower():
            second_test = True
            break;

    message = lang.get_mensajes("SECOND_TERM_DOES_NOT_MATCH")
    if not second_test:
        predicted_word = predict_second_term(values_list, parts[1].lower())
        if len(predicted_word) > 0:
            message = lang.get_mensajes("SECOND_TERM_DOES_NOT_MATCH_MAYBE") + \
                      predicted_word['nombre']
    assert second_test, message


def save_into_history_file(line):
    """Method to save the history into a file

    Parameters:
    line (int): Number of the line

    Returns:
    none

    @author: Álvaro García Infante
   """
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    f = open("history", "a")
    f.write(dt_string + " >> " + line + "\n")
    f.close()


def check_grammar(text):
    """It will check the terms over the whole text of the user to check for a correct grammar using the rest
    of the methods of the class

    Parameters:
    text (String): Read text

    Returns:
    nothing

    @author: Álvaro García Infante
   """
    count = 0
    for line in text.splitlines():
        history.append(line)
        save_into_history_file(line)
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        try:
            check_parts(parts, count)
            interpreter.use_module(parts)
        except AssertionError as error:
            print(error)

        count + 1
