import streamlit as st
import pandas as pd
import plotly.express as px

# ================== PAGE CONFIG & THEME ==================
st.set_page_config(page_title="Okta Global Services Tracker", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #3c3f8f; }
    .stProgress > div > div { background-color: #3c3f8f; }
    </style>
""", unsafe_allow_html=True)

# ================== SIDEBAR INFO ==================
st.sidebar.title("📌 Project Summary")
st.sidebar.markdown("""
**Global Services Program Tracker**

A simulated dashboard for a company like Okta to track:
- 🔍 Partner performance
- 📊 Regional delivery metrics
- 🎓 Customer education impact

**Stack**: Python, Pandas, Streamlit, Plotly  
**Focus**: Reporting automation + insight delivery
""")

# ================== MOCK DATA ==================
partner_data = pd.DataFrame({
    'Partner': ['Alpha', 'Beta', 'Gamma', 'Delta'],
    'Engagement Rate (%)': [85, 72, 91, 66],
    'Certifications': [12, 8, 15, 5],
    'NPS Score': [45, 50, 72, 38]
})

project_status = pd.DataFrame({
    'Region': ['NA', 'EMEA', 'APAC', 'LATAM'],
    'Not Started': [2, 1, 3, 0],
    'In Progress': [5, 3, 2, 1],
    'Completed': [10, 8, 6, 4]
})

education_data = pd.DataFrame({
    'Course': ['Security Basics', 'API Access', 'Partner Onboarding'],
    'Completion %': [92, 76, 89],
    'Satisfaction Score': [4.5, 4.2, 4.7]
})

# ================== FILTERS ==================
st.title("🌐 Global Services Program Tracker")
st.markdown("Track partner performance, project delivery status, and customer education insights — built for an identity tech company like Okta.")

selected_region = st.selectbox("🌍 Filter by Region", options=project_status['Region'].unique())
filtered_status = project_status[project_status['Region'] == selected_region]

# ================== SCORECARD METRICS ==================
st.subheader("📈 Quarterly Scorecard")
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Partner Engagement", "78%", "+12% QoQ")
col2.metric("Project Completion (Global)", "65%", "-5%")
col3.metric("Reporting Automation Rate", "90%", "+18%")

# ================== PARTNER PERFORMANCE ==================
st.subheader("🤝 Partner Performance Overview")
st.dataframe(partner_data)

fig1 = px.bar(partner_data, x='Partner', y='Engagement Rate (%)', color='Partner',
              title='Partner Engagement Rate')
st.plotly_chart(fig1, use_container_width=True)

# ================== PARTNER PROFILE VIEWER ==================
st.subheader("🔎 Partner Profile Viewer")
selected_partner = st.selectbox("Select a Partner", partner_data['Partner'])
st.table(partner_data[partner_data['Partner'] == selected_partner].T)

# ================== PROJECT STATUS ==================
st.subheader("📊 Project Delivery Status by Region")
st.dataframe(filtered_status.set_index('Region'))

fig2 = px.bar(filtered_status.melt(id_vars='Region'), x='Region', y='value', color='variable',
              title=f'Project Status Distribution - {selected_region}')
st.plotly_chart(fig2, use_container_width=True)

# ================== EDUCATION INSIGHTS ==================
st.subheader("🎓 Customer Education Program Insights")
for i, row in education_data.iterrows():
    st.write(f"**{row['Course']}** — Satisfaction: {row['Satisfaction Score']} ⭐")
    st.progress(row['Completion %'] / 100)

# ================== PROGRAM HEALTH INSIGHTS ==================
st.subheader("🧠 Program Health Summary")
st.markdown("""
✅ **Gamma** has the highest engagement rate (91%) and certifications.  
⚠️ **LATAM** has lowest project completion rate — needs review.  
📚 Education program shows strong satisfaction, especially in *Security Basics*.
""")

# ================== EXPORT OPTION ==================
csv_data = partner_data.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Partner Data", data=csv_data, file_name='partner_data.csv', mime='text/csv')
