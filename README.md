# Notificación Caso

Este proyecto, **Notificación Caso**, tiene como objetivo principal la gestión y notificación de casos dentro de una organización o sistema. Está desarrollado en el repositorio [MarcosSuntaxi/notificacion_caso](https://github.com/MarcosSuntaxi/notificacion_caso).

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoint](#endpoint)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción

Este repositorio contiene el código fuente para la administración y notificación de casos. Permite registrar, actualizar y notificar sobre diferentes eventos o incidencias que requieren atención.

## Características

- Registro y seguimiento de casos.
- Notificación automática a los responsables.
- Histórico de acciones tomadas.
- Interfaz amigable para usuarios.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/MarcosSuntaxi/notificacion_caso.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd notificacion_caso
   ```
3. Instala las dependencias necesarias (ajusta según el gestor de paquetes y lenguaje utilizado):
   ```bash
   # Ejemplo para proyectos Node.js
   npm install

   # Ejemplo para proyectos Python
   pip install -r requirements.txt
   ```

## Uso

1. Configura las variables de entorno si es necesario.
2. Ejecuta la aplicación:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Accede a la aplicación desde tu navegador o cliente según corresponda.

## Endpoint

A continuación se describe el endpoint principal del sistema de notificación de casos:

- **URL:** `/api/notificar-caso`
- **Método:** `POST`
- **Descripción:** Permite crear y notificar un nuevo caso en el sistema.
- **Cuerpo de la petición (JSON):**
  ```json
  {
    "titulo": "Título del caso",
    "descripcion": "Descripción detallada del caso",
    "responsable": "correo@ejemplo.com",
    "prioridad": "alta"
  }
  ```
- **Respuesta exitosa (JSON):**
  ```json
  {
    "mensaje": "Caso notificado exitosamente",
    "id_caso": 123
  }
  ```
- **Ejemplo de uso con `curl`:**
  ```bash
  curl -X POST http://localhost:3000/api/notificar-caso \
    -H "Content-Type: application/json" \
    -d '{
      "titulo": "Error de servidor",
      "descripcion": "El sistema se cayó a las 3pm",
      "responsable": "soporte@ejemplo.com",
      "prioridad": "alta"
    }'
  ```