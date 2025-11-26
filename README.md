---
title: Azure Agent Currency Exchange
emoji: ⚡
colorFrom: pink
colorTo: red
sdk: gradio
sdk_version: 5.50.0
app_file: app.py
pinned: false
license: mit
short_description: AI-Powered Currency Exchange Assistant on Azure
tags:
  - azure-ai
  - agent-framework
---

<div align="center">

# 💱 Azure Agent Currency Exchange

**AI-Powered Currency Assistant hosted on Azure Container Apps**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/mahimairaja/azure-agent-currency-exchange/actions/workflows/ci.yml/badge.svg)](https://github.com/mahimairaja/azure-agent-currency-exchange/actions/workflows/ci.yml)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mahimairaja/azure-agent-currency-exchange)

[Demo](https://huggingface.co/spaces/mahimairaja/azure-agent-currency-exchange) • [Documentation](#-features) • [Installation](#-quick-start) • [Contributing](#-contributing)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 💱 **Real-time Exchange Rates**
Get up-to-the-minute currency exchange rates powered by the [Frankfurter API](https://www.frankfurter.app/).

### 🤖 **Natural Language Interface**
Ask questions in plain English like "How much is 100 USD in EUR?" powered by **Azure OpenAI (GPT-4o-mini)**.

</td>
<td width="50%">

### ☁️ **Azure Native**
Built on **Azure Container Apps** and the **Microsoft Agent Framework** for enterprise-grade scalability and security.

### 📊 **Full Observability**
Integrated with **Azure Monitor** and **Application Insights** for deep telemetry and performance tracking.

</td>
</tr>
</table>

---

## 🎯 Demo

Try it live on [Hugging Face Spaces](https://huggingface.co/spaces/mahimairaja/azure-agent-currency-exchange)!

**Example queries:**
```
💬 "How much is 100 USD in EUR?"
💬 "Convert 50 GBP to JPY"
💬 "What is the exchange rate for CAD to AUD?"
💬 "Show me the rate for Bitcoin (just kidding, fiat only!)"
```

---

## 📚 Architecture

![Conversation Flow](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdrive.google.com/uc?id=1GlSfBru8BrYBvFnKRDFVTyLSxKNnKrxn)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | ![Gradio](https://img.shields.io/badge/Gradio-FF6F00?style=flat&logo=gradio&logoColor=white) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) |
| **Agent Framework** | ![Microsoft Agent Framework](https://img.shields.io/badge/Agent_Framework-0078D4?style=flat&logo=microsoft&logoColor=white) |
| **LLM** | ![Azure OpenAI](https://img.shields.io/badge/Azure_OpenAI-0078D4?style=flat&logo=microsoft-azure&logoColor=white) |
| **Infrastructure** | ![Azure Container Apps](https://img.shields.io/badge/Azure_Container_Apps-0078D4?style=flat&logo=microsoft-azure&logoColor=white) |
| **Package Manager** | ![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat&logo=python&logoColor=white) |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- Azure Subscription (for backend deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahimairaja/azure-agent-currency-exchange.git
   cd azure-agent-currency-exchange
   ```

2. **Install dependencies**
   ```bash
   uv sync --all-groups
   ```

3. **Run Locally**

   **Frontend (Gradio):**
   ```bash
   uv run python app.py
   ```
   Open `http://localhost:7860` in your browser.

   **Backend (FastAPI):**
   ```bash
   uv run python main.py
   ```
   *Note: Backend requires Azure resources to be provisioned.*

---

## ☁️ Deployment

### Azure (Backend)

This project uses the **Azure Developer CLI (`azd`)** for easy deployment.

```bash
# Login to Azure
azd auth login

# -- Add required env variables to azure environment --

# 1. Setup Environment Name
azd env set AZURE_ENV_NAME "<YOUR-ENV-NAME>"

# 2. Setup Location
azd env set AZURE_LOCATION "<YOUR-AZURE-LOCATION>"

# 3. Setup Model Deployment Name
azd env set AZURE_AI_MODEL_DEPLOYMENT_NAME "gpt-4o-mini"

# NOTE: This env name and location depends your subscription and region availability.
# And for model name check the list of available models in your subscription.

# Provision and Deploy
azd up
```

This will create:
- Azure Container App (Agent Service)
- Azure OpenAI Service (GPT-4o-mini)
- Azure Monitor & Application Insights
- Managed Identities & RBAC

And you will find the Container App URL in the output of the `azd up` command.

### Hugging Face Spaces (Frontend)

The frontend is configured for automatic deployment to Hugging Face Spaces via GitHub Actions.

1. Create a Space on Hugging Face.
2. Set the `AZURE_API_URL` secret in your Space to your Azure Container App endpoint.
3. Push to `main` to trigger the sync workflow.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Mahimai Raja** - [LinkedIn](https://linkedin.com/in/mahimairaja) - [GitHub](https://github.com/mahimairaja)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Mahimai Raja](https://github.com/mahimairaja)

</div>
