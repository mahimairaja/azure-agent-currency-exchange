import os
import gradio as gr
import requests
from contants import DEFAULT_CONVERSION_RATE

API_URL = os.getenv("AZURE_API_URL").rstrip("/")


def static_response():
    response = "### 💱 Current Exchange Rates (Base: 1 EUR)\n\n"
    response += "| Currency | Rate |\n|----------|------|\n"

    for currency, rate in DEFAULT_CONVERSION_RATE.items():
        response += f"| **{currency}** | {rate} |\n"

    return response


def chat(message, history):
    if not message:
        return ""

    try:
        payload = {"prompt": message}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(
                f"{API_URL}/invoke", json=payload, headers=headers, timeout=30
            )
            response.raise_for_status()

            data = response.json()
        except requests.exceptions.RequestException:
            return static_response()

        if "result" in data:
            return data["result"]
        elif "detail" in data:
            return f"⚠️ Error from Agent: {data['detail']}"
        else:
            return str(data)

    except requests.exceptions.RequestException as e:
        return f"❌ Network Error: {str(e)}\n\nCheck if the agent endpoint is reachable: {API_URL}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


custom_css = """
.gradio-container {
    font-family: 'Inter', sans-serif;
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    margin-bottom: 1rem;
    color: white;
}

.header-content {
    text-align: left;
}

.header-container h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.header-container p {
    font-size: 1rem;
    opacity: 0.95;
    margin: 0.25rem 0 0 0;
}

.header-cta {
    margin-left: 2rem;
    text-align: center;
}

footer {
    text-align: center;
    padding: 0.5rem;
    color: #666;
    font-size: 0.8rem;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="purple",
        secondary_hue="blue",
        neutral_hue="slate",
    ),
    css=custom_css,
    title="Azure Currency Exchange",
) as demo:
    with gr.Row():
        gr.HTML(
            """
            <div class="header-container">
                <div class="header-content">
                    <h1>📊 Azure Currency Exchange</h1>
                    <p>Ask me anything about currency exchange rates!</p>
                    <p style="font-size: 0.85rem; opacity: 0.8;">
                        Powered by GPT-4o-mini • FastAPI • Azure Container Apps • Gradio UI • Azure Monitor
                    </p>
                </div>
                <div class="header-cta">
                    <a href="https://linkedin.com/in/mahimairaja" target="_blank" style="text-decoration: none;">
                        <button style="
                            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
                            color: white;
                            border: none;
                            padding: 10px 24px;
                            font-size: 1rem;
                            font-weight: 700;
                            border-radius: 8px;
                            cursor: pointer;
                            box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
                            transition: all 0.3s ease;
                            text-transform: uppercase;
                            letter-spacing: 1px;
                            white-space: nowrap;
                        " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 20px rgba(255, 107, 107, 0.6)';"
                           onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(255, 107, 107, 0.4)';">
                            🚀 Build Your Agent
                        </button>
                    </a>
                    <p style="font-size: 0.75rem; margin-top: 0.5rem; opacity: 0.9;">
                        Let's build it together!
                    </p>
                </div>
            </div>
            """
        )

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown(
                """
                ### Exchange Rate Assistant

                Ask me anything about currency exchange rates!
                """
            )

            chat_interface = gr.ChatInterface(
                fn=chat,
                examples=[
                    "How much is 100 USD in EUR?",
                    "Convert 1000 JPY to USD",
                    "What is the rate for GBP to AUD today?",
                ],
                type="messages",
                chatbot=gr.Chatbot(
                    height=500,
                    show_copy_button=True,
                    avatar_images=(
                        None,
                        "https://em-content.zobj.net/source/twitter/376/robot_1f916.png",
                    ),
                ),
            )

    gr.HTML(
        """
        <footer>
            <p>Built with ❤️ by <a href="https://github.com/mahimairaja" target="_blank">mahimairaja</a></p>
        </footer>
        """
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
