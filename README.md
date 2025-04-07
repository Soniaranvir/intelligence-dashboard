# 🌐 OktaPulse: Global Services Intelligence Dashboard

OktaPulse is a real-time analytics dashboard designed for global services and partner teams in identity tech. It combines data from partner engagement, regional project delivery, and customer education to deliver a unified view of service performance — with built-in forecasting.

## ✨ Features

- 🤝 **Partner Performance Metrics**: Engagement rate, certifications, NPS
- 📊 **Project Delivery Tracking**: Interactive status by region
- 🎓 **Education Progress**: Course completion and satisfaction
- 🔮 **Forecasting**: Predict project workload using time-series modeling
- 🌑 **Dark Mode & Animations**: Beautiful UX with Lottie visuals
- 📤 **Data Export**: Downloadable reports for stakeholders

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Plotly, Lottie
- **Backend**: Python, Pandas, Statsmodels
- **Forecasting**: Holt-Winters Exponential Smoothing
- **Deployment**: Streamlit Cloud / HuggingFace Spaces

## 🚀 Live Demo

> [🔗 Click here to launch the app](https://your-live-link.streamlit.app)

## 📸 Screenshots

| Partner Metrics | Forecasting |
|---|---|
| ![Partner Metrics](assets/sample1.png) | ![Forecasting](assets/sample2.png) |

## 💡 Use Cases

- Internal dashboards for partner success teams
- Delivery ops in identity/security tech
- Strategic insights for services orgs

## 📦 Install Locally

```bash
git clone https://github.com/your-username/oktapulse-dashboard.git
cd oktapulse-dashboard
pip install -r requirements.txt
streamlit run app.py
