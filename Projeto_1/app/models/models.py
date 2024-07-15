from pydantic import BaseModel, ConfigDict


class Grupo(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    nome: str


# Criação de classes para os modelos de dados que serão usados na API
# Essas classes são usadas para validar os dados recebidos e enviados pela API
class Produto(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    nome: str
    grupo: Grupo


# Criação de classes para os modelos de dados que serão usados na API
# Essas classes são usadas para validar os dados recebidos e enviados pela API
class Producao(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    ano: int
    quantidade: int

class Comercializacao(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ano: int
    quantidade: int

class Pais(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    nome: str

class Quantidade(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    ano: int
    quantidade: int

class Faturamento(BaseModel):
    # Configuração para permitir a serialização e desserialização de objetos
    model_config = ConfigDict(from_attributes=True)

    # atributos do modelo
    id: int
    ano: int
    faturamento: int

class Processamento(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ano: int
    quantidade: int
