import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, subject, deadline=None):
    if not title or not title.strip():
        raise ValueError("titulo nao pode ser vazio")
    if not subject or not subject.strip():
        raise ValueError("materia nao pode ser vazia")

    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "subject": subject.strip(),
        "deadline": deadline,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks(show_done=False):
    tasks = load_tasks()
    if not show_done:
        tasks = [t for t in tasks if not t["done"]]
    return tasks


def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return task
    return None


def remove_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return False
    save_tasks(new_tasks)
    return True


def print_tasks(tasks):
    if not tasks:
        print("  nenhuma tarefa encontrada.")
        return
    for t in tasks:
        status = "[x]" if t["done"] else "[ ]"
        deadline_str = f" | prazo: {t['deadline']}" if t.get("deadline") else ""
        print(f"  {status} #{t['id']} - {t['title']} ({t['subject']}){deadline_str}")


def main():
    print("=== organizador de tarefas de estudo ===")
    print("comandos: add, list, done, remove, all, sair")

    while True:
        cmd = input("\n> ").strip().lower()

        if cmd == "sair":
            print("ate mais!")
            break

        elif cmd == "add":
            title = input("titulo da tarefa: ").strip()
            subject = input("materia: ").strip()
            deadline = input("prazo (opcional, ex: 2025-06-30): ").strip() or None
            try:
                task = add_task(title, subject, deadline)
                print(f"tarefa #{task['id']} adicionada!")
            except ValueError as e:
                print(f"erro: {e}")

        elif cmd == "list":
            tasks = list_tasks()
            print("\ntarefas pendentes:")
            print_tasks(tasks)

        elif cmd == "all":
            tasks = list_tasks(show_done=True)
            print("\ntodas as tarefas:")
            print_tasks(tasks)

        elif cmd == "done":
            try:
                task_id = int(input("id da tarefa concluida: "))
                task = complete_task(task_id)
                if task:
                    print(f"tarefa '{task['title']}' marcada como concluida!")
                else:
                    print("tarefa nao encontrada.")
            except ValueError:
                print("id invalido.")

        elif cmd == "remove":
            try:
                task_id = int(input("id da tarefa para remover: "))
                if remove_task(task_id):
                    print("tarefa removida.")
                else:
                    print("tarefa nao encontrada.")
            except ValueError:
                print("id invalido.")

        else:
            print("comando nao reconhecido.")


if __name__ == "__main__":
    main()
