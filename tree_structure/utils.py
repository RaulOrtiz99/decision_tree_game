def elegir_accion_aleatoria(acciones_con_peso):
    total = sum(peso for _, peso in acciones_con_peso)
    rand = random.uniform(0, total)
    acumulado = 0
    for accion, peso in acciones_con_peso:
        if acumulado + peso >= rand:
            return accion
        acumulado += peso