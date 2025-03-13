from browse import browse_text
from browse_images_tool import browse_images
from llm import llm
from langchain.agents import initialize_agent

# Tools to be used by the agent
tools = [browse_text, browse_images]

# Load the agent with its LLM and its available tools
# verbose needs to be set to True
agent = initialize_agent(llm=llm, tools=tools, agent='zero-shot-react-description', verbose=True)

# agent.run is deprecated
print(agent.invoke("como ficar pika no valorant"))
