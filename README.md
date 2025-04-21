
# 📚 Study Planner API - Proyecto Django

Este es el backend en Django para el **Generador Inteligente de Planes de Estudio con IA**.

## 🚀 Instalación y ejecución

### 1️⃣ Clona o descarga el proyecto
```
unzip study_planner.zip o git clone --
cd study_planner
```

### 2️⃣ Crea y activa un entorno virtual (opcional pero recomendado)
```
python -m venv env
source env/bin/activate      # En Mac/Linux
env\Scripts\activate       # En Windows
```

### 3️⃣ Instala las dependencias
```
pip install -r requirements.txt
```

### 4️⃣ Revisa el archivo `study_planner/settings.py`
Verifica que `INSTALLED_APPS` tenga:
```
'rest_framework',
'planner',
```
Y que la base de datos sea SQLite (ya viene configurado).

### 5️⃣ Ejecuta migraciones (aunque no uses base de datos aún)
```
python manage.py migrate
```

### 6️⃣ Levanta el servidor local
```
python manage.py runserver
```

## 🔎 Cómo probar el API
Haz un POST a:
```
http://localhost:8000/api/generate-plan/
```

### 📥 Ejemplo de JSON (Body):
```
{
  "tasks": [
    {"name": "Proyecto IA", "deadline": "2025-04-10", "urgency": 5},
    {"name": "Examen Mate", "deadline": "2025-04-15", "urgency": 3},
    {"name": "Ensayo Historia", "deadline": "2025-04-05", "urgency": 4}
  ],
  "availability": {"Monday": 2, "Tuesday": 3, "Wednesday": 1},
  "habits": "early"
}
```

La respuesta será un plan de estudio ordenado por prioridad y días restantes.

## ✅ Siguientes pasos
- Integración con Frontend
- Conexión con Google Calendar
- Mejorar el algoritmo de recomendación

---

### API Key

Pregunta por una OpenAI key o ingresa la tuya creando un archivo .env con el nombre de variable ``` OPENAI_API_KEY ```

Autor: **Daniel Zúñiga Rojas**
