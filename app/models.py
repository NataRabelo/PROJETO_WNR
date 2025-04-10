# Vou manter o modelo de banco de dados em um arquivo único para facilitar a leitura e a manutenção do mesmo. 

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Float
from sqlalchemy.orm import relationship
from app import db

# Tabela Usuário
class Usuario(db.Model):
    __tablename__ = "usuarios"

    id                      = Column(Integer, primary_key=True, index=True)
    nome                    = Column(String, index=True)
    email                   = Column(String, unique=True, index=True)
    senha                   = Column(String)
    is_active               = Column(Boolean, default=True)
    role                    = Column(String(10), nullable=False, default="user")

    # Método obrigatório para Flask-Login
    def get_id(self):
        return str(self.id)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False




# Tabela Cliente
class Cliente(db.Model):
    __tablename__ = "clientes"

    id                      = Column(Integer, primary_key=True, index=True)
    nome                    = Column(String, index=True)
    cpf                     = Column(String(11), unique=True, index=True)
    email                   = Column(String, index=True)
    data_nascimento         = Column(Date)
    renda_familiar          = Column(Float)
    bairro                  = Column(String)
    canal_divulgacao        = Column(String)
    cep                     = Column(String(8))
    cidade                  = Column(String)
    condicao_habitacao      = Column(String)
    cpf_responsavel         = Column(String(11), nullable=True, default="")
    complemento             = Column(String)
    numero_cs               = Column(String)
    despesa_mensal          = Column(Float)
    escolaridade            = Column(String)
    estado                  = Column(String)
    endereco                = Column(String)
    fone_contato            = Column(String)
    fone_pessoal            = Column(String)
    foto                    = Column(String)
    grau_parentesco         = Column(String)
    nome_plano_saude        = Column(String, default="Sem plano de Saúde")
    nome_responsavel        = Column(String, default="")
    numero_filhos           = Column(Integer, default=0)
    possui_filhos           = Column(String)
    plano_saude             = Column(String)
    previdenciario          = Column(String)
    profissao               = Column(String)
    remuneracao             = Column(Float)
    rg                      = Column(String)
    saldo                   = Column(Float)
    sexo                    = Column(String)
    tipo_moradia            = Column(String)
    transporte              = Column(String)
    idade                   = Column(String)

    # Relacionamentos
    encaminhamentos = relationship("Encaminhamento", back_populates="cliente", cascade="all, delete-orphan")
    guias = relationship("Guia", back_populates="cliente")


# Tabela Profissional
class Profissional(db.Model):
    __tablename__ = "profissionais"

    id                      = Column(Integer, primary_key=True, index=True)
    nome                    = Column(String, index=True)
    cpf                     = Column(String(11), unique=True, index=True)
    email                   = Column(String, unique=True, index=True)
    data_nascimento         = Column(Date)
    bairro                  = Column(String)
    banco                   = Column(String)
    cep                     = Column(String(8))
    cidade                  = Column(String)
    complemento             = Column(String)
    graduacao               = Column(String)
    issqn                   = Column(String)
    fone_pessoal            = Column(String)
    fone_profissional       = Column(String)
    foto                    = Column(String)
    curriculum_lattes       = Column(String)
    dias_horas_disponiveis  = Column(String)
    endereco_profissional   = Column(String)
    estado                  = Column(String)
    observacoes             = Column(String)
    pix                     = Column(String)
    registro_profissional   = Column(String)
    rg                      = Column(String)
    valor_minimo            = Column(Float)

    # Relacionamentos
    encaminhamentos = relationship("Encaminhamento", back_populates="profissional", cascade="all, delete-orphan")
    guias = relationship("Guia", back_populates="profissional")


# Tabela Encaminhamento
class Encaminhamento(db.Model):
    __tablename__ = "encaminhamentos"

    id                      = Column(Integer, primary_key=True, index=True)
    cliente_id              = Column(Integer, ForeignKey("clientes.id", ondelete="CASCADE"))
    profissional_id         = Column(Integer, ForeignKey("profissionais.id", ondelete="CASCADE"))
    convenio                = Column(String)
    dias_horas_atendimento  = Column(String)
    data_encaminhamento     = Column(Date)
    observacoes_gerais      = Column(String)
    queixa                  = Column(String)
    situacao                = Column(String)
    tipo_encaminhamento     = Column(String)
    valor                   = Column(Float)

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="encaminhamentos")
    profissional = relationship("Profissional", back_populates="encaminhamentos")


# Tabela Guia
class Guia(db.Model):
    __tablename__ = "guias"

    id                      = Column(Integer, primary_key=True, index=True)
    cliente_id              = Column(Integer, ForeignKey("clientes.id"))
    profissional_id         = Column(Integer, ForeignKey("profissionais.id"))
    data_original           = Column(Date)
    hora_emissao            = Column(String)
    observacoes_gerais      = Column(String)
    quantidade_emissoes     = Column(Integer)
    tipo_pagamento          = Column(String)
    valor_unitario          = Column(Float)
    valor_total             = Column(Float)
    pago                    = Column(String)

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="guias")
    profissional = relationship("Profissional", back_populates="guias")
