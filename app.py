import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(
    page_title="AI Market Intelligence 2024",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS para visual "High-Tech"
st.markdown("""
    <style>
    .main { background-color: #050505; }
    .stMetric { 
        background-color: #0a0a0a; 
        border: 1px solid #1f2937; 
        border-radius: 12px; 
        padding: 20px;
    }
    h1, h2, h3 { color: #60a5fa; }
    </style>
    """, unsafe_allow_html=True)

# --- DATASET 1: LLM BENCHMARKS ---
def get_llm_data():
    data = {
        'Modelo': ['GPT-4o', 'Claude 3.5 Sonnet', 'Gemini 1.5 Pro', 'Llama 3 (70B)', 'Mistral Large'],
        'Raciocínio (MMLU)': [88.7, 88.7, 85.9, 82.0, 81.2],
        'Codificação (HumanEval)': [90.2, 92.0, 84.1, 81.7, 73.0],
        'Custo ($/1M tokens)': [5.0, 3.0, 3.5, 0.6, 4.0],
        'Provedor': ['OpenAI', 'Anthropic', 'Google', 'Meta', 'Mistral']
    }
    return pd.DataFrame(data)

# --- DATASET 2: ADOÇÃO POR INDÚSTRIA ---
def get_adoption_data():
    data = {
        'Indústria': ['Finanças', 'Saúde', 'Tecnologia', 'Varejo', 'Educação', 'Manufatura'],
        'Investimento (Bi $)': [12.5, 8.2, 25.0, 5.4, 3.1, 7.8],
        'Crescimento YoY (%)': [45, 30, 65, 20, 15, 25]
    }
    return pd.DataFrame(data)

df_llm = get_llm_data()
df_adoption = get_adoption_data()

# --- SIDEBAR ---
st.sidebar.title("AI Intelligence Hub")
st.sidebar.info("Monitoramento em tempo real do ecossistema de IA Generativa.")
st.sidebar.markdown("---")
view_mode = st.sidebar.radio("Nível de Análise:", ["Visão Geral", "Benchmarks Técnicos", "ROI & Produtividade"])

# --- HEADER ---
st.title("🤖 AI Market Intelligence Dashboard")
st.markdown("Análise estratégica de modelos de linguagem e tendências de adoção global.")

if view_mode == "Visão Geral":
    # Métricas de Mercado
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Market Cap (AI)", "$1.2T", "+18%")
    m2.metric("Modelos Ativos", "150+", "Novos: 12")
    m3.metric("Líder de Coding", "Claude 3.5", "Anthropic")
    m4.metric("Líder de Raciocínio", "GPT-4o", "OpenAI")

    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🌐 Investimento Global por Indústria")
        fig_adoption = px.pie(df_adoption, values='Investimento (Bi $)', names='Indústria', 
                             hole=.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_adoption, use_container_width=True)
    
    with c2:
        st.subheader("📈 Crescimento Anual (YoY)")
        fig_growth = px.bar(df_adoption, x='Indústria', y='Crescimento YoY (%)', 
                           color='Crescimento YoY (%)', color_continuous_scale='Blues')
        st.plotly_chart(fig_growth, use_container_width=True)

elif view_mode == "Benchmarks Técnicos":
    st.subheader("📊 Performance Comparativa: Raciocínio vs Coding")
    fig_bench = px.scatter(df_llm, x='Raciocínio (MMLU)', y='Codificação (HumanEval)', 
                          size='Custo ($/1M tokens)', color='Modelo', text='Modelo',
                          hover_name='Provedor', template="plotly_dark")
    fig_bench.update_traces(textposition='top center')
    st.plotly_chart(fig_bench, use_container_width=True)
    
    st.markdown("---")
    st.subheader("💰 Eficiência de Custo (Lower is Better)")
    fig_cost = px.bar(df_llm.sort_values('Custo ($/1M tokens)'), x='Modelo', y='Custo ($/1M tokens)', 
                     color='Provedor', template="plotly_dark")
    st.plotly_chart(fig_cost, use_container_width=True)

elif view_mode == "ROI & Produtividade":
    st.subheader("🧮 Calculadora de Impacto de IA")
    col_calc1, col_calc2 = st.columns(2)
    
    with col_calc1:
        st.markdown("#### Parâmetros de Entrada")
        hours_saved = st.slider("Horas economizadas por colaborador/dia:", 0.5, 4.0, 1.5)
        num_employees = st.number_input("Número de colaboradores:", 1, 1000, 50)
        avg_salary = st.number_input("Salário médio por hora ($):", 10, 200, 45)
    
    with col_calc2:
        # Cálculos
        daily_savings = hours_saved * num_employees * avg_salary
        monthly_savings = daily_savings * 22
        yearly_savings = monthly_savings * 12
        
        st.markdown("#### Resultados Estimados")
        st.success(f"Economia Mensal: **<LaTex>${monthly_savings:,.2f}**")
        st.info(f"Economia Anual: **$</LaTex>{yearly_savings:,.2f}**")
        st.warning(f"Aumento de Capacidade: **+{ (hours_saved/8)*100:.1f}%**")

# --- FOOTER ---
st.markdown("---")
st.caption("Desenvolvido por Luan Antunes de Lima | Dados baseados em benchmarks de mercado 2024.")
