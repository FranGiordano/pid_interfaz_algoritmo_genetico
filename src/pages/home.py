import dash
from dash import html, callback, Input, Output, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path="/",
                   title="PID",
                   update_title="PID",
                   name="PID")

layout = dbc.Container([
    # html.H1(children='Algoritmos Genéticos', style={'textAlign': 'center'}),
    # html.Br(),
    # html.Span(f"""
    #     En ocasiones la computación se basa en procesos observados de la naturaleza para
    #     resolver ciertos problemas. Un algoritmo genético trata de replicar el modelo de
    #     selección natural que propuso Darwin, el cual básicamente dice que, dentro de una
    #     población, los individuos que sobreviven son aquellos que están más adaptados al
    #     medio. Además, esta teoría de la evolución introduce un concepto muy interesante
    #     que son las mutaciones. Una mutación es un pequeño cambio que se produce de
    #     manera aleatoria en ciertos individuos e introduce de esta manera versatilidad en las
    #     poblaciones. Habrá mutaciones que den lugar a cambios favorables y otros
    #     desfavorables.
    #     Los algoritmos genéticos se utilizan para resolver problemas de búsqueda y
    #     optimización pues se basan en hacer evolucionar poblaciones de soluciones hacia
    #     valores óptimos del problema.
    # """)
    dcc.Markdown('''
    # Algoritmos Genéticos
    En ocasiones la computación se basa en procesos observados de la naturaleza para
    resolver ciertos problemas. Un algoritmo genético trata de replicar el modelo de
    selección natural que propuso Darwin, el cual básicamente dice que, dentro de una
    población, los individuos que sobreviven son aquellos que están más adaptados al
    medio. Además, esta teoría de la evolución introduce un concepto muy interesante
    que son las mutaciones. Una mutación es un pequeño cambio que se produce de
    manera aleatoria en ciertos individuos e introduce de esta manera versatilidad en las
    poblaciones. Habrá mutaciones que den lugar a cambios favorables y otros
    desfavorables.
    
    Los **algoritmos genéticos** se utilizan para **resolver problemas de búsqueda y
    optimización** pues se basan en hacer evolucionar poblaciones de soluciones hacia
    valores óptimos del problema.
    
    ### Conceptos útiles
    
    * **Individuo**: los individuos de nuestra población son las posibles soluciones al problema
    que estamos tratando.
    
    * **Población**: conjunto de individuos (soluciones).
    
    * **Función fitness o de adaptación**: función que evalúa a los individuos y les asigna una
    puntuación en función de lo buenas soluciones que sean para el problema.
    
    * **Función de cruce**: función que, dados dos individuos, genera dos ‘descendientes’ a
    partir de la combinación de genes de sus ‘padres’. Esta función se diseña
    especialmente para el problema que se esté tratando y, por lo general, se encarga de
    que los hijos sean mejores soluciones que los padres.
    
    ### Estructura del algoritmo genético
    
    Entonces, la estructura de un algoritmo genético es la siguiente:
    
    1. **Fase inicial**: Se genera una población inicial de individuos (soluciones), usualmente de manera
    aleatoria.
    
    2. **Fase de evaluación**: se evalúan los individuos de la población con la función fitness.
    
    3. **Fase de selección**: se seleccionan los mejores individuos.
    
    4. **Fase de reproducción**: se cruzan los individuos seleccionados mediante la función de
    cruce, dando lugar a una nueva generación que va a sustituir a la anterior.
    
    5. **Fase de mutación**: se introducen mutaciones (pequeños cambios) en ciertos
    individuos de la nueva población de manera aleatoria.
    
    6. **Tenemos una nueva generación, generalmente, con soluciones mejores que la
    anterior. Volvemos al punto 2**.
    
    Los algoritmos genéticos finalizan o bien cuando alcanzan un número de generaciones
    concreto o cuando cumplen una condición de parada.
    
    ### Limitaciones presentes en Algoritmos genéticos
    
    * La definición de la función de aptitud debe ser bien definida, dado que de no
    ser así el algoritmo puede que no resulte capaz de brindarnos soluciones ó bien
    que presentes errores respecto al problema.
    
    * Los problemas complejos donde se presenta una gran cantidad de elementos
    no resultan factibles de resolver dado que implica un extenso espacio de
    búsqueda y por lo tanto dificultad a la hora de encontrar soluciones.
    
    * Elección de lenguaje robusto para encontrar soluciones de modo tal que tolere
    cambios aleatorios sin producir errores o resultados incorrectos.
    
    A modo de facilitar el aprendizaje y la práctica en lo que respecta a los Algoritmos genéricos en
    la asignatura Inteligencia Artificial, a continuación se propone la resolución del problema de la
    mochila con el algoritmo genético general y la variante del enjambre de partículas.
    ''')],

    style={'text-align': 'justify', 'minWidth': '1200px', 'maxWidth': '1200px'}
)
