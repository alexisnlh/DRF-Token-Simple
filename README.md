# DRF-Token-Simple

API REST simple desarrollada con Django y Django REST Framework que implementa autenticación de usuarios mediante Tokens usando el módulo `authtoken` integrado en DRF.

> 🎓 Proyecto basado en el [tutorial de Fazt Code](https://www.youtube.com/watch?v=Gr_QsOifaro)

## 📋 Descripción

Este proyecto implementa un sistema de autenticación completo que incluye registro de usuarios, login y obtención del perfil de usuario. La particularidad es que presenta **dos implementaciones diferentes** del mismo sistema:

- **Function-Based Views (func)**: Implementación usando vistas basadas en funciones con decoradores.
- **Class-Based Views (class)**: Implementación usando vistas basadas en clases (APIView).

Ambas implementaciones demuestran cómo lograr los mismos resultados con diferentes enfoques de programación en Django REST Framework.

<a id="tabla-de-contenidos"></a>
## 📋 Tabla de Contenidos

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Endpoints](#endpoints)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Probando con cURL](#curl)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Seguridad](#seguridad)
- [Aprendizaje](#aprendizaje)
- [Licencia](#licencia)
- [Autor](#autor)
- [Agradecimientos](#agradecimientos)

<a id="características"></a>
## ✨ Características

- ✅ Registro de usuarios
- ✅ Autenticación mediante login
- ✅ Generación automática de tokens al registrarse
- ✅ Protección de endpoints con autenticación por token
- ✅ Consulta de perfil de usuario autenticado
- ✅ Dos estilos de implementación (funciones vs clases)
- ✅ Código ampliamente comentado para facilitar el aprendizaje
- ✅ Base de datos SQLite incluida

<a id="tecnologías"></a>
## 🛠️ Tecnologías

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **SQLite**
- **Token Authentication (DRF authtoken)**

<a id="instalación"></a>
## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/alexisnlh/DRF-Token-Simple.git
cd drf-token-simple
```

### 2. Crear entorno virtual

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django djangorestframework
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`

**[⬆ back to top](#tabla-de-contenidos)**

<a id="endpoints"></a>
## 🔌 Endpoints

### Aplicación `func` (Function-Based Views)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/func/register` | Registro de usuarios | No requerida |
| POST | `/func/login` | Login y obtención de token | No requerida |
| GET | `/func/profile` | Perfil del usuario autenticado | Token requerido |

### Aplicación `class` (Class-Based Views)

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/class/register` | Registro de usuarios | No requerida |
| POST | `/class/login` | Login y obtención de token | No requerida |
| GET | `/class/profile` | Perfil del usuario autenticado | Token requerido |

**[⬆ back to top](#tabla-de-contenidos)**

<a id="ejemplos-de-uso"></a>
## 📝 Ejemplos de Uso

### Registro de Usuario

```bash
POST /func/register
Content-Type: application/json

{
    "username": "usuario_ejemplo",
    "email": "usuario@example.com",
    "password": "contraseña_segura"
}
```

**Respuesta:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    "user": {
        "id": 1,
        "username": "usuario_ejemplo",
        "email": "usuario@example.com"
    }
}
```

### Login

```bash
POST /func/login
Content-Type: application/json

{
    "username": "usuario_ejemplo",
    "password": "contraseña_segura"
}
```

**Respuesta:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    "user": {
        "id": 1,
        "username": "usuario_ejemplo",
        "email": "usuario@example.com"
    }
}
```

### Obtener Perfil (Requiere Token)

```bash
GET /func/profile
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Respuesta:**
```json
{
    "id": 1,
    "username": "usuario_ejemplo",
    "email": "usuario@example.com"
}
```

**[⬆ back to top](#tabla-de-contenidos)**

<a id="curl"></a>
## 🧪 Probando con cURL

### Registro
```bash
curl -X POST http://127.0.0.1:8000/func/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"test1234"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/func/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"test1234"}'
```

### Profile
```bash
curl -X GET http://127.0.0.1:8000/func/profile \
  -H "Authorization: Token TU_TOKEN_AQUI"
```

**[⬆ back to top](#tabla-de-contenidos)**

<a id="estructura-del-proyecto"></a>
## 📂 Estructura del Proyecto

```
drf-token-simple/
├── func/                   # App con Function-Based Views
│   ├── views.py           # Vistas con decoradores
│   └── urls.py
├── class/                  # App con Class-Based Views
│   ├── views.py           # Vistas con APIView
│   └── urls.py
├── server/              # Configuración principal
│   ├── settings.py
│   └── urls.py
├── db.sqlite3             # Base de datos
├── JSON_example.txt       # Ejemplos de peticiones JSON
└── manage.py
```

<a id="seguridad"></a>
## 🔐 Seguridad

- Los tokens se generan automáticamente al crear un usuario
- Las contraseñas se almacenan hasheadas en la base de datos
- Los endpoints de perfil están protegidos y requieren autenticación
- Se valida que el usuario exista antes de generar tokens

<a id="aprendizaje"></a>
## 📚 Aprendizaje

Este proyecto es ideal para:

- Aprender la diferencia entre Function-Based Views y Class-Based Views
- Entender cómo implementar autenticación por token en DRF
- Comprender el flujo de registro, login y autorización
- Ver código comentado y documentado para facilitar el aprendizaje

<a id="licencia"></a>
## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

<a id="autor"></a>
## 👤 Autor

**Alexis NLH**

- GitHub: [@alexisnlh](https://github.com/alexisnlh)

<a id="agradecimientos"></a>
## 🙏 Agradecimientos

- [Fazt Code](https://www.youtube.com/c/FaztCode) por el tutorial original
- Comunidad de Django REST Framework

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub

**[⬆ back to top](#tabla-de-contenidos)**
