# eb2024_desafio_integrador_2
Ecom Python Bootcamp 20204 - Desafío Integrador 2

# Money Share

**Money Share** es una plataforma diseñada para gestionar cuentas y transacciones financieras entre usuarios. Este sistema ofrece herramientas para realizar transferencias, administrar saldos, visualizar comprobantes y mantener un historial de movimientos. Además, incluye funcionalidades avanzadas para usuarios administradores.

## Integrantes del equipo
Andrea, Matias Galo <br>
Sosa Lopez, Facundo Samuel

## Requisitos Previos

Herramientas necesarias para instalar y ejecutar el proyecto:
- **Python 3.9+**
- **Django 4.2+**
- **Mysql 7+**
- **Git**

## Instalación

### 1. Clonar el repositorio
git clone https://github.com/facundososalopez/eb2024_desafio_integrador_2
### 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
### 3. Instalar dependencias
pip install -r requirements/base.txt
### 4. Configurar variables de entorno creando un archivo .env (ejemplo)
  # ENVIRONMENT
  SECRET_KEY=django-insecure-abc123456
  DJANGO_DEBUG=True
  ENVIRONMENT_RUN=development
  DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
  # DB (MYSQL)
  DB_NAME=moneyshare_db
  DB_USER=admin
  DB_PASSWORD=supersecurepassword
  DB_HOST=127.0.0.1
  DB_PORT=3306
  # EMAIL (SMTP)
  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_HOST_USER=tuemail
  EMAIL_HOST_PASSWORD=password
  EMAIL_USE_TLS=True
  EMAIL_FROM=tuemail@gmail.com
### 5. Migrar la base de datos
python manage.py makemigrations
python manage.py migrate
### 6. Ejecutar el servidor
python manage.py runserver
### 7.Acceso al sistema
http://127.0.0.1:8000

### Funcionalidades

### 🚀 **Funcionalidades**

#### 🧑‍💻 **Funcionalidades para Usuarios Regulares**

1. **💵 Gestión de Saldo:**
   - Consulta en tiempo real el saldo disponible en tu cuenta para mantener tus finanzas organizadas.

2. **🔄 Transferencias:**
   - Envía dinero a otros usuarios dentro del sistema de forma rápida y segura.
   - Accede a los detalles completos de cada operación realizada.

3. **📥 Ingreso de Dinero:**
   - Agrega fondos a tu cuenta utilizando los métodos habilitados por la plataforma.

4. **📜 Historial de Transacciones:**
   - Visualiza todas las operaciones realizadas con filtros avanzados.

5. **📑 Comprobantes:**
   - Genera comprobantes descargables e imprimibles de cada transacción para mayor transparencia.

6. **⭐ Usuarios Favoritos:**
   - Accede fácilmente a un listado de los usuarios con quienes realizaste más transacciones.

7. **🔒 Gestión de Cuenta:**
   - Recupera tu contraseña en caso de olvido.
   - Regístrate y personaliza tu perfil dentro del sistema.
   - Agrega tu propio avatar.

#### 🛠️ **Funcionalidades para Administradores**

1. **📋 Gestión de Cuentas:**
   - Supervisa, edita y administra las cuentas de todos los usuarios registrados.

2. **⚙️ Configuración de Transferencias:**
   - Carga y gestiona los diferentes tipos de transferencias disponibles en la plataforma.

3. **🌐 Historial Global:**
   - Visualiza y analiza el historial de transacciones de todos los usuarios del sistema.


#### 🔐 **Seguridad y Accesibilidad**

- **Autenticación Segura:** Protege las cuentas de los usuarios mediante sistemas de inicio de sesión robustos.
- **Roles de Usuario:** Define accesos y privilegios según el tipo de cuenta (usuario regular o administrador).
- **Compatibilidad Multi-dispositivo:** Diseñado para funcionar de manera óptima en computadoras, tablets y smartphones.
 
