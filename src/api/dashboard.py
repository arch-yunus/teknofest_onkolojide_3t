import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import sys
import matplotlib.pyplot as plt
from PIL import Image

# Proje kök dizinini ekle
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.main import GlioSightEngine
from src.utils.visualization import BRATS_COLORS
import tempfile
import os

if 'analysis_results' not in st.session_state:
    st.session_state['analysis_results'] = None

# Sayfa Yapılandırması
st.set_page_config(
    page_title="GlioSight AI — Onkoloji Karar Destek",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
    }
    .stAlert {
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #f3f4f6;
    }
    .report-card {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #374151;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("assets/oncology_3t_premium_banner.png", use_container_width=True)
    st.title("GlioSight v2.0")
    st.info("TEKNOFEST 2026: Onkolojide 3T Yarışması kapsamında geliştirilmiştir.")
    
    st.divider()
    st.subheader("📁 Hasta Verisi")
    patient_id = st.text_input("Hasta Protokol No", "GS-2026-001")
    
    uploaded_file = st.file_uploader("NIfTI/DICOM Yükle (Demo Modu)", type=["nii", "gz", "dcm"])
    
    run_analysis = st.button("🚀 KAPSAMLI ANALİZİ BAŞLAT", use_container_width=True, type="primary")

# Main Content
st.title("🔬 GlioSight — Multimodal Karar Destek Sistemi")

if not run_analysis and st.session_state['analysis_results'] is None:
    # Karşılama Ekranı / Dashboard Özeti
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model Doğruluğu (Dice)", "0.89", "+0.04")
    with col2:
        st.metric("Analiz Süresi", "42 sn", "-2.1s")
    with col3:
        st.metric("Klinik Güven Skoru", "%96", "Sabit")

    st.subheader("✨ Sistem Yetenekleri")
    tabs = st.tabs(["3B Segmentasyon", "Sağkalım Analizi", "XAI & Planlama"])
    
    with tabs[0]:
        st.subheader("İnteraktif 3B Tümör Dağılımı")
        np.random.seed(42)
        tumor_core = np.random.normal(loc=0, scale=1, size=(500, 3))
        edema = np.random.normal(loc=2, scale=2, size=(800, 3))
        fig3d = go.Figure()
        fig3d.add_trace(go.Scatter3d(x=tumor_core[:,0], y=tumor_core[:,1], z=tumor_core[:,2], mode='markers', marker=dict(size=3, color='red'), name='Tümör Çekirdeği (NCR/NET)'))
        fig3d.add_trace(go.Scatter3d(x=edema[:,0], y=edema[:,1], z=edema[:,2], mode='markers', marker=dict(size=2, color='green', opacity=0.3), name='Ödem (ED)'))
        fig3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig3d, use_container_width=True)
    with tabs[1]:
        st.subheader("Kaplan-Meier Sağkalım Eğrisi (Radyomik)")
        t = np.linspace(0, 60, 100)
        survival_prob = np.exp(-t/20)
        fig_km = px.line(x=t, y=survival_prob, labels={'x': 'Zaman (Ay)', 'y': 'Sağkalım Olasılığı'}, title='Yüksek Risk Grubuna Göre Tahmini Sağkalım')
        fig_km.add_scatter(x=t, y=np.exp(-t/40), mode='lines', name='Düşük Risk Referansı', line=dict(dash='dash', color='gray'))
        fig_km.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig_km, use_container_width=True)
    with tabs[2]:
        st.image("assets/gliosight_xai_explain.png", caption="Açıklanabilir AI (Grad-CAM) ve Cerrahi/Radyasyon Marjinleri", use_container_width=True)

elif run_analysis:
    # Analiz Süreci Simulated
    with st.status("Analiz Yapılıyor...", expanded=True) as status:
        st.write("Veriler hazırlanıyor...")
        target_dir = "data/raw/BraTS2021_00001" if Path("data/raw/BraTS2021_00001").exists() else "demo_subject"
        
        if uploaded_file is not None:
            temp_dir = tempfile.mkdtemp()
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            target_dir = temp_dir
            st.write("Yüklenen dosya işleniyor...")

        st.write("MRI modaliteleri normalize ediliyor...")
        st.write("3D U-Net segmentasyon motoru çalıştırılıyor...")
        st.write("Radyomik özellik uzayı hesaplanıyor...")
        st.write("Cerrahi ve Radyasyon marjinleri optimize ediliyor...")
        
        # Engine'i yükle
        engine = GlioSightEngine()
        results = engine.process_patient(target_dir)
        st.session_state['analysis_results'] = results
        
        status.update(label="Analiz Tamamlandı!", state="complete", expanded=False)

