# Funciones y multiples valores de return

def my_function():
    result = 3*2
    return result

output = my_function()

print(output)

print ("\n -----------------------\n")

# Crear una funcion con dos entradas y una salida
def format_name(f_name, l_name):
    f_name = f_name.title()  #.title() pasa todas las palabras a minusculas iniciando con mayuscula (paOlA = Paola)
    l_name = l_name.title()
    formated_name = f_name + " " + l_name
    return formated_name

New_name = format_name(input("Dame primer nombre: "), input("Dame tu apellido: "))

print(New_name)

print ("\n -----------------------\n")

# Funcion con varios outputs

def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "Entradas invalidas"
    else :
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"


print(format_name(input("Dame tu primer nombre: "), input("Dame tu apellido: ")))

print ("\n -----------------------\n")

def format_name(f_name, l_name):
    """
    Docstrings: Se usan para darle documentacion a la funcion \n
    Funcion que cambia el formato de un nombre
    :param f_name:
    :param l_name:
    :return:
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

print ("\n -----------------------\n")