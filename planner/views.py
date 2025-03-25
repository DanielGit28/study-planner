from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .ml_predictor import MLPredictor
from .gpt_generator import generate_gpt_plan
import asyncio
import json

@method_decorator(csrf_exempt, name='dispatch')
class GenerateStudyPlanView(APIView):
    def post(self, request):
        tasks = request.data.get('tasks')
        if not tasks:
            return Response({"error": "Tasks are required"}, status=400)

        ml = MLPredictor()

        async def process_task(task):
            urgency = task.get('urgency', 3)
            days_left = task.get('days_left', 7)
            task_type = task.get('task_type', 0)
            mode = ml.predict_mode(urgency, days_left, task_type)
            gpt_response = await asyncio.to_thread(
                generate_gpt_plan,
                task.get('name', 'Tarea'),
                mode,
                task.get('deadline', '2025-05-01'),
                urgency
            )
            try:
                gpt_json = json.loads(gpt_response)
            except Exception:
                gpt_json = {"raw_response": gpt_response}

            return {
                "task": task.get('name', 'Tarea'),
                "mode": mode,
                "gpt_plan": gpt_json
            }

        async def run_tasks():
            return await asyncio.gather(*(process_task(task) for task in tasks))

        full_plan = asyncio.run(run_tasks())
        return Response({"study_plan": full_plan})
