from django.shortcuts import render
from .forms import EstadoForm
from tree_structure.pnj_scenarios import crear_arbol_guardia, crear_arbol_mago, crear_arbol_vendedor, ejecutar_fsm

def simulador_pnjs(request):
    form = EstadoForm()
    context = {
        'form': form,
        'accion_guardia': None,
        'accion_mago': None,
        'accion_vendedor': None,
        'estado_guardia': {},
        'estado_mago': {},
        'estado_vendedor': {}
    }

    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            estado_guardia = {
                "salud_jugador": int(form.cleaned_data['salud_jugador']),
                "distancia_al_jugador": int(form.cleaned_data['distancia_al_jugador']),
                "conoce_jugador": form.cleaned_data['conoce_jugador']
            }
            estado_mago = {
                "mana_actual": int(form.cleaned_data['mana_actual']),
                "enemigo_cerca": form.cleaned_data['enemigo_cerca'],
                "objetivo_valioso": form.cleaned_data['objetivo_valioso']
            }
            estado_vendedor = {
                "dinero_suficiente": form.cleaned_data['dinero_suficiente'],
                "producto_disponible": form.cleaned_data['producto_disponible']
            }

            guardia = crear_arbol_guardia()
            mago = crear_arbol_mago()
            vendedor = crear_arbol_vendedor()

            accion_guardia = guardia.tomar_decision(estado_guardia)
            accion_mago = mago.tomar_decision(estado_mago)
            accion_vendedor = vendedor.tomar_decision(estado_vendedor)

            accion_guardia_fsm = ejecutar_fsm("guardia", estado_guardia)
            accion_mago_fsm = ejecutar_fsm("mago", estado_mago)
            accion_vendedor_fsm = ejecutar_fsm("vendedor", estado_vendedor)

            context.update({
                'accion_guardia': accion_guardia_fsm,
                'accion_mago': accion_mago_fsm,
                'accion_vendedor': accion_vendedor_fsm,
                'estado_guardia': estado_guardia,
                'estado_mago': estado_mago,
                'estado_vendedor': estado_vendedor
            })

    return render(request, 'simulador.html', context)