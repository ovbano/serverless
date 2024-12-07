import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

# URL base de tu API
BASE_URL = "https://7d0a1tv1e0.execute-api.us-east-1.amazonaws.com/tasks"

# Obtener todas las tareas
def task_list(request):
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()  # Obtener la respuesta JSON completa
        tasks = data.get("body", {}).get("tasks", [])  # Extraer las tareas
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las tareas: {e}")
        tasks = []
    return render(request, "task_list.html", {"tasks": tasks})



# Agregar una nueva tarea
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        try:
            response = requests.post(BASE_URL, json={"title": title, "description": description})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error al agregar la tarea: {e}")
        return redirect("task_list")
    return render(request, "add_task.html")

# Actualizar una tarea
def update_task(request, id):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        done = request.POST.get("done") == "on"  # Checkbox
        try:
            response = requests.put(f"{BASE_URL}/{id}", json={"title": title, "description": description, "done": done})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error al actualizar la tarea: {e}")
        return redirect("task_list")
    return render(request, "update_task.html", {"id": id})

# Eliminar una tarea
def delete_task(request, id):
    try:
        response = requests.delete(f"{BASE_URL}/{id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al eliminar la tarea: {e}")
    return redirect("task_list")
