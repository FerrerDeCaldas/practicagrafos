from typing import Any, List
from collections import deque

class GrafoMatriz:

  def __init__(self):
    self.matrizAdy : List[List[int]] = []
    self.vertices : List[Any] = [] ## Lista con los nodos
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.vertices: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.vertices.append(valor) ## Agrega el vertice a lista de vertices
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

    for fila in self.matrizAdy:
      fila.append(0) ## Agrega una fila de ceros
    self.matrizAdy.append([0] * self.tamano) ## Agrega una columna de ceros

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.vertices:
      self.agregarVertice(vertice1)
    if vertice2 not in self.vertices:
      self.agregarVertice(vertice2)

    posV1 = self.vertices.index(vertice1) ## Entrega la posicion de el vertice 1 en la matriz de ady
    posV2 = self.vertices.index(vertice2) ## Entrega la posicion del vertice 2 en la matriz de adyacencia

    self.matrizAdy[posV1][posV2] = peso ## Hay un camino entre v1 y v2

    if not dirigido: ## Si no es dirigido debo agregar la relacion contraria
      self.matrizAdy[posV2][posV1] = peso

  def recorrerEnAnchura ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    cola = deque([verticeInicial])  ## Cola de pendientes por visitar
    while cola:  ## Mientras que tenga vertices pendientes por visitar
      vertice = cola.popleft()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano):  ## Recorrer la matriz ady para buscar vertices relacionados
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            cola.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados

  def recorrerEnProfundidad( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    pila = [verticeInicial]  ## Pila de pendientes por visitar
    while pila:  ## Mientras que tenga vertices pendientes por visitar
      vertice = pila.pop()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano - 1, -1, -1):  ## Recorrer la matriz ady para buscar vertices relacionados (Se recorre en sentio inverso)
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            pila.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados


  def encontrarCaminoMasCorto(self, verticeInicial : Any, verticeFinal : Any) -> tuple:
    if verticeInicial not in self.vertices or verticeFinal not in self.vertices:
      ## Si alguno de los 2 vertices no existe
      return (float('inf'), [])

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    distancias = { vertice : float('inf') for vertice in self.vertices }
    ## La distancia al vertice inicial es la unica que se conoce con antelacion
    distancias[verticeInicial] = 0

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    predecesores = { vertice : None for vertice in self.vertices }

    visitados = [] ## Lista donde almacenaremos los vertices cuando los hayamos visitado

    verticeActual = verticeInicial

    ## Mientras que el vertice actual sea un nodo valido y sea diferente al vertice final
    while verticeActual is not None and verticeActual != verticeFinal:
      ## Consultar todos los vecinos del vertice actual que no he visitado
      vecinosNoVisitados = []
      posicionVertice = self.vertices.index(verticeActual)
      for i in range(self.tamano):
        if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados:
          vecinosNoVisitados.append(self.vertices[i])
      ## Actualizar los recorridos de la mejor ruta conocida
      for vecino in vecinosNoVisitados:
        ## Busca en la matriz de ady el peso de la conexion entre el vertice actual y el vecino no visitado
        pesoConexion = self.matrizAdy[posicionVertice][self.vertices.index(vecino)]
        ## acumula la mejor distancia conocida con la conexion actual
        distancia = distancias[verticeActual] + pesoConexion
        ## Si encontre una distancia menor a la que tenia registrada como mejor distancia conocida
        if distancia < distancias[vecino]:
          distancias[vecino] = distancia ## Actualizo mi nueva mejor distancia
          predecesores[vecino] = verticeActual ## Actualizo que la mejor distancia se dio con este predecesor
      visitados.append(verticeActual)

      distanciaMenor = float('inf')
      verticeMenor = None

      for vertice in distancias:
        if distancias[vertice] < distanciaMenor and vertice not in visitados:
          distanciaMenor = distancias[vertice]
          verticeMenor = vertice

      verticeActual = verticeMenor
    caminoMasCorto = []

    if distancias[verticeFinal] == float('inf'):
      return(float('inf'), [])

    pasoActual = verticeFinal

    while pasoActual is not None:
      caminoMasCorto.insert(0, pasoActual)
      pasoActual = predecesores[pasoActual]
    return (distancias[verticeFinal], caminoMasCorto)

  def arbolExpansionMinimo(self) -> tuple:
    if self.tamano == 0:
      return (0, []) ## Si el grafo esta vacio entonces no hay un AEM posible}

    verticesVisitados = [ self.vertices[0] ] ## Empiezo visitando el primer vertice del grafo segun su aparicion en la matriz
    conexionesArbol = [] ## Lista con todas las conexiones que hacen parte del arbol
    pesoTotal = 0 ## Acumular la longitud del AEM

    while len(verticesVisitados) < self.tamano: ## La cantidad de vertices visitados
      pesoMasBajo = float('inf')
      origenElegido = None
      destinoElegido = None

      ## Buscar todos los vecinos no visitados de los nodos del AEM
      for vertice in verticesVisitados: ## Para cada vertice en los vertices visitados
        indiceFila = self.vertices.index(vertice) ## Consultamos la fila en la cual debemos buscar los vecinos

        for indice in range(self.tamano): ## Recorremos la fila desde la posicion inicial hasta el final
          verticeEvaluado = self.vertices[indice]
          pesoEvaluado = self.matrizAdy[indiceFila][indice]

          if pesoEvaluado != 0 and verticeEvaluado not in verticesVisitados: ## Validamos que el V Evaluado sea un vecino y que ademas no haya sido visitado
            if pesoEvaluado < pesoMasBajo: ## Si el vecino evaluado es el mejor vecino hasta el momento
              pesoMasBajo = pesoEvaluado
              origenElegido = vertice
              destinoElegido = verticeEvaluado
      verticesVisitados.append(destinoElegido) ## Como en destino elegido me quedo el mejor vecino entonces lo visito
      conexionesArbol.append((origenElegido,destinoElegido, pesoMasBajo))
      pesoTotal = pesoTotal + pesoMasBajo

    return (pesoTotal, conexionesArbol)




