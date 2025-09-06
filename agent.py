from browse_tool import browse_text
from browse_images_tool import browse_images
from browse_news_tool import browse_news
from llm import llm
from langchain.agents import initialize_agent
from langchain_core.messages import HumanMessage, SystemMessage
import sys
from flask import Flask, request
from flask_cors import CORS
import base64

app = Flask(__name__)

# Configure CORS later, if needed
CORS(app)

# Tools to be used by the agent
tools = [browse_text, browse_images, browse_news]

# Load the agent with its LLM and its available tools
# verbose needs to be set to True
agent = initialize_agent(
    llm=llm,
    tools=tools,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True,
)


@app.route("/agent", methods=["POST"])
def call_agent():
    question = request.json["question"]
    messages = [
        SystemMessage(
            "Responda sempre em português brasileiro, com cordialidade, assertividade e concisão. Evite o uso de símbolos como asterisco (*) — inclusive para formatação em negrito — e jogo da velha (#). Quando o usuário solicitar uma imagem, responda somente com o link da imagem mais pertinente, sem qualquer texto adicional."
        ),
        HumanMessage(question),
    ]
    response = agent.invoke(messages)
    if isinstance(response, dict) and "output" in response:
        return {"response": response["output"]}  # Access as a dictionary
    elif hasattr(response, "output"):
        return {"response": response.output}  # Access as an attribute
    else:
        return {
            "error": "Unexpected response format",
            "raw_response": str(response),
        }, 500


@app.route("/picture", methods=["POST"])
def describe_image():
    question = request.form["question"]
    weather_info = request.form["weather"]
    question = f"{question}. Informações: {weather_info}"

    # File we got
    image_file = request.files["pic"]
    # Base64'd up version of it
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Prepare prompt
    messages = [
        SystemMessage(
            'Responda em português brasileiro com cordialidade, assertividade e concisão. Analise a imagem enviada pelo usuário com base no conteúdo visual. Use informações contextuais adicionais apenas se forem realmente necessárias para enriquecer a análise, e sempre de forma sutil e breve, sem citá-las diretamente ou de maneira extensa. Evite o uso de símbolos como: * (asterisco), # (jogo da velha) e " (aspas) em suas respostas.'
        ),
        HumanMessage(
            content=[
                {"type": "text", "text": question},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                },
            ]
        ),
    ]

    # Get response from Gemini
    response = llm.invoke(messages)
    print(response)
    return {"response": response.text()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
