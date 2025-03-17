from browse_tool import browse_text
from browse_images_tool import browse_images
from llm import llm
from langchain.agents import initialize_agent
from langchain_core.messages import HumanMessage, SystemMessage
import sys

messages = [
    SystemMessage(
        'Responda em português brasileiro, seja cordial, porém assertiva e concisa. Não use símbolos como: *, #, " em suas respostas. Quando o usuário pedir-te uma imagem, responda o link da que parecer-te mais pertinente'
    ),
    HumanMessage(sys.argv[1]),
]

# Tools to be used by the agent
tools = [browse_text, browse_images]

# Load the agent with its LLM and its available tools
# verbose needs to be set to True
agent = initialize_agent(
    llm=llm, tools=tools, agent="zero-shot-react-description", verbose=True
)

# agent.run is deprecated
print(agent.invoke(messages))
