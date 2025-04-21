import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_gpt_plan(task_name, mode, deadline, urgency):
    prompt = f"""
Eres un asistente que genera planes de estudio personalizados. 
Devuelve únicamente un objeto JSON (sin texto explicativo) con la siguiente estructura:

{{
  "actividades": [
    {{
      "tipo": "Lectura/Ejercicio/Practica/Examen/etc, lo que se te ocurra pero varia",
      "descripcion": "...",
      "tiempo_estimado": "...",
      "recursos": [
        {{
          "titulo": "...",
          "autor": "...",
          "link": "..."
        }}
      ]
    }},
    ...
  ]
}}

Tarea: {task_name}
Urgencia: {urgency}/5
Deadline: {deadline}
Modo de estudio: {mode}
"""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return completion.choices[0].message.content