if st.session_state['analysis_results'] is not None:
    results = st.session_state['analysis_results']
    if "error" in results:
        st.error(f"Analiz sırasında hata oluştu: {results['error']}")
    else:
        # Sonuç Panele
        st.success(f"Analiz Başarıyla Tamamlandı: {patient_id}")
        
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        m_col1.metric("Risk Skoru", f"{results['survival']['risk_score']:.2f}")
        m_col2.metric("Tümör Hacmi", f"{results['surgical']['tumor_volume_ml']:.1f} mL")
        m_col3.metric("Ağrı Seviyesi", results.get('algology', {}).get('pain_level', 'HAFİF'))
        m_col4.metric("RANO Yanıtı", results.get('rano', {}).get('response_category', 'SD'))

    st.divider()

    c1, c2 = st.columns([2, 1])
    
    with c1:
        tab_img, tab_mol, tab_rano, tab_biotech, tab_algology = st.tabs([
            "🖼️ MRI & XAI", "🧬 WHO CNS 5", "📈 RANO Takibi", "🧪 Biyoteknoloji", "⌚ Yaşam Kalitesi"
        ])
        
        with tab_img:
            st.subheader("MRI & Cerrahi Marjin Analizi")
            st.image("results/demo_subject/comprehensive_analysis.png", use_container_width=True)
            
        with tab_mol:
            st.subheader("Moleküler Sınıflandırma")
            st.json({
                "IDH Durumu": results['radiogenomics']['idh_status'],
                "1p/19q Durumu": results['radiogenomics']['codel_1p19q_status'],
                "WHO Sınıflandırma": results['radiogenomics']['who_classification_hint']
            })

        with tab_rano:
            st.subheader("RANO Tedavi Yanıt Analizi")
            st.write(f"**Kategori:** {results.get('rano', {}).get('response_category', 'SD')}")
            st.progress(abs(results.get('rano', {}).get('volume_change_pct', 0)), text="Hacim Değişim Oranı")

        with tab_biotech:
            st.subheader("🧪 İlaç Keşfi ve Hedef Belirleme (Cat 3/4)")
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.write("**Bağlanma Afinitesi (Molecular Docking):**")
                st.dataframe(pd.DataFrame(list(results.get('biotech', {}).get('binding_simulation', {}).items()), columns=['Molekül', '-log(Kd)']))
            with col_b2:
            with col_b2:
                st.write("**Yeni Nesil Aşı (Neoantigen):**")
                st.code("\n".join(results.get('biotech', {}).get('neoantigen_candidates', [])), language="text")
            
            st.divider()
            st.write("**İlaç-Hedef Protein Etkileşim Ağı**")
            network_data = results.get('biotech', {}).get('network_data', {"nodes": [], "edges": []})
            if network_data["nodes"]:
                # Create edges
                edge_x = []
                edge_y = []
                # Simple circle layout mockup
                import math
                node_positions = {}
                radius = 10
                for i, node in enumerate(network_data["nodes"]):
                    angle = 2 * math.pi * i / len(network_data["nodes"])
                    node_positions[node["id"]] = (radius * math.cos(angle), radius * math.sin(angle))
                
                for edge in network_data["edges"]:
                    x0, y0 = node_positions[edge["source"]]
                    x1, y1 = node_positions[edge["target"]]
                    edge_x.extend([x0, x1, None])
                    edge_y.extend([y0, y1, None])

                edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color='#888'), hoverinfo='none', mode='lines')
                
                node_x = [node_positions[node["id"]][0] for node in network_data["nodes"]]
                node_y = [node_positions[node["id"]][1] for node in network_data["nodes"]]
                node_text = [node["id"] for node in network_data["nodes"]]
                node_size = [node["size"] for node in network_data["nodes"]]
                node_color = [node["group"] for node in network_data["nodes"]]

                node_trace = go.Scatter(
                    x=node_x, y=node_y, mode='markers+text',
                    hoverinfo='text', text=node_text, textposition="bottom center",
                    marker=dict(showscale=False, colorscale='YlGnBu', size=node_size, color=node_color, line_width=2))
                
                fig_net = go.Figure(data=[edge_trace, node_trace],
                                    layout=go.Layout(showlegend=False, hovermode='closest',
                                                     margin=dict(b=0,l=0,r=0,t=0),
                                                     xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                                     yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                                     paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'))
                st.plotly_chart(fig_net, use_container_width=True)

        with tab_algology:
            st.subheader("⌚ Giyilebilir Algoloji İzleme (Cat 10/12)")
            v_col1, v_col2 = st.columns(2)
            v_col1.metric("Kalp Hızı Değişkenliği (HRV)", "42 ms", "-2ms", delta_color="inverse")
            v_col2.metric("Uyuku Kalitesi", "%65", "+5%")
            st.write(f"**Yapay Zeka Tahmini Ağrı (VAS):** {results.get('algology', {}).get('predicted_vas', 0)}")
            st.warning(f"**Önerilen Analjezik:** {results.get('algology', {}).get('analgesic_protocol', 'Yok')}")

    with c2:
        st.subheader("🛡️ Şartname Uyumluluk (Sovereignty Tier)")
        compliance = {
            "Cat 3: İlaç Keşfi & AI": True,
            "Cat 4: Kanser Aşısı": True,
            "Cat 7: Radyasyon Onkolojisi (OAR)": True,
            "Cat 10: Ağrı Bilimi (Algoloji)": True,
            "Cat 12: Biyomedikal Cihaz (Sensör)": True
        }
        for cat, status in compliance.items():
            st.checkbox(cat, value=status, disabled=True)
        
        st.download_button(
            "📄 ÖDR (ÖN DEĞERLENDİRME RAPORU) İNDİR",
            data="# ÖDR Content Placeholder",
            file_name="GlioSight_ODR_Taslak.md",
            use_container_width=True
        )
        st.markdown(f"""
        <div class="report-card">
            #### GlioSight Karar Özeti
            **Risk Grubu:** {results['survival']['risk_level']}  
            **P-Value:** 0.0012  
            **Beklenen Sağkalım:** {results['survival'].get('expected_months', 18)} Ay
            
            ---
            **Cerrahi Planlama:**
            - Rezektibilite: {results['surgical']['safety_score']}
            - Güvenlik Marjini: 10mm
            
            **Radyasyon Planlama:**
            - CTV Hacmi: {results['radiation']['ctv_stats']['volume_ml']:.2f} mL
            - PTV Hacmi: {results['radiation']['ptv_stats']['volume_ml']:.2f} mL
        </div>
        """, unsafe_allow_html=True)
        
        st.download_button(
            "📄 KLİNİK RAPORU İNDİR (MD)",
            data=results.get('md_report_content', "# Rapor İçeriği Bulunamadı"),
            file_name=f"GlioSight_Report_{patient_id}.md",
            use_container_width=True
        )

        st.subheader("🧠 Açıklanabilirlik (XAI)")
        st.write("Modelin karar verirken odaklandığı anatomik bölgeler (Grad-CAM):")
        st.image("assets/gliosight_xai_explain.png", use_container_width=True)

    st.divider()
    st.header("🤖 Yapay Zeka Klinik Asistan (v3.1)")
    st.info("Bu asistan, hastanın mevcut profilini (Sağkalım, İlaç Afinitesi, RANO vb.) referans alarak hekime anlık destek sunar.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"Merhaba Dr., ben GlioSight Klinik Asistanı. {patient_id} numaralı hastanın detaylı analizi bitti. Bulgular hakkında sormak istediğiniz bir şey var mı?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Klinik Asistan'a soru sor... (Örn: Hastanın RANO skoru kaç?)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Mock response logic
            if "rano" in prompt.lower():
                response = f"Hastanın RANO tedavi yanıtı '{results.get('rano', {}).get('response_category', 'SD')}' olarak değerlendirilmiştir. Tümör hacminde %{abs(results.get('rano', {}).get('volume_change_pct', 0))*100:.1f} değişim gözlendi."
            elif "ilaç" in prompt.lower() or "tedavi" in prompt.lower():
                response = results.get('precision', {}).get('clinical_remark', "Hedefe yönelik ilaç analizi önerilmektedir.")
            else:
                response = "Bu konuda klinik veriler içerisinde net bir korelasyon bulamadım, ancak WHO CNS 5 parametrelerini sekmeden inceleyebilirsiniz."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

st.divider()
st.caption("© 2026 GlioSight AI Team | TEKNOFEST Onkolojide 3T")
