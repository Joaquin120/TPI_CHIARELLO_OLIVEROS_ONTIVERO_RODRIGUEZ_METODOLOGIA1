# Sistema de Gestión de Turnos Odontológicos

Este repositorio contiene la lógica de dominio para la gestión de turnos odontológicos, resolviendo la doble restricción física de disponibilidad simultánea de profesionales y sillones/boxes. El proyecto fue especificado y construido bajo la metodología **Spec-Driven Development (SDD)** con **Active Stack**.

---

## Requisitos Previos

* Python 3.11 o superior.
* Git.

---

## Instalación y Ejecución de Tests

Para clonar el repositorio y ejecutar la suite de pruebas desde cero, seguí estos pasos exactos en tu terminal:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Joaquin120/TPI_CHIARELLO_OLIVEROS_ONTIVERO_RODRIGUEZ_METODOLOGIA1.git](https://github.com/Joaquin120/TPI_CHIARELLO_OLIVEROS_ONTIVERO_RODRIGUEZ_METODOLOGIA1.git)
cd TPI_CHIARELLO_OLIVEROS_ONTIVERO_RODRIGUEZ_METODOLOGIA1/turnos-odontologia
```

### 2. Crear y activar el entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la suite de pruebas
```bash
pytest -v
```

> **Nota:** Todos los 8 tests unitarios deben pasar en verde, validando el camino feliz, las excepciones de solapamiento por profesional y sillón, y los turnos contiguos bajo intervalos semiabiertos $[inicio, fin)$.

---

## Estructura del Repositorio

* `openspec/`: Estructura metodológica de OpenSpec con especificaciones vigentes (`specs/`) y cambios archivados (`changes/archive/`).
* `src/domain/`: Lógica de dominio puro en Python (modelos, servicios de validación y excepciones de negocio).
* `tests/`: Suite de pruebas unitarias automatizadas con `pytest`.
* `pytest.ini`: Configuración de resolución de módulos para ejecución directa.
* `requirements.txt`: Dependencias del entorno de testing (`pytest`, `pytest-cov`).

---

## Integrantes del Equipo

* Joaquín Chiarello
* Santiago Ontivero
* Cristian Rodríguez
* Joseph Oliveros
