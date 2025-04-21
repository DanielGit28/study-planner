import json
import re

def extract_json_from_response(text):
    # Busca el contenido dentro de ```json ... ``` o similar
    match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
    if not match:
        # Si no está en bloque markdown, intenta encontrar primer bloque JSON
        match = re.search(r'(\{.*\})', text, re.DOTALL)

    try:
        return json.loads(match.group(1)) if match else {"raw_response": text}
    except json.JSONDecodeError:
        return {"raw_response": text}