from typing import Any, List, Dict
from collections import deque

class GrafoLista:

  def __init__(self):
    self.listaAdy : Dict[Any, List[Any]] = {}
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.listaAdy: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.listaAdy[valor] = []
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.listaAdy: ## Validamos si v1 aun no existe y en ese caso se manda crear
      self.agregarVertice(vertice1)
    if vertice2 not in self.listaAdy:## Validamos si v2 aun no existe y en ese caso se manda crear
      self.agregarVertice(vertice2)

    vecinosVertice1 = [] ## Encontrar los vecinos que ya tiene registrados el v1
    for vertice in self.listaAdy[vertice1]:
      vecinosVertice1.append(vertice[0])

    if vertice2 not in vecinosVertice1: ## Solo agrego la conexion en caso de que no exista previamente
      self.listaAdy[vertice1].append((vertice2, peso))

    if not dirigido: ## Si no es dirigido se debe crear la relacion inversa

      vecinosVertice2 = [] ## Encontar los vecinos que ya tiene registrados el v2
      for vertice in self.listaAdy[vertice2]:
        vecinosVertice2.append(vertice[0])

      if vertice1 not in vecinosVertice2: ## Solo agrego la conexion en caso de que no exista previamente
        self.listaAdy[vertice2].append((vertice1, peso))

  def recorrerEnAnchura ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.listaAdy: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    cola = deque([verticeInicial])  ## Cola de pendientes por visitar
    while cola:  ## Mientras que tenga vertices pendientes por visitar
      vertice = cola.popleft()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        for vecino, peso in self.listaAdy[vertice]:  ## Recorrer la lista ady para buscar vertices relacionados
          if vecino not in visitados: ## Si el vecino no ha sido visitado
            cola.append(vecino)  ## Agrego ese vecino a la cola de pendientes por visitar
    return visitados

  def recorrerEnProfundidad ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.listaAdy: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    pila = [verticeInicial]  ## Cola de pendientes por visitar
    while pila:  ## Mientras que tenga vertices pendientes por visitar
      vertice = pila.pop()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        for vecino, peso in reversed(self.listaAdy[vertice]):  ## Recorrer la lista ady para buscar vertices relacionados
          if vecino not in visitados: ## Si el vecino no ha sido visitado
            pila.append(vecino)  ## Agrego ese vecino a la cola de pendientes por visitar
    return visitados

    """
    ListaAdy = {
         "A": [B, C, E, F],
         "B": [A, D],
         "C": [A, E],
         "D": [B, I],
         "E": [A, C, F, G],
         "F": [A, E],
         "G": [E, H],
         "H": [G],
         "I": [D]
        }
    """

  def encontrarCaminoMasCorto(self, verticeInicial: any, verticeFinal: any) -> tuple:

    # Si el vertice inicial o final no existen en el grafo no hay un camino posible
    if verticeInicial not in self.listaAdy or verticeFinal not in self.listaAdy:
      return (float('inf'), [])

    # Guarda la mejor distancia conocida desde el vértice inicial hasta cada vértice.
    # Al comienzo todas las distancias se dejan en infinito porque todavía no se ha encontrado ningún camino hacia esos vértices.
    distancias = {vertice: float('inf') for vertice in self.listaAdy}

    # La distancia desde el vértice inicial hasta sí mismo es 0.
    distancias[verticeInicial] = 0

    # Lista de vértices ya visitados.
    # Cuando un vértice entra a esta lista significa que ya se revisaron sus vecinos.
    visitados = []

    # Guarda desde qué vértice se llegó a cada vértice usando la mejor distancia.
    predecesores = {vertice: None for vertice in self.listaAdy}

    # El algoritmo comienza revisando el vértice inicial.
    verticeActual = verticeInicial

    while verticeActual is not None and verticeActual != verticeFinal:


      for vecino, peso in self.listaAdy[verticeActual]:

        # Solo se consideran vecinos que todavía no han sido visitados.
        if vecino not in visitados:

          # distancia mínima conocida hasta verticeActual + peso de la conexión desde verticeActual hasta el vecino.
          distancia = distancias[verticeActual] + peso

          # Si la distancia es menor que la distancia guardada para el vecino, se actualiza porque se encontró una ruta más corta.
          if distancia < distancias[vecino]:
            distancias[vecino] = distancia

            # Se registra que la mejor forma conocida de llegar al vecino es pasando primero por verticeActual.
            predecesores[vecino] = verticeActual

      # Después de revisar todas las conexiones del vértice actual, se marca como visitado para no procesarlo de nuevo.
      visitados.append(verticeActual)

      # Se busca el siguiente vértice no visitado con la menor distancia acumulada.

      distanciaMenor = float('inf')
      verticeMenor = None

      for vertice in distancias:
        # El nuevo vértice actual debe ser no visitado y tener la menor distancia conocida hasta el momento.
        if distancias[vertice] < distanciaMenor and vertice not in visitados:
          distanciaMenor = distancias[vertice]
          verticeMenor = vertice

      # Se actualiza el vértice actual con el mejor candidato encontrado.
      verticeActual = verticeMenor

    # Se reconstruye el camino con ayuda de los predecesores.
    camino = []

    # Si la distancia al destino sigue siendo infinita, no existe camino posible.
    if distancias[verticeFinal] == float('inf'):
      return (float('inf'), [])

    # Se empieza desde el vértice final y se va retrocediendo hasta el inicial.
    pasoActual = verticeFinal

    while pasoActual is not None:
      # Se inserta al comienzo para que el resultado quede ordenado desde el origen hasta el destino, sin necesidad de invertir la lista al final.
      camino.insert(0, pasoActual)

      # Se avanza hacia atrás en la ruta usando el predecesor guardado.
      pasoActual = predecesores[pasoActual]

    return (distancias[verticeFinal], camino)



from typing import Any, List, Dict, Tuple
from collections import deque
import heapq


class AristaCampus:
    def __init__(self, destino: Any, distancia: int, tiempo: int, 
                 congestion: int, accesible: bool, estado: str = "disponible"):
        self.destino = destino
        self.distancia = distancia
        self.tiempo = tiempo
        self.congestion = congestion
        self.accesible = accesible
        self.estado = estado


class GrafoCampus(GrafoLista):

    def __init__(self):
        super().__init__()
        self.aristas_detalle: Dict[Any, List[AristaCampus]] = {}

    def agregarConexion(self, origen: Any, destino: Any, distancia: int, tiempo: int,
                       congestion: int, accesible: bool, estado: str = "disponible"):
        
        super().agregarConexion(origen, destino, dirigido=False, peso=distancia)
        
        if origen not in self.aristas_detalle:
            self.aristas_detalle[origen] = []
        if destino not in self.aristas_detalle:
            self.aristas_detalle[destino] = []

        self.aristas_detalle[origen].append(
            AristaCampus(destino, distancia, tiempo, congestion, accesible, estado)
        )
        self.aristas_detalle[destino].append(
            AristaCampus(origen, distancia, tiempo, congestion, accesible, estado)
        )

    def dijkstra(self, origen: Any, destino: Any, criterio: str = "distancia") -> tuple:
        if origen not in self.listaAdy or destino not in self.listaAdy:
            return float('inf'), [], "Origen o destino no existen"

        if criterio == "distancia":
            attr = 'distancia'
            unidad = "metros"
        elif criterio == "tiempo":
            attr = 'tiempo'
            unidad = "minutos"
        elif criterio == "congestion":
            attr = 'congestion'
            unidad = "nivel"
        elif criterio == "accesible":
            attr = None
            unidad = "accesibilidad"
        else:
            return float('inf'), [], "Criterio invalido"

        distancias = {v: float('inf') for v in self.listaAdy}
        predecesores = {v: None for v in self.listaAdy}
        distancias[origen] = 0

        pq = [(0, origen)]

        while pq:
            dist_actual, u = heapq.heappop(pq)

            if dist_actual > distancias[u]:
                continue

            for arista in self.aristas_detalle.get(u, []):
                if arista.estado != "disponible":
                    continue
                if criterio == "accesible" and not arista.accesible:
                    continue

                peso = 0 if criterio == "accesible" else getattr(arista, attr)
                nueva_dist = dist_actual + peso

                if nueva_dist < distancias[arista.destino]:
                    distancias[arista.destino] = nueva_dist
                    predecesores[arista.destino] = u
                    heapq.heappush(pq, (nueva_dist, arista.destino))

        if distancias[destino] == float('inf'):
            return float('inf'), [], "No hay ruta disponible"

        
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = predecesores[actual]
        camino.reverse()

        explicacion = self._generar_explicacion(camino, criterio, distancias[destino], unidad)
        return distancias[destino], camino, explicacion

    def _generar_explicacion(self, camino: List[Any], criterio: str, costo: float, unidad: str) -> str:
        if criterio == "distancia":
            return f"Ruta mas corta seleccionada por distancia total ({costo:.0f} {unidad})."
        elif criterio == "tiempo":
            return f"Ruta mas rapida seleccionada por tiempo estimado ({costo:.0f} {unidad})."
        elif criterio == "congestion":
            return f"Ruta con menor congestion seleccionada (costo acumulado: {costo:.1f})."
        else:
            return f"Ruta 100% accesible para movilidad reducida."

    
    def arbolExpansionMinimo(self) -> tuple:
        return super().arbolExpansionMinimo()



def crear_campus_udem() -> GrafoCampus:
    g = GrafoCampus()

    lugares = [
        "EntradaPrincipal", "Biblioteca", "Cafeteria", "BloqueA", "BloqueB", "BloqueC",
        "Laboratorio1", "Laboratorio2", "Auditorio", "Enfermeria", "Parqueadero1",
        "Parqueadero2", "ZonaDeportiva", "Teatro", "OficinasAdmin", "Capilla", "Banco"
    ]

    for lugar in lugares:
        g.agregarVertice(lugar)

    conexiones = [
        ("EntradaPrincipal", "Biblioteca", 120, 5, 3, True),
        ("EntradaPrincipal", "BloqueA", 80, 3, 4, True),
        ("EntradaPrincipal", "Parqueadero1", 50, 2, 2, True),
        ("Biblioteca", "Cafeteria", 60, 2, 5, True),
        ("Biblioteca", "BloqueB", 90, 4, 3, True),
        ("Cafeteria", "BloqueA", 70, 3, 6, True),
        ("BloqueA", "Laboratorio1", 40, 2, 2, True),
        ("BloqueA", "Auditorio", 85, 4, 4, True),
        ("BloqueB", "Laboratorio2", 55, 3, 3, False),
        ("BloqueB", "BloqueC", 65, 3, 4, True),
        ("BloqueC", "OficinasAdmin", 45, 2, 2, True),
        ("Laboratorio1", "Laboratorio2", 120, 6, 2, False),
        ("Auditorio", "Teatro", 100, 5, 3, True),
        ("Enfermeria", "BloqueC", 75, 4, 2, True),
        ("Parqueadero1", "Parqueadero2", 90, 4, 5, True),
        ("Parqueadero2", "ZonaDeportiva", 110, 5, 3, True),
        ("ZonaDeportiva", "Teatro", 80, 4, 4, True),
        ("OficinasAdmin", "Banco", 30, 1, 1, True),
        ("Capilla", "Biblioteca", 95, 4, 2, True),
        ("Banco", "EntradaPrincipal", 140, 6, 4, True),
    ]

    for o, d, dist, t, cong, acc in conexiones:
        g.agregarConexion(o, d, dist, t, cong, acc, "disponible")

  
    for arista in g.aristas_detalle.get("BloqueB", []):
        if arista.destino == "Laboratorio2":
            arista.estado = "bloqueado"

    return g



