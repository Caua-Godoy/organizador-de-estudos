# 📚 organizador de tarefas

![CI](https://github.com/Caua-Godoy/study-task-organizer/actions/workflows/ci.yml/badge.svg)

Organizador de tarefas de estudo via linha de comando (CLI). O programa ajuda estudantes a gerenciar atividades escolares/universitarias, organizando por materia e prazo, sem depender de apps externos ou internet.

---

## 🎯 Problema real

Estudantes frequentemente perdem prazos de trabalhos, provas e atividades por falta de organizacao. Cadernos e anotacoes avulsas se perdem facilmente, e muitos apps de produtividade sao complexos ou exigem cadastro. Esta ferramenta resolve isso de forma simples, rodando direto no terminal.


## ✅ Funcionalidades

- Adicionar tarefa com titulo, materia e prazo opcional
- Listar tarefas pendentes
- Listar todas as tarefas (incluindo concluidas)
- Marcar tarefa como concluida
- Remover tarefa
- Persistencia local em arquivo JSON


## 🚀 Instalacao

**1. Clone o repositorio:**
```bash
git clone https://github.com/Caua-Godoy/organizador-de-estudos.git
cd organizador-de-estudos
```

**2. (Opcional) Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate   # linux/mac
venv\Scripts\activate      # windows
```

**3. Instale as dependencias:**
```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

```bash
python -m src.app
```

### Comandos disponiveis

| Comando  | Descricao                        |
|----------|----------------------------------|
| `add`    | Adicionar nova tarefa            |
| `list`   | Listar tarefas pendentes         |
| `all`    | Listar todas (incluindo feitas)  |
| `done`   | Marcar tarefa como concluida     |
| `remove` | Remover uma tarefa               |
| `sair`   | Encerrar o programa              |

### Exemplo de uso

```
=== organizador de tarefas de estudo ===
comandos: add, list, done, remove, all, sair

> add
titulo da tarefa: estudar para prova de calculo
materia: matematica
prazo (opcional, ex: 2025-06-30): 2025-06-20
tarefa #1 adicionada!

> list

tarefas pendentes:
  [ ] #1 - estudar para prova de calculo (matematica) | prazo: 2025-06-20

> done
id da tarefa concluida: 1
tarefa 'estudar para prova de calculo' marcada como concluida!
```

---

## 🧪 Rodando os testes

```bash
pytest -v
```

Saida esperada: 14 testes passando.

---

## 🔍 Rodando o lint

```bash
ruff check src/
```

---

## 📦 Versao

`1.0.0`

---

## 👤 Autor

Caua Godoy

## 🔗 Repositorio

https://github.com/Caua-Godoy/organizador-de-estudos


### README COM AUXILIO DE IA
