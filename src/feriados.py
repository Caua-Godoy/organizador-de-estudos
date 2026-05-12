import requests
from datetime import date

BRASILAPI_URL = "https://brasilapi.com.br/api/feriados/v1/{ano}"


def buscar_feriados(ano: int = None) -> list:
    if ano is None:
        ano = date.today().year
    url = BRASILAPI_URL.format(ano=ano)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def eh_feriado(data_str: str):
    try:
        ano = int(data_str[:4])
        feriados = buscar_feriados(ano)
        for f in feriados:
            if f["date"] == data_str:
                return f["name"]
    except Exception:
        pass
    return None


def listar_feriados_cli():
    ano = date.today().year
    print(f"\n📅 feriados nacionais de {ano}:\n")
    try:
        feriados = buscar_feriados(ano)
        for f in feriados:
            print(f"  {f['date']} — {f['name']}")
    except requests.exceptions.ConnectionError:
        print("  ❌ sem conexao com a internet.")
    except requests.exceptions.HTTPError as e:
        print(f"  ❌ erro ao buscar feriados: {e}")
    print()
