from django import forms

class EstadoForm(forms.Form):
    salud_jugador = forms.IntegerField(label='Salud del Jugador', min_value=0, max_value=100, initial=50)
    distancia_al_jugador = forms.IntegerField(label='Distancia al jugador', min_value=0, max_value=100, initial=20)
    conoce_jugador = forms.BooleanField(label='¿Te conoce?', required=False)

    mana_actual = forms.IntegerField(label='Maná actual', min_value=0, max_value=100, initial=50)
    enemigo_cerca = forms.BooleanField(label='¿Enemigo cerca?', required=False)
    objetivo_valioso = forms.BooleanField(label='¿Objetivo valioso?', required=False)

    dinero_suficiente = forms.BooleanField(label='¿Tiene suficiente dinero?', required=False)
    producto_disponible = forms.BooleanField(label='¿Producto disponible?', required=False)