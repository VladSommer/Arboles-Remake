# Clase del nodo
class Node:
    # Constructor
    def __init__(self, name, data):
        self.name = name # Nombre del nodo
        self.data = data # dato
        self.children = [] # Hijos
        self.parent_pointer: Node # Puntero al padre 
    
    # Metodo para añadir un hijo
    def add_child(self, name, value):
        new_node = Node(name, value)
        new_node.parent_pointer = self
        self.children.append(new_node)
    
    # Representacion en forma de string del Nodo
    def __str__(self) -> str:
        return f"({self.name} : {self.data})"

    # Representacion en forma de string de los hijos del Nodo
    def get_children_as_str(self) -> str:
        v = ""
        for i in self.children:
            v += str(i) + " "

        return f"[ {v}]"

# Obtener un arbol especificando la raiz y el nombre
def get_node(root: Node, name: str) -> Node:
    if root is None: return # Retorna si la raiz no existe

    queue = [root] # Cola para para la iteracion
    nodes = [] # Lista de nodos recolectados

    while queue:
        current_node = queue.pop()
        nodes.append(current_node) # Añadir el nodo actual a la lista
        
        # Añadir los hijos del nodo actual a la lista
        for c in current_node.children:
            nodes.append(c) 

    # Recorrer los nodos obtenidos y retornar el nodo especificado
    for i in nodes:
        if i.name == name:
            return i

    # Retornar None en caso de que el nodo no haya sido encotrado
    return None # type: ignore

# Imprimir El padre y los hijos de un nodo dado
def print_parent_and_child(node: Node):
    # terminar la ejecucion si el nodo no existe
    if node is None:
        print("Ese nodo no existe")
        return

    try:
        # Se ejecuta si el padre existe
        print(f"{str(node.parent_pointer)} -> {str(node)} -> {node.get_children_as_str()}")
        
    except AttributeError:
        # Se ejecuta si el padre NO existe
        print(f"{str(node)} -> {node.get_children_as_str()}")

#* =============== EJEMPLOS PRACTICOS ===============

# NOTE: el dato de los nodos son usados como pequeñas descripciones

#* EJEMPLO: Sistema de archivos
# disco C
root_dir = Node("C", "Directorio C")

# Hijos de C
root_dir.add_child("Windows", "Carpeta del OS")
root_dir.add_child("ProgramFiles", "Archivos de programa")
root_dir.add_child("Users", "Carpeta Usuarios")

# Obtener los hijos de C
windows_dir = get_node(root_dir, "Windows")
program_files_dir = get_node(root_dir, "ProgramFiles")
users_dir = get_node(root_dir, "Users")

# Hijos de Windows
windows_dir.add_child("explorer.exe", "EXE del explorador de archivos")
windows_dir.add_child("regedit.exe", "EXE del editor de registros")
windows_dir.add_child("System32", "No necesita introduccion")

# Hijos de Program Files
program_files_dir.add_child("JetBrains", "Archivos de los IDES de Jet Brians")
program_files_dir.add_child("Inkscape", "Archivos de Inkscape")
program_files_dir.add_child("Google", "Archivos de Google")

# Obtener los hijos de Program Files
jet_brains_dir = get_node(program_files_dir, "JetBrains")
inkscape_dir = get_node(program_files_dir, "Inkscape")
google_dir = get_node(program_files_dir, "Google")

# Hijos de Jetbrains
jet_brains_dir.add_child("IntelliJ IDEA", "Archivos de IntelliJ Idea")
jet_brains_dir.add_child("WebStorm", "Archivos de WebStorm")
jet_brains_dir.add_child("Pycharm", "Archivos de Pycharm")

# Hijo de Users
users_dir.add_child("Vlad", "Usuario Vlad")

# Obtener el hijo de User
username_dir = get_node(users_dir, "Vlad")

# Hijos de "Vlad"
username_dir.add_child("Desktop", "Escritorio")
username_dir.add_child("Downloads", "Descargas")
username_dir.add_child("Images", "Imagenes")
username_dir.add_child("Videos", "Videos")
username_dir.add_child("Music", "Musica")

#* EJEMPLO: Rockstar games
# Raiz del proyecto
project_root = Node("GTA VI", "Proyecto de GTA VI")

# Director del juego
project_root.add_child("Director", "Director de juego")
game_director = get_node(project_root, "Director")

# Hijos del Director
game_director.add_child("Programmers", "Programadores")
game_director.add_child("Artists", "Artistas")
game_director.add_child("Designers", "Diseñadors")
programmers = get_node(game_director, "Programmers")
artists = get_node(game_director, "Artists")
designers = get_node(game_director, "Designers")

# Hijos de Programadores
programmers.add_child("Gameplay Programmers", "Programadores de Gameplay")
programmers.add_child("AI Programmers", "Programadores de IA")
programmers.add_child("Networking Programmers", "Programadores de Networking")
programmers.add_child("Engine Programmers", "Programadores de Motor")
programmers.add_child("Software Engineers", "Ingenieros de Software")

# Hijos de Programadores de Motor
engine_programmers = get_node(programmers,"Engine Programmers")
engine_programmers.add_child("Graphics Programmers", "Programadores de Graficos")
engine_programmers.add_child("Physics Programmers", "Programadores de Fisicas")

# Hijos de Artistas
artists.add_child("Texture Artists", "Artista des Texturas")
artists.add_child("3D Modelers", "Modeladores 3D")
artists.add_child("Model Riggers", "Riggers de Modelos")
artists.add_child("Illustrators", "Ilustradores")

# Hijos de Diseñadores
designers.add_child("Character Designers", "Diseñadores de Personaje")
designers.add_child("Scenario Designers", "Diseñadores de Escenarios")
