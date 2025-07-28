import streamlit as st
from PIL import Image

# Configuração da página com layout mais amplo
st.set_page_config(
    page_title="🏠 Home - Avaliação de Projetos", 
    page_icon="🏠",
    layout="wide"
)

# ESTILOS E CSS CUSTOMIZADO
st.markdown("""
    <style>
        /* Estilos gerais */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* Cabeçalhos */
        .main-header {
            color: #4B0082;
            text-align: center;
            padding: 1rem;
            border-bottom: 2px solid #4B0082;
            margin-bottom: 2rem;
        }
        
        /* Cards */
        .custom-card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            background: white;
            border-left: 4px solid #4B0082;
        }
        
        /* Botões */
        .stButton>button {
            background-color: #4B0082;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            margin-top: 1rem;
        }
        
        /* Projetos */
        .project-card {
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 3px solid #4B0082;
        }
        
        /* Link do forms */
        .forms-link {
            background-color: #4B0082;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.3rem 0.8rem;
            font-size: 0.9rem;
            text-decoration: none;
            display: inline-block;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO
image = Image.open('header.png')
st.image(image, use_container_width=True)

# TÍTULO PRINCIPAL
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0;'>Avaliação de Projetos</h1>
        <p style='margin:0; font-size:1.1rem;'>CIP - Central de Inteligência de Projetos</p>
    </div>
""", unsafe_allow_html=True)

# INSTRUÇÕES
with st.container():
    st.markdown("""
        <div class="custom-card">
            <h3 style='color: #4B0082;'>📋 Instruções de Avaliação</h3>
            <p>Nesta plataforma, sua tarefa é avaliar cada proposta de projeto em <strong>duas dimensões:</strong></p>
            <ol>
                <li><strong>O problema</strong> que o projeto busca resolver</li>
                <li><strong>A solução</strong> proposta</li>
            </ol>
            <p>Atribua <strong>uma nota de 0 a 5</strong> para cada critério:</p>
            <ul>
                <li>0 - Não atende ao critério (nota mínima)</li>
                <li>5 - Atende plenamente ao critério (nota máxima)</li>
            </ul>
            <p>A avaliação será calculada automaticamente conforme os pesos pré-definidos.</p>
        </div>
    """, unsafe_allow_html=True)

# LISTA DE PROJETOS
st.markdown("""
    <div style="margin-top: 2rem;">
        <h2 style='color: #4B0082; text-align: center;'>📌 Propostas de Projeto em Aberto</h2>
    </div>
""", unsafe_allow_html=True)

# PROJETO 1
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("""
            <div class="project-card">
                <h3 style='color: #011B70; margin:0;'>Projeto 1: Automação de Contratos Aprendiz - Empregador (Planilha de Custos) </h3>
                <p style="margin: 0.5rem 0;"><strong>Superintendência:</strong> SUPEX</p>
                <p style="margin: 0.5rem 0;"><strong>Gerência:</strong> Jurídica e Compliance e DPO - Supervisão de Administração de Contratos</p>
                <p style="margin: 0.5rem 0 1rem 0;"><strong>Proponente:</strong> Fabricio Canonaco</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Avaliar Projeto 1 ", key="projeto1"):
            st.switch_page("pages/1_Automacao Aprendiz Empregador Planilha de Custos.py")
    with col2:
        if st.button("Resultados Projeto 1", key="projeto1result"):
            st.switch_page("pages/1_Resultado Avaliacao Aprendiz Empregador Planilha de Custos.py")

# PROJETO 2
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("""
            <div class="project-card">
                <h3 style='color: #011B70; margin:0;'>Projeto 2 - Automação de Contratos Aprendiz - Empregador</h3>
                <p style="margin: 0.5rem 0;"><strong>Superintendência: SUPEX</strong> SUPEX</p>
                 <p style="margin: 0.5rem 0;"><strong>Gerência:</strong> Jurídica e Compliance e DPO - Supervisão de Administração de Contratos</p>   
                <p style="margin: 0.5rem 0 1rem 0;"><strong>Proponente:</strong> Fabrício Canonaco</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Avaliar Projeto 2", key="projeto2"):
            st.switch_page("pages/2_Automacao Contratos Aprendiz-Empregador.py")
    with col2:
        if st.button("Resultados Projeto 2", key="projeto2result"):
            st.switch_page("pages/2_Resultado Avaliacao Automacao Contratos .py")

# Ranking
with st.container():
    col1,col2, col3 = st.columns([30,8,30])
    
    with col2:
        if st.button("Ranking", key="Ranking"):
            st.switch_page("pages/Ranking.py")


# RODAPÉ
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
        CIP - Central de Inteligência de Projetos | Versão 2.0
    </div>
""", unsafe_allow_html=True)