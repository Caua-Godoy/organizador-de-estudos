import json
import os
import pytest
from src.app import add_task, list_tasks, complete_task, remove_task, load_tasks, save_tasks


@pytest.fixture(autouse=True)
def clean_data_file(tmp_path, monkeypatch):
    """roda antes de cada teste, usa arquivo temporario"""
    fake_file = str(tmp_path / "tasks.json")
    monkeypatch.setattr("src.app.DATA_FILE", fake_file)
    yield


# ---- testes de adicionar ----

def test_add_task_simples():
    task = add_task("estudar matematica", "matematica", "2025-07-01")
    assert task["title"] == "estudar matematica"
    assert task["subject"] == "matematica"
    assert task["done"] == False
    assert task["deadline"] == "2025-07-01"


def test_add_task_sem_deadline():
    task = add_task("ler capitulo 3", "historia")
    assert task["deadline"] is None


def test_add_task_titulo_vazio_levanta_erro():
    with pytest.raises(ValueError):
        add_task("", "matematica")


def test_add_task_materia_vazia_levanta_erro():
    with pytest.raises(ValueError):
        add_task("fazer lista", "")


def test_add_task_titulo_so_espacos():
    with pytest.raises(ValueError):
        add_task("   ", "fisica")


# ---- testes de listar ----

def test_list_tasks_vazio():
    tasks = list_tasks()
    assert tasks == []


def test_list_tasks_so_pendentes():
    add_task("tarefa 1", "bio")
    t2 = add_task("tarefa 2", "quimica")
    complete_task(t2["id"])

    pendentes = list_tasks()
    assert len(pendentes) == 1
    assert pendentes[0]["title"] == "tarefa 1"


def test_list_tasks_todas():
    add_task("tarefa 1", "bio")
    t2 = add_task("tarefa 2", "quimica")
    complete_task(t2["id"])

    todas = list_tasks(show_done=True)
    assert len(todas) == 2


# ---- testes de concluir ----

def test_complete_task():
    task = add_task("fazer prova", "ingles")
    result = complete_task(task["id"])
    assert result["done"] == True


def test_complete_task_inexistente():
    result = complete_task(9999)
    assert result is None


# ---- testes de remover ----

def test_remove_task():
    task = add_task("tarefa para deletar", "artes")
    removed = remove_task(task["id"])
    assert removed == True
    assert list_tasks(show_done=True) == []


def test_remove_task_inexistente():
    result = remove_task(9999)
    assert result == False


# ---- testes de persistencia ----

def test_tasks_persistem_entre_chamadas():
    add_task("tarefa persistente", "geo")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "tarefa persistente"


def test_ids_sequenciais():
    t1 = add_task("primeira", "mat")
    t2 = add_task("segunda", "port")
    assert t1["id"] == 1
    assert t2["id"] == 2
