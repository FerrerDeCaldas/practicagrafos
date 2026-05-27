# Sistema de Optimización de Recorridos - UdeM

## Descripción del proyecto

Este proyecto consiste en un sistema inteligente de rutas dentro del campus de la Universidad de Medellín (UdeM), desarrollado como parte de la práctica de Grafos.

El sistema modela el campus universitario como un **grafo** donde cada lugar importante es un vértice y los caminos entre ellos son aristas con múltiples atributos:

- Distancia (en metros)
- Tiempo estimado de recorrido (en minutos)
- Nivel de congestión (1-10)
- Accesibilidad para personas con movilidad reducida
- Estado del camino (disponible, bloqueado, en mantenimiento)

### Funcionalidades principales:

- **Búsqueda de rutas óptimas** utilizando Dijkstra modificado con 4 criterios de optimización:
  1. Ruta más corta (por distancia)
  2. Ruta más rápida (por tiempo)
  3. Ruta con menor congestión
  4. Ruta accesible para movilidad reducida

- Ignora automáticamente caminos bloqueados o en mantenimiento.
- **Árbol de Expansión Mínima (AEM)** para generar un recorrido completo por el campus con la menor distancia posible.
- Reconstrucción clara de la ruta y explicación del criterio utilizado.

El grafo contiene **17 lugares** representativos del campus.

---

## Cómo ejecutar el proyecto

### Requisitos
- Python 3.8 o superior

### Pasos para ejecutar:

1. Clonar el repositorio:
   ```bash
   git clone <enlace-del-repositorio>
   cd <nombre-del-repositorio>