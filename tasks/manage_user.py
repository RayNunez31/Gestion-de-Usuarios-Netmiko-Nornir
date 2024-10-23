from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config

# Función para crear un usuario
def create_user(task, username, password):
    username_str = str(username)
    task.run(netmiko_send_config, config_commands=[f"username {username} privilege 15 secret {password}"])  # Ajusta el expect_string según la salida esperada

# Función para eliminar un usuario
def delete_user(task, username):
    username_str = str(username)
    task.run(netmiko_send_config, config_commands=[f"no username {username}"])  # Ajusta el expect_string según la salida esperada

#Funcion para ver los usuarios configurados en el router
def show_users(task):
    task.run(netmiko_send_command, command_string="show running-config | include username")