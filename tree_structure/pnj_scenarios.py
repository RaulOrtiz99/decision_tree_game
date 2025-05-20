from .decision_tree import DecisionNode
from .fsm import EstadoMaquina
from .utils import elegir_accion_aleatoria

# Guardia con condiciones numéricas
def crear_arbol_guardia():
    return DecisionNode(
        lambda e: e["salud_jugador"] > 70,
        si=DecisionNode(
            lambda e: e["distancia_al_jugador"] < 10,
            si=DecisionNode(resultado="Atacar"),
            no=DecisionNode(resultado="Patrullar")
        ),
        no=DecisionNode(
            lambda e: e["conoce_jugador"],
            si=DecisionNode(resultado="Saludar"),
            no=DecisionNode(resultado="Ignorar")
        )
    )

# Mago con árbol de decisión + aleatoriedad
def crear_arbol_mago():
    return DecisionNode(
        lambda e: e["mana_actual"] > 50,
        si=DecisionNode(
            lambda e: e["enemigo_cerca"],
            si=DecisionNode(
                lambda e: e["objetivo_valioso"],
                si=DecisionNode(resultado="Lanzar hechizo poderoso"),
                no=DecisionNode(resultado="Usar hechizo básico")
            ),
            no=DecisionNode(resultado="Recargar maná")
        ),
        no=DecisionNode(resultado="Esperar")
    )

# Vendedor con sistema de prioridad
def crear_arbol_vendedor():
    return DecisionNode(
        lambda e: e["dinero_suficiente"],
        si=DecisionNode(
            lambda e: e["producto_disponible"],
            si=DecisionNode(resultado="Ofrecer producto"),
            no=DecisionNode(resultado="Sin stock")
        ),
        no=DecisionNode(resultado="Dinero insuficiente")
    )

# Ejecutar FSM para mejorar lógica de comportamiento
def ejecutar_fsm(tipo_pnj, estado_juego):
    fsm = EstadoMaquina()

    if tipo_pnj == "guardia":
        if estado_juego["salud_jugador"] > 50:
            fsm.actualizar_estado("detectar_jugador")
            if estado_juego["distancia_al_jugador"] < 10:
                fsm.actualizar_estado("atacar")
            else:
                fsm.actualizar_estado("patrullar")
        else:
            fsm.actualizar_estado("reset")

    elif tipo_pnj == "mago":
        if estado_juego["mana_actual"] > 50:
            if estado_juego["enemigo_cerca"]:
                if estado_juego["objetivo_valioso"]:
                    acciones = [("Lanzar hechizo poderoso", 60), ("Usar hechizo básico", 40)]
                else:
                    acciones = [("Usar hechizo básico", 80), ("Esperar", 20)]
                resultado = elegir_accion_aleatoria(acciones)
                return resultado
            else:
                return "Recargar maná"
        else:
            return "Esperar"

    elif tipo_pnj == "vendedor":
        if estado_juego["dinero_suficiente"]:
            if estado_juego["producto_disponible"]:
                return "Vender"
            else:
                return "Sin stock"
        else:
            return "Dinero insuficiente"

    return fsm.get_accion()