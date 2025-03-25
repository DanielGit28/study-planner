import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_gpt_plan(task_name, mode, deadline, urgency):
    prompt = f"""
Eres un experto en educación. Dame un plan de estudio para esta tarea:
Tarea: {task_name}
Modo de estudio recomendado: {mode}
Deadline: {deadline}
Urgencia: {urgency}/5

Devuélveme:
- 3 actividades variadas (ej: lectura, ejercicios, mapas mentales, escritura) o mas
- Tiempo estimado por actividad
- Recursos recomendados (videos, links, papers)
En formato JSON.
"""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return completion.choices[0].message.content
