# Sistema de Optimización de Recorridos - Universidad de Medellín (UdeM)

## Descripción del proyecto

Este proyecto modela el campus de la Universidad de Medellín como un **grafo** para ayudar a estudiantes, docentes y visitantes a encontrar las mejores rutas entre diferentes lugares.

Cada lugar del campus es un **vértice** y los caminos son **aristas** que contienen múltiples atributos:
- Distancia en metros
- Tiempo estimado en minutos
- Nivel de congestión (1-10)
- Accesibilidad para personas con movilidad reducida
- Estado del camino (disponible, bloqueado, mantenimiento)

El sistema permite calcular rutas óptimas según diferentes criterios y generar un recorrido completo por el campus usando Árbol de Expansión Mínima.

---

## Cómo funciona el código

### Estructura principal:

1. **Clase `AristaCampus`**:
   - Almacena toda la información de cada camino (distancia, tiempo, congestión, accesibilidad y estado).

2. **Clase `GrafoCampus`** (hereda de `GrafoLista`):
   - Extiende la clase base proporcionida en clase.
   - Sobrescribe `agregarConexion()` para guardar tanto el peso (distancia) como toda la información adicional.

3. **Algoritmo Dijkstra Modificado** (`dijkstra()`):
   - Permite elegir entre 4 criterios de optimización:
     - Ruta más corta (distancia)
     - Ruta más rápida (tiempo)
     - Ruta con menor congestión
     - Ruta accesible (solo usa caminos aptos para movilidad reducida)
   - Ignora automáticamente caminos bloqueados o en mantenimiento.
   - Usa cola de prioridad (`heapq`) para mayor eficiencia.

4. **Árbol de Expansión Mínima**:
   - Reutiliza el método original de la clase base `GrafoLista`.
   - Calcula el recorrido de menor distancia que conecta todos los lugares.

5. **Menú interactivo**:
   - Permite al usuario seleccionar el tipo de ruta y los puntos de origen/destino.

---

## Cómo ejecutar el proyecto

### Requisitos
- Python 3.8 o superior

### Pasos:

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

   ```bash
   python grafo_udem.py