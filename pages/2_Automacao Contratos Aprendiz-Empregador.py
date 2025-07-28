import streamlit as st
import pandas as pd
import os
from PIL import Image

# Configuração da página com layout mais amplo
st.set_page_config(
    page_title="Automação Contratos Aprendiz Empregador", 
    page_icon="📋",
    layout="wide"
)

def calcular_media(notas, pesos):
    return sum(n * p for n, p in zip(notas, pesos))

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
        
        /* Sliders */
        .stSlider {
            margin-bottom: 1.5rem;
        }
        
        /* Botões */
        .stButton>button {
            background-color: #4B0082;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            margin-top: 1rem;
        }
        
        /* Expanders */
        .stExpander {
            margin-bottom: 1rem;
        }
        
        /* Métricas */
        .stMetric {
            border-radius: 5px;
            padding: 1rem;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO

# Imagem de cabeçalho
image = Image.open('headerav.png')
st.image(image, use_container_width=True)

# Título principal (Nome e informações do projeto)
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0;'>Projeto - Automação de Contratos Aprendiz - Empregador </h1> 
        <p style='margin:0; font-size:1.1rem;'>SUPEX -Gerência Jurídica e Compliance e DPO - Supervisão de Administração de Contratos
 - Fabrício Canonaco</p>
    </div>
""", unsafe_allow_html=True)

# SEÇÃO DE INFORMAÇÕES DO PROJETO

col1, col2 = st.columns([1, 1])

with col1:
    with st.expander("🧱 **Problema Identificado**", expanded=False):
        st.markdown("""
            O atual fluxo para emissão dos contratos da modalidade Aprendiz Empregador, conforme Apresentação, gera intenso trabalho manual e dedicação de colaboradores, reduzindo a produtividade das equipes e dificultando maior controle, transparência e assertividade das informações fornecidas pelo CIEE. Os problemas se relacionam a questões de eficiência e produtividade nos processos relacionados aos contratos, como criação, revisão, aprovação e armazenamento, bem como, tempo e recursos, permitindo que os colaboradores tenham menos tempo para tarefas mais estratégicas e de maior valor. Como exemplo, podemos citar... Isso impacta as negociações e formalizações de novas parcerias.
                   - Link da apresentação: https://docs.google.com/presentation/d/1sFp0EpFk54Tpih4Xqe0MGzKZw8o9RKSgHR7rD5SBs_Q/edit?usp=sharing """)

with col2:
    with st.expander("💡 **Solução Proposta**", expanded=False):
        st.markdown("""
          A emissão dos contratos de forma automatizada e por meio do Kairós, representa um enorme ganho em eficiência, transparência, controle, conformidade e economia de custos ao simplificar muitos processos relacionados aos contratos, como criação, revisão, aprovação, armazenamento, tempo e recursos, permitindo que os colaboradores se concentrem em tarefas mais estratégicas e de maior valor, como análises de instrumentos jurídicos de empresas da segmentação A ou projetos específicos com Orgãos Públicos (BEEM). 

A proposta é que todo esse fluxo ocorra de forma automatizada, onde a Unidade preenche as informações uma única vez no Kairós, e o sistema orquestra as etapas subsequentes até a liberação para contratações integrando tarefas com CNPC para análise de score, gerando relatórios, obtendo aprovação, integrando com a Gestão do Aprendiz para validação automatizada das condições a serem praticada para o aprendiz (com base em regras pré-definidas), integrando com DocuSign/CLM, e carregando todas as informações no Kairós e TOTVS, com mínima intervenção humana. 

Em síntese, impacta positivamente nas negociações e formalizações de novas parcerias. A solicitação de formalização do contrato poderá ser iniciada na visão (i) Backoffice Kairós ou no (ii) portal do CIEE por iniciativa da parte interessada. Neste momento, será contemplado apenas a solicitação do contrato Aprendiz Empregador, em novo fluxo. Além disso, damos celeridade a negociações em andamento, subsidiando tratativas entre Área de Atendimento e Parceiro, bem como contratos já assinados/cadastrados, subsidiando possíveis renovações, atualizações de valores, etc.

Toda a proposta de funcionalidades, fluxos de trabalho e telas, com inputs e outputs necessários, está detalhada em documentação completa de requisitos, disponível no link: https://drive.google.com/file/d/1a2eq0Y_PIgsKDlGPPCKMtMW7qfv_pTUT/view?usp=sharing .
                    Novo Fluxo: https://drive.google.com/file/d/1KtlkPgT8h4WeQzrSZ7Kb6qU18M26e1Xp/view?usp=sharing
        """)

col3, col4 = st.columns([1, 1])

with col3: 
    with st.expander("🗺️ **Roadmap do Projeto**", expanded=False):
        st.markdown("""
            **Início do Projeto: Fevereiro/2026**
- 1. Envolvimento das partes interessadas e kick off
- 2. reuniões recorrentes da equipe de projeto para análise e ajustes na documentação de requisitos e fluxos
- 3. revisão de cronograma e elaboração de cronograma final
- 4. prototipação e desenvolvimento (Sistemas) com acompanhamento, testes e validações da equipe do projeto
- 5. publicação e divulgação do novo fluxo operacional e sistêmico 
- 6. Piloto com GR SP Capital (Unid. Barueri)
- 7. Apresentar resultado do piloto e realizar ajustes na solução e nos fluxos propostos
- 8. Preparar comunicações internas (pontuais e recorrentes)
- 9. Preparar e aplicar treinamentos
- 10. Monitorar nova "operação" dentro do novo fluxo e nova solução (6 meses)
- 11. Analisar os indicadores propostos e apresentar resultados iniciais do projeto implementado para novos ajustes/melhorias (se necessários).
- 12. Sessão de lições aprendidas e encerramento do projeto
                    **Encerramento do Projeto: Janeiro/2027**
        """)

with col4:
    with st.expander("💰 **Recursos Financeiros Previstos**", expanded=False):
        st.markdown("""
Custo de OPEX relacionado ao tempo de desenvolvimento, a ser dimensionado pela Gerência de Tecnologia + custo de integração com o CLM (R$ 60.960,00 - estimativa por analogia ao serviço prestado pela Docusign no projeto Visual Law em nov/2023)
""")

col5, col6 = st.columns([1, 1])
       
with col5:
    with st.expander("🎯 **Resultados Esperados**", expanded=False):
        st.markdown("""

- 1) Redução de trabalho e SLAs (Financeiro; Marca; Processual / Tecnológico)
    INDICADOR: 
    - - a) SLA reduzido = de 10 para 2 dias na emissão de contratos do produto Aprendiz Empregador = - 80% (ou seja, retorno ao cliente pode passar de semanas para até algumas horas)
    - - b) Custo (homem-hora) reduzido de  90,09 para  16,85 por contrato = -80% (Para 600 contratos por ano: 54.000 - 10.000 = -  44.000,00 anuais)
    - - c) volume de trabalho reduzido de de 215 para 40 minutos por contrato = -81% 

- 2) Número de tickets Zendesk zerado para AIJ e NPC - SUNOA / Ailton Jr) (Produtividade; Processual / Tecnológico)
INDICADOR: tickets relacionados abertos na Zendesk = 0

- 3) Melhoria na satisfação com cliente interno e externo (Financeiro; Marca)
INDICADOR: entrevista qualitativa com Unidades, áreas beneficiadas e clientes externos

- 4) Fluxos e processos automatizados no Kairós; (Processual / Tecnológico)
INDICADOR: 0/1 ; feito / não feito

- 5) Registro e cópias dos instrumentos jurídicos relacionados (Segurança Jurídica)
INDICADOR: 0/1 ; feito / não feito

- 6) Acelerar as negociações do Atendimento (Aprendiz Empregador) (Produtividade; Financeiro; Marca; Processual / Tecnológico)
INDICADOR: entrevista qualitativa com consultores

- 7) Não perder parceiros por demora na formalização de parcerias (Financeiro; Marca)
INDICADOR: entrevista qualitativa com consultores

- 8) Maior controle, transparência e assertividade das informações (Financeiro; Marca)
INDICADOR: entrevista qualitativa com consultores e clientes

- 9) Fortalecimento da conformidade (score, validação legal e registro seguidos rigorosamente)
INDICADOR: entrevista qualitativa com Compliance

- 10) Aprimoramento da governança de dados (Kairós como fonte única e confiável para os dados contratuais)
INDICADOR: entrevista qualitativa com o DBA

(custo médio por hora de um profissional, que, considerando um salário de 4.426,00 para uma jornada mensal de 176 horas, resulta em aproximadamente 25,15 por hora fora impostos)
 """)

with col6:
    with st.expander("🤝 **Áreas Envolvidas**", expanded=False):
        st.markdown("""
- SUPEX: Supervisão de Administração de Contratos; 
- SUPEX: Supervisão de Desenvolvimento de Sistemas e Processos de Atendimento; 
- SAFIN: Gerência de Contas a Pagar e Receber (CNPC, SECOR)
- SUNOA: Gerência Nacional de Operações (Núcleo de Processos Contratuais)
- SUNOA: Gerência Regional de Atendimento SP Capital (ou outra GR)
- SUNOA: Supervisão de Gestão do Aprendiz; 
- SUNOA: Supervisão de Administração e Operação Contratos Estágio e Aprendiz; 
        """)

st.link_button("📝 Acessar Forms do Projeto", "https://docs.google.com/spreadsheets/d/1zZwLYqN_6etRW5ke102gqqlnXzV18LumLcWldDL2R8Y/edit?hl=pt-BR&forcehl=1&gid=855947888#gid=855947888",
                  use_container_width=True)

# SEÇÃO DE AVALIAÇÃO

st.markdown("""
    <div class="custom-card">
        <h2 style='color: #4B0082; text-align: center;'>🎯 Avaliação do Projeto </h2>
    </div>
""", unsafe_allow_html=True)

# Seleção de avaliador
nomes_usuarios = ["Aline Oliveira","André Diniz", "Integrante SAFIN","Leonardo Briza", 
                 "Marcelo Gallo","Monica Vargas", "Patricia Testai", "Paulo Ravagnani", "Rodrigo Dib"]
avaliador = st.selectbox("**Selecione seu nome:**", nomes_usuarios, index=None, placeholder="Escolha seu nome...")

# Opção para abster-se
if avaliador:
    abster = st.checkbox("Desejo me abster desta votação (minhas avaliações serão desconsideradas)")
else:
    abster = False

# Mostrar os critérios apenas se não estiver abstendo
if avaliador and not abster:
    # CRITÉRIOS - PROBLEMA
    st.markdown("""
        <div class="custom-card">
            <h3 style='color: #011B70; text-align: center;'>Critérios - Problema</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        gravidade = st.slider(
            "**Gravidade do problema - Peso: 0,50**\n"
            "\nO problema é sério? Pode traver impactos relevantes se não for resolvido?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa gravidade | 5 = Extremamente grave"
        )

    with col2:
        urgencia = st.slider(
            "**Urgência de Solução do Problema - Peso: 0,30**\n"
            "\nEssa é uma situação que exige ação imediata ou pode esperar?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa urgência | 5 = Muita urgência"
        )

    with col3:
        tendencia = st.slider(
            "**Tendência do Problema - Peso: 0,20**\n"
            "\nSe nada for feito, o problema tende a piorar, estagnar ou se resolver?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa tendência de piora | 5 = Alta tendência de piora"
        )

    # Cálculo da média do problema
    notas_problema = [gravidade, urgencia, tendencia]
    pesos_problema = [0.50, 0.30, 0.20]
    media_problema = calcular_media(notas_problema, pesos_problema)

    # Exibição com estilo
    st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin:0;">Média - Problema</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: {"#28a745" if media_problema >= 3.5 else "#ffc107" if media_problema >= 2 else "#dc3545"}">
                    {media_problema:.2f}
                </div>
            </div>
            <div style="margin-top: 0.5rem;">
                <progress value="{media_problema}" max="5" style="width:100%; height:10px; border-radius:5px; color: {"#28a745" if media_problema >= 3.5 else "#ffc107" if media_problema >= 2 else "#dc3545"}"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # CRITÉRIOS - SOLUÇÃO
    st.markdown("""
        <div class="custom-card">
            <h3 style='color: #011B70; text-align: center;'>Critérios - Solução</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        viabilidade_solucao = st.slider(
            "**Viabilidade da Solução - Peso: 0,30**\n"
            "\nA proposta é realista? Considera bem custos, prazos e riscos?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Inviável | 5 = Totalmente viável"
        )

        resultados_esperados = st.slider(
            "**Resultados Esperados - Peso: 0,30**\n"
            "\nOs resultados estão bem descritos? São mensuráveis?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Indefinidos | 5 = Bem definidos e mensuráveis"
        )

        impacto_solucao = st.slider(
            "**Impacto da Solução - Peso 0,20**\n"
            "\nA solução trará benefícios concretos para o CIEE?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixo impacto | 5 = Alto impacto "
        )

    with col2:
        alinhamento_estrategico = st.slider(
            "**Alinhamento Estratégico - Peso 0,10**\n"
            "\nConectada com planejamento estratégico ou compromissos institucionais?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Sem alinhamento | 5 = Totalmente alinhado"
        )

        abrangencia = st.slider(
            "**Abrangência (Público e Território) - Peso: 0,10**\n"
            "\nO projeto atinge muitas pessoas/áreas ou tem escopo limitado?",
            0.0, 5.0, 0.0, step=0.5,
            help="0 = Baixa abrangência | 5 = Alta abrangência"
        )

    # Cálculo da média da solução
    notas_solucao = [viabilidade_solucao, resultados_esperados, impacto_solucao, alinhamento_estrategico, abrangencia]
    pesos_solucao = [0.30, 0.30, 0.20, 0.10, 0.10]
    media_solucao = calcular_media(notas_solucao, pesos_solucao)

    # Exibição com estilo
    st.markdown(f"""
        <div class="custom-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="margin:0;">Média - Solução</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: {"#28a745" if media_solucao >= 3.5 else "#ffc107" if media_solucao >= 2 else "#dc3545"}">
                    {media_solucao:.2f}
                </div>
            </div>
            <div style="margin-top: 0.5rem;">
                <progress value="{media_solucao}" max="5" style="width:100%; height:10px; border-radius:5px; color: {"#28a745" if media_solucao >= 3.5 else "#ffc107" if media_solucao >= 2 else "#dc3545"}"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # OBSERVAÇÕES
    observacoes = st.text_area(
        "**Deixe sua opinião sobre o projeto avaliado:**",
        placeholder="Descreva aqui suas observações, sugestões ou considerações adicionais...",
        height=200
    )

    # RESULTADO FINAL
    media_geral = calcular_media([media_problema, media_solucao], [0.50, 0.50])

    # Definir cor e status com base na média
    if media_geral < 2:
        cor_status = "#dc3545"
        status = "REPROVADO"
    elif media_geral < 3.5:
        cor_status = "#ffd900f6"
        status = "REVISÃO NECESSÁRIA"
    else:
        cor_status = "#28a745"
        status = "APROVADO"

    st.markdown(f"""
        <div class="custom-card">
            <h3 style='text-align: center;'>Resultado Final Individual</h3>
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 2rem; font-weight: bold; color: {cor_status};">
                    {media_geral:.2f}
                </div>
                <div style="font-size: 1.5rem; font-weight: bold; color: {cor_status}; margin-top: 0.5rem;">
                    {status}
                </div>
                <progress value="{media_geral}" max="5" style="width:80%; height:15px; border-radius:5px; margin-top:1rem;"></progress>
            </div>
        </div>
    """, unsafe_allow_html=True)

# SALVAR AVALIAÇÃO
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("💾 Salvar Avaliação", use_container_width=True):
        if not avaliador:
            st.error("Por favor, selecione seu nome antes de salvar.")
        elif abster:
            # Se optou por abster-se, salva apenas o nome e a flag de abstenção
            dados = {
                "Avaliador": [avaliador],
                "Abstenção": ["Sim"],
                "Gravidade": [None],  # Usando None para deixar vazio
                "Urgência": [None],
                "Tendência": [None],
                "Média Problema": [None],
                "Viabilidade da Solução": [None],
                "Resultados Esperados": [None],
                "Impacto da Solução": [None],
                "Alinhamento Estratégico": [None],
                "Abrangência": [None],
                "Média Solução": [None],
                "Média Final": [None],
                "Observação": ["Avaliador optou por abster-se"]
            }
            
            df = pd.DataFrame(dados)
            arquivo = "avaliacoes02.xlsx"

            if os.path.exists(arquivo):
                df_existente = pd.read_excel(arquivo)
                if avaliador in df_existente["Avaliador"].values:
                    st.error("Este avaliador já preencheu a avaliação. Cada avaliador só pode avaliar cada projeto uma vez.")
                else:
                    df = pd.concat([df_existente, df], ignore_index=True)
                    df.to_excel(arquivo, index=False)
                    st.success("✅ Abstenção registrada com sucesso!")
            else:
                df.to_excel(arquivo, index=False)
                st.success("✅ Abstenção registrada com sucesso!")
                
        elif 'media_geral' not in locals():
            st.error("Por favor, preencha todos os critérios de avaliação.")
        else:
            # Código original para salvar avaliação normal
            dados = {
                "Avaliador": [avaliador],
                "Abstenção": ["Não"],
                "Gravidade": [gravidade],
                "Urgência": [urgencia],
                "Tendência": [tendencia],
                "Média Problema": [media_problema],
                "Viabilidade da Solução": [viabilidade_solucao],
                "Resultados Esperados": [resultados_esperados],
                "Impacto da Solução": [impacto_solucao],
                "Alinhamento Estratégico": [alinhamento_estrategico],
                "Abrangência": [abrangencia],
                "Média Solução": [media_solucao],
                "Média Final": [media_geral],
                "Observação": [observacoes]
            }

            df = pd.DataFrame(dados)
            arquivo = "avaliacoes02.xlsx"

            if os.path.exists(arquivo):
                df_existente = pd.read_excel(arquivo)
                if avaliador in df_existente["Avaliador"].values:
                    st.error("Este avaliador já preencheu a avaliação. Cada avaliador só pode avaliar cada projeto uma vez.")
                else:
                    df = pd.concat([df_existente, df], ignore_index=True)
                    df.to_excel(arquivo, index=False)
                    st.success("✅ Avaliação salva com sucesso!")
            else:
                df.to_excel(arquivo, index=False)
                st.success("✅ Avaliação salva com sucesso!")



# RODAPÉ
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
        CIP - Central de Inteligência de Projetos | Versão 2.0
    </div>
""", unsafe_allow_html=True)