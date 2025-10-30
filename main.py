from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from tasks.manage_user import create_user, delete_user, show_users

# Inicializar Nornir
nr = InitNornir(config_file="config.yaml")  # Asegúrate de tener el archivo de configuración


while True:
    # Menú de opciones
    print("\nSeleccione una opción:")
    print("1. Crear un nuevo usuario")
    print("2. Eliminar un usuario existente")
    print("3. Mostrar usuarios configurados")

    # Solicitar al usuario que seleccione una opción
    option = input("Ingrese el número de la opción (1, 2 o 3): ")

    # Solicitar al usuario que ingrese el tipo de destino (todos, equipo o grupo)
    target_type = input("¿Desea aplicar la acción a todos los equipos (A), a un equipo específico (E) o a un grupo específico (G)? Ingrese 'A', 'E' o 'G': ").strip().upper()

    if target_type == 'A':
        device = nr  # Aplica a todos los dispositivos

    elif target_type == 'E':
        # Solicitar al usuario que ingrese el nombre del equipo
        target_device = input("Ingrese el nombre del equipo: ")
        device = nr.filter(name=target_device)

    elif target_type == 'G':
        # Solicitar al usuario que ingrese el nombre del grupo
        target_group = input("Ingrese el nombre del grupo: ")
        device = nr.filter(group=target_group)

    else:
        print("Opción de destino no válida. Por favor, ingrese 'A', 'E' o 'G'.")
        continue  # Vuelve al inicio del bucle

    if option == '1':
        # Solicitar al usuario que ingrese el nombre de usuario y la contraseña
        new_username = input("Ingrese el nombre del nuevo usuario: ")
        new_password = input("Ingrese la contraseña del nuevo usuario: ")

        # Crear usuario en el dispositivo o grupo especificado
        result_create = device.run(task=create_user, username=new_username, password=new_password)
        print_result(result_create)

    elif option == '2':
        # Solicitar al usuario que ingrese el nombre del usuario a eliminar
        del_username = input("Ingrese el nombre del usuario a eliminar: ")

        # Eliminar usuario en el dispositivo o grupo especificado
        result_delete = device.run(task=delete_user, username=del_username)
        print("\nResultados de la eliminación del usuario:")
        print_result(result_delete)

    elif option == '3':
        # Mostrar usuarios existentes en el dispositivo o grupo especificado
        print("\nMostrando usuarios existentes:")
        result_show = device.run(task=show_users)
        print_result(result_show)

    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        continue  # Vuelve al inicio del bucle

    # Preguntar si el usuario desea salir
    exit_program = input("\n¿Desea salir del programa? (S para sí, C para continuar): ").strip().upper()
    if exit_program == 'S':
        print("Saliendo del programa...")
        break  # Sale del bucle y termina el programa
