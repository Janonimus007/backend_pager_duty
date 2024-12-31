# PagerDuty API Services

Este proyecto es una aplicación en Flask que interactúa con la API de PagerDuty para manejar y visualizar datos de servicios, incidentes, políticas de escalación y equipos. Incluye la funcionalidad para generar reportes en formato CSV utilizando pandas.

## Requisitos

- Python 3.8 o superior
- Flask
- pandas
- requests
- python-dotenv

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Janonimus007/backend_pager_duty.git
   cd backend

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # En Windows: venv\Scripts\activate
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
3. Crea un archivo .env basado en el ejemplo proporcionado:
   ```bash
    cp .env.example .env

## Endpoints Disponibles

### Servicios

#### GET `/services`
#### GET `/services/csv`

### Incidentes por Servicio
#### GET `/services/incidents`
#### GET `/services/incidents/csv`

### Estado de Incidentes por Servicio
#### GET `/services/incidents/status`
#### GET `/services/incidents/status/csv`

### Equipos y Servicios
#### GET `/teams/services`
#### GET `/teams/services/csv`

### Políticas de Escalamiento
#### GET `/policies/teams/services`
