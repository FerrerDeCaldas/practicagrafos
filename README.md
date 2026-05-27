# Sistema de Optimización de Recorridos - Universidad de Medellín (UdeM)

## Descripción del proyecto

Este proyecto consiste en un sistema que modela el campus de la Universidad de Medellín como un **grafo**, permitiendo encontrar rutas óptimas entre diferentes lugares según diversos criterios. 

Cada lugar es un **vértice** y los caminos entre ellos son **aristas** con múltiples atributos:
- Distancia (metros)
- Tiempo estimado (minutos)
- Nivel de congestión (1-10)
- Accesibilidad para personas con movilidad reducida
- Estado del camino (disponible, bloqueado o en mantenimiento)

El sistema cumple con todos los requerimientos de la práctica: Dijkstra modificado con múltiples criterios, ignorar caminos bloqueados, Árbol de Expansión Mínima, entre otros.

---

## Cómo funciona el código

### Estructura principal:

- **`AristaCampus`**: Clase que almacena toda la información detallada de cada camino.
- **`GrafoCampus`**: Hereda de la clase base `GrafoLista` proporcionada en clase. Sobrescribe `agregarConexion()` para soportar múltiples atributos por arista.
- **Dijkstra Modificado**: Implementación personalizada que permite optimizar según 4 criterios diferentes.
- **Árbol de Expansión Mínima**: Reutiliza el método original de la clase base.

### Menú Principal y Funcionalidades

Al ejecutar el programa, aparece el siguiente menú:

1. **Ruta más corta (distancia)**  
   Calcula la ruta con la menor distancia total en metros.

2. **Ruta más rápida (tiempo)**  
   Calcula la ruta con el menor tiempo estimado de recorrido (en minutos).

3. **Ruta con menor congestión**  
   Calcula la ruta que acumula el menor nivel de congestión.

4. **Ruta accesible (movilidad reducida)**  
   Calcula una ruta que solo utiliza caminos accesibles para personas con movilidad reducida. Ignora automáticamente los caminos no accesibles.

5. **Recorrido completo (Árbol de Expansión Mínima)**  
   Muestra un recorrido que visita todos los lugares del campus sin repetir ninguno, utilizando la menor distancia total posible (ideal para visitantes).

6. **Salir**  
   Termina la ejecución del programa.

**Características generales del sistema:**
- Ignora automáticamente caminos en estado "bloqueado" o "en mantenimiento".
- Reconstruye y muestra la ruta completa (origen → ... → destino).
- Muestra el costo total según el criterio seleccionado.
- Proporciona una breve explicación de por qué se seleccionó esa ruta.
- El grafo contiene **17 lugares** representativos del campus.

---

## Cómo ejecutar el proyecto

### Requisitos
- Python 3.8 o superior

### Pasos para ejecutar:

1. Clonar o descargar el repositorio.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar el programa con:

   ```bash
   python grafo_udem.py