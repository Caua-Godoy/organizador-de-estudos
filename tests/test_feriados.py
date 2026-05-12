from unittest.mock import MagicMock, patch

from src.feriados import buscar_feriados, eh_feriado


# --- teste de integracao real (chama a API de verdade) ---


def test_buscar_feriados_retorna_lista():
    feriados = buscar_feriados(2025)
    assert isinstance(feriados, list)
    assert len(feriados) > 0
    assert "date" in feriados[0]
    assert "name" in feriados[0]


def test_feriados_tem_campos_esperados():
    feriados = buscar_feriados(2025)
    for f in feriados:
        assert "date" in f
        assert "name" in f
        assert "type" in f


# --- testes com mock (nao dependem de internet) ---


@patch("src.feriados.requests.get")
def test_eh_feriado_retorna_nome(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"date": "2025-01-01", "name": "Confraternizacao Universal", "type": "national"}
    ]
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    resultado = eh_feriado("2025-01-01")
    assert resultado == "Confraternizacao Universal"


@patch("src.feriados.requests.get")
def test_eh_feriado_retorna_none_se_nao_feriado(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"date": "2025-01-01", "name": "Confraternizacao Universal", "type": "national"}
    ]
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    resultado = eh_feriado("2025-06-15")
    assert resultado is None
