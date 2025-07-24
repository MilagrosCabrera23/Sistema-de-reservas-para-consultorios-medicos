#  Sistema de Reservas para Consultorios Médicos — Backend con FastAPI
Este proyecto es una API REST desarrollada con FastAPI para gestionar las reservas de turnos médicos entre pacientes y profesionales de la salud, con un sistema de autenticación seguro y una arquitectura modular escalable.

##  Funcionalidades Clave
###  Autenticación y Autorización
- Registro e inicio de sesión para pacientes, médicos y administradores
- Autenticación con JWT
- Control de acceso por roles (RBAC)

###  Gestión de Usuarios
- CRUD completo para pacientes y médicos
- Asignación y validación de roles
- Acceso a historial de turnos y datos personales

### Gestión de Consultorios / Especialidades (opcional)
- Gestión de especialidades médicas (Cardiología, Pediatría, etc.)
- Asociación entre médicos y especialidades

### Gestión de Servicios Médicos
- Servicios como "Consulta general", "Vacunación", etc.
- Asignación de servicios por médico

### Gestión de Horarios y Disponibilidad
- Médicos pueden configurar días y horarios de atención
-  de franjas horarias (almuerzo, vacaciones, etc.)
- Generación automática de franjas disponibles
- Validación para evitar solapamiento de turnos

### Gestión de Turnos / Reservas
Pacientes pueden:
Buscar turnos por médico, especialidad o fecha
Reservar y cancelar turnos

Médicos pueden:
Ver, confirmar o cancelar turnos asignados
Historial de turnos por usuario

### Notificaciones
- Recordatorios de turnos
- Confirmaciones y cancelaciones

##  Arquitectura del Proyecto
El proyecto sigue una estructura basada en capas desacopladas y responsabilidades claras:
```
Sistema de reservas
│
├── app/
│   ├── core/                  # Configuración y seguridad (JWT, DB)
│   ├── models/                # Modelos SQLAlchemy
│   ├── schemas/               # Esquemas Pydantic (I/O)
│   ├── crud/                  # Lógica de acceso a datos (repositorios)
│   ├── services/              # Lógica de negocio
│   ├── api/
│   │   ├── routes/            # Rutas agrupadas (usuarios, turnos, etc.)
│   │   └── deps.py            # Dependencias para inyecciones
│   ├── utils/                 # Funciones auxiliares (JWT, fechas, etc.)
│   └── tests/                 # Pruebas automatizadas
├── main.py
├── .env                       # Variables de entorno
├── requirements.txt           # Dependencias del proyecto
└── README.md
```

## Tecnologías Usadas
- FastAPI	Web framework principal
- SQLAlchemy	ORM para manejar la base de datos
- Pydantic	Validaciones y esquemas de datos
- JWT (python-jose)	Autenticación basada en tokens
- Passlib (bcrypt)	Hash seguro de contraseñas
- MySQL	Base de datos
- Python-dotenv	Manejo de variables de entorno
- Uvicorn	Servidor ASGI para FastAPI
- Pytest + httpx	Tests automatizados

## Cómo correr el proyecto

### 1.Clona el repositorio:
```
bash
git clone https://github.com/tuusuario/sistema-reservas-medicas.git
cd sistema-reservas-medicas
```
### 2.Crea un entorno virtual e instálalo:
```
bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3.Crea un archivo .env:
```
env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### 4.Ejecuta la aplicación:
```
bash
uvicorn main:app --reload
```
## Abre la documentación en tu navegador:

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

## Futuras mejoras (para escalar o en versión Pro)
- Panel Admin (usando FastAPI-Admin o integrar un Frontend con React/Angular)
- Soporte para múltiples consultorios físicos
- Soporte para carga de historia clínica digital




