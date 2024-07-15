from app.api.api_grupo import obter_grupo, listar_grupo, obter_produtos_do_grupo, obter_producao_do_grupo, obter_comercializacao_do_grupo, obter_importacao_quantidade,obter_importacao_faturamento, obter_exportacao_quantidade, obter_exportacao_faturamento, obter_processamento_do_grupo
from app.models.entities import Grupo, Produto, Producao, Comercializacao, Quantidade, Faturamento, Processamento
from app.infra.database import Session

from pytest_mock import MockerFixture
import pytest

@pytest.mark.asyncio
async def test_obter_grupo(mocker: MockerFixture):

    grupo = Grupo(id=1, nome='Grupo 1')

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = grupo
    
    resultado = await obter_grupo(1, session_mock, True)

    assert resultado == grupo, 'A função obter_grupo não retornou o grupo correto'


@pytest.mark.asyncio   
async def test_obter_grupo_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = None

    with pytest.raises(Exception) as excinfo:
        await obter_grupo(1, session_mock, True)
        
    assert 'Grupo não encontrado' in str(excinfo.value), 'A função obter_grupo não retornou o erro correto'


@pytest.mark.asyncio
async def test_listar_grupo(mocker: MockerFixture):
    grupos = [Grupo(id=1, nome='Grupo 1'), Grupo(id=2, nome='Grupo 2')]

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .all.return_value = grupos

    resultado = await listar_grupo(session_mock, True)
        
    assert resultado == grupos, 'A função listar_grupo não retornou a lista de grupos correta'


@pytest.mark.asyncio
async def test_obter_produtos_do_grupo(mocker: MockerFixture):
    grupo = Grupo(id=1, nome='Grupo 1', produtos=[])
    grupo.produtos.extend([
        Produto(id=1, nome='Produto 1', grupo_id=1),
        Produto(id=2, nome='Produto 2', grupo_id=1)
    ])

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = grupo
    
    resultado = await obter_produtos_do_grupo(1, session_mock, True)

    assert resultado == grupo.produtos, 'A função obter_produtos_do_grupo não retornou os produtos corretos'


@pytest.mark.asyncio
async def test_obter_produtos_do_grupo_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = None

    with pytest.raises(Exception) as excinfo:
        await obter_produtos_do_grupo(1, session_mock, True)
        
    assert 'Grupo não encontrada' in str(excinfo.value), 'A função obter_produtos_do_grupo não retornou o erro correto'


@pytest.mark.asyncio
async def test_obter_producao_do_grupo(mocker: MockerFixture):
    grupo = Grupo(id=1, nome='Grupo 1', producao=[])
    grupo.producao.extend([
        Producao(id=1, grupo_id=1, quantidade=10),
        Producao(id=2, grupo_id=1, quantidade=20)
    ])

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = grupo
    
    resultado = await obter_producao_do_grupo(1, session_mock, True)

    assert resultado == grupo.producao, 'A função obter_producao_do_grupo não retornou a produção correta'


@pytest.mark.asyncio
async def test_obter_producao_do_grupo_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = None

    with pytest.raises(Exception) as excinfo:
        await obter_producao_do_grupo(1, session_mock, True)
        
    assert 'Grupo não encontrada' in str(excinfo.value), 'A função obter_producao_do_grupo não retornou o erro correto'

#==============================================================================
# COMERCIALIZAÇÃO	
#==============================================================================

@pytest.mark.asyncio
async def test_obter_comercializacao_do_grupo(mocker: MockerFixture):
    grupo = Grupo(id=1, nome='Grupo 1', comercializacao=[])
    grupo.comercializacao.extend([
        Comercializacao(id=1, grupo_id=1, quantidade=10),
        Comercializacao(id=2, grupo_id=1, quantidade=20)
    ])

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = grupo
    
    resultado = await obter_comercializacao_do_grupo(1, session_mock, True)

    assert resultado == grupo.comercializacao, 'A função obter_comercializacao_do_grupo não retornou a comercialização correta'


@pytest.mark.asyncio
async def test_obter_comercializacao_do_grupo_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = None

    with pytest.raises(Exception) as excinfo:
        await obter_comercializacao_do_grupo(1, session_mock, True)
        
    assert 'Grupo não encontrado' in str(excinfo.value), 'A função obter_comercializacao_do_grupo não retornou o erro correto'

#==============================================================================
# IMPORTAÇÃO	
#==============================================================================

@pytest.mark.asyncio
async def test_obter_importacao_quantidade(mocker: MockerFixture):
    lista_quantidade = [
        Quantidade(id=1, grupo_id=1, quantidade=10),
        Quantidade(id=2, grupo_id=1, quantidade=20)
    ]

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = lista_quantidade
    
    resultado = await obter_importacao_quantidade(1, session_mock, True)

    assert resultado == lista_quantidade, 'A função obter_importacao_quantidade não retornou a comercialização correta'

@pytest.mark.asyncio
async def test_obter_importacao_quantidade_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = []

    with pytest.raises(Exception) as excinfo:
        await obter_importacao_quantidade(1, session_mock, True)
        
    assert 'Quantidade de importação por grupo não encontrada' in str(excinfo.value), 'A função obter_importacao_quantidade não retornou o erro correto'

@pytest.mark.asyncio
async def test_obter_importacao_faturamento(mocker: MockerFixture):
    lista_faturamento = [
        Faturamento(id=1, grupo_id=1, faturamento=10),
        Faturamento(id=2, grupo_id=1, faturamento=20)
    ]

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = lista_faturamento
    
    resultado = await obter_importacao_faturamento(1, session_mock, True)

    assert resultado == lista_faturamento, 'A função obter_importacao_faturamento não retornou o faturamento correto'

@pytest.mark.asyncio
async def test_obter_importacao_faturamento_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = []

    with pytest.raises(Exception) as excinfo:
        await obter_importacao_faturamento(1, session_mock, True)
        
    assert 'Faturamento de importação por grupo não encontrada' in str(excinfo.value), 'A função obter_importacao_faturamento não retornou o erro correto'

@pytest.mark.asyncio
async def test_obter_exportacao_quantidade(mocker: MockerFixture):
    lista_quantidade = [
        Quantidade(id=1, grupo_id=1, quantidade=10),
        Quantidade(id=2, grupo_id=1, quantidade=20)
    ]

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = lista_quantidade
    
    resultado = await obter_exportacao_quantidade(1, session_mock, True)

    assert resultado == lista_quantidade, 'A função obter_exportacao_quantidade não retornou a quatidade correta'

@pytest.mark.asyncio
async def test_obter_exportacao_quantidade_nao_encontrado(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = []

    with pytest.raises(Exception) as excinfo:
        await obter_exportacao_quantidade(1, session_mock, True)
        
    assert 'Quantidade de exportação por grupo não encontrada' in str(excinfo.value), 'A função obter_exportacao_quantidade não retornou o erro correto'

@pytest.mark.asyncio
async def test_obter_exportacao_faturamento(mocker: MockerFixture):
    lista_faturamento = [
        Faturamento(id=1, grupo_id=1, faturamento=10),
        Faturamento(id=2, grupo_id=1, faturamento=20)
    ]

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = lista_faturamento
    
    resultado = await obter_exportacao_faturamento(1, session_mock, True)

    assert resultado == lista_faturamento, 'A função obter_exportacao_faturamento não retornou a exportação correta'

@pytest.mark.asyncio
async def test_obter_exportacao_faturamento(mocker: MockerFixture):
    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .where.return_value \
                .all.return_value = []

    with pytest.raises(Exception) as excinfo:
        await obter_exportacao_faturamento(1, session_mock, True)
        
    assert 'Faturamento de exportação por grupo não encontrada' in str(excinfo.value), 'A função obter_exportacao_faturamento não retornou o erro correto'


@pytest.mark.asyncio
async def test_obter_processamento_do_grupo(mocker: MockerFixture):
    grupo = Grupo(id=1, nome='Grupo 1', processamento=[
        Processamento(id=1, grupo_id=1, quantidade=10),
        Processamento(id=2, grupo_id=1, quantidade=20)
    ])

    session_mock = mocker.patch.object(Session, '__init__', return_value=None)
    session_mock.query.return_value \
                .where.return_value \
                .first.return_value = grupo
    
    resultado = await obter_processamento_do_grupo(1, session_mock, True)

    assert resultado == grupo.processamento, 'A função obter_processamento_do_grupo não retornou o processamento correto'