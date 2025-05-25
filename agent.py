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
            'Responda em português brasileiro, seja cordial, porém assertiva e concisa. Não use símbolos como: *, #, " em suas respostas. Quando o usuário pedir-te uma imagem, responda o link da que parecer-te mais pertinente.'
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
    question = request.json["question"]
    weather_info = request.json["weather"]
    question = f"{question}. Informações: {weather_info}"

    # File we got
    image_file = request.files["pic"]
    # Base64'd up version of it
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Prepare prompt
    messages = [
        SystemMessage(
            'Responda em português brasileiro, seja cordial, porém assertiva e concisa. Não use símbolos como: *, #, " em suas respostas. Descreva a imagem que o usuário te enviar e se necessário ou pertinente use as informações que ele te passar.'
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
    return {"response": response}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