if __name__ == "__main__":
    grafo = crear_campus_udem()
    
    print("SISTEMA DE OPTIMIZACION DE RUTAS - UdeM")
    print("=" * 60)

    while True:
        print("\nOpciones:")
        print("1. Ruta mas corta (distancia)")
        print("2. Ruta mas rapida (tiempo)")
        print("3. Ruta con menor congestion")
        print("4. Ruta accesible (movilidad reducida)")
        print("5. Recorrido completo (Arbol de Expansion Minima)")
        print("6. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "6":
            print("Hasta pronto!")
            break

        if opcion in ["1","2","3","4"]:
            origen = input("Ingrese origen: ")
            destino = input("Ingrese destino: ")
            
            criterios = {"1":"distancia", "2":"tiempo", "3":"congestion", "4":"accesible"}
            resultado = grafo.dijkstra(origen, destino, criterios[opcion])
            costo, ruta, explicacion = resultado

            if ruta:
                print("\nRuta encontrada:")
                print(" -> ".join(ruta))
                print(f"Costo total: {costo}")
                print(explicacion)
            else:
                print("No se encontro ruta disponible.")

        elif opcion == "5":
            peso, conexiones = grafo.arbolExpansionMinimo()
            print(f"\nArbol de Expansion Minima (Distancia total: {peso} metros)")
            print("Conexiones del recorrido:")
            for u, v, p in conexiones:
                print(f"{u} -- {v} ({p}m)")

