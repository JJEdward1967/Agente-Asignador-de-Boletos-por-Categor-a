# 🎫 Agente Asignador de Boletos por Categoría

Un agente reactivo simple desarrollado en Python que asigna automáticamente boletos según la categoría ingresada. Proyecto desarrollado como parte del Sprint 3 del módulo "Creación de Agentes Inteligentes".

## 📋 Descripción

Este agente simula una tarea típica de un sistema de gestión de entradas para eventos. Recibe como entrada una categoría de boleto y asigna automáticamente una cantidad predefinida:

| Categoría | Boletos Asignados |
|-----------|-------------------|
| `standard` | 2 |
| `standard_plus` | 4 |
| `platino` | 10 |

## 🧠 Tipo de Agente

Según la teoría de agentes inteligentes, este es un **agente reactivo simple**:
- Opera con reglas del tipo "si condición → entonces acción"
- No planifica a largo plazo ni optimiza metas complejas
- Responde directamente a cada entrada según la categoría recibida

## 🔄 Flujo de Funcionamiento

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ PERCEPCIÓN  │ ──► │  DECISIÓN   │ ──► │   ACCIÓN    │
│  (input)    │     │ (condicional)│     │  (output)   │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       └───────────────────────────────────────┘
                    (bucle while)
```

1. **Percepción**: El agente recibe la categoría del boleto mediante `input()`
2. **Decisión**: Evalúa la categoría con condicionales `if/elif/else`
3. **Acción**: Imprime los boletos asignados usando un bucle `for`
4. **Repetición**: El ciclo continúa hasta que el usuario escribe `salir`

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- **Visual Studio Code** con extensión de Python
- **GitHub Copilot** para generación asistida de código
- **ChatGPT 5.1** para diseño conceptual y planificación
- **Claude

## 🚀 Instalación y Uso

### Requisitos
- Python 3.6 o superior

### Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/agente-boletos.git

# Navegar al directorio
cd agente-boletos

# Ejecutar el agente
python agente_boletos.py
```

### Ejemplo de Uso

```
Agente asignador de boletos. Escribe 'salir' para terminar.

Ingrese la categoría (standard, standard_plus, platino): platino
Boleto 1 - categoría platino
Boleto 2 - categoría platino
Boleto 3 - categoría platino
Boleto 4 - categoría platino
Boleto 5 - categoría platino
Boleto 6 - categoría platino
Boleto 7 - categoría platino
Boleto 8 - categoría platino
Boleto 9 - categoría platino
Boleto 10 - categoría platino
Total de boletos generados para la categoría 'platino': 10

Ingrese la categoría (standard, standard_plus, platino): salir
Saliendo del programa. ¡Hasta luego!
```

## 📁 Estructura del Proyecto

```
agente-boletos/
├── agente_boletos.py    # Código principal del agente
├── README.md            # Este archivo
└── screenshot.png       # Captura de pantalla de ejecución
```

## 🔮 Mejoras Futuras

- Integración con módulo OCR para leer categorías desde boletos físicos
- Inclusión de correlativo único para cada boleto
- Persistencia del historial en base de datos
- Exposición como API REST o interfaz web

## 📚 Conceptos de Programación Aplicados

Este proyecto refuerza los siguientes fundamentos:

- **Variables**: Almacenamiento de datos de entrada y resultados
- **Condicionales**: Lógica de decisión con `if/elif/else`
- **Bucles**: `while` para interacción continua, `for` para iteración
- **Funciones**: Modularización del código en unidades reutilizables

## 🎓 Contexto Académico

Desarrollado como parte del Sprint 3 del posgrado en Hiperautomatización con IA y herramientas No-Code (IEBS), aplicando el paradigma de **Vibe Coding** (programación asistida por IA).

## 👤 Autor

**Jaime Blanco**
