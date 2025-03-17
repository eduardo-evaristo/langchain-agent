# LangChain Agent

This project demonstrates the use of LangChain to create an agent that can browse the web, search for news, and find images based on user queries. The agent utilizes various tools and APIs to provide comprehensive responses. This agent is necessary because we have a project where a simple LLM wouldn't suffice.

## Features

- **Web Search**: Search the web for general information.
- **News Search**: Search for the latest news articles.
- **Image Search**: Search for images related to a given query.

## Requirements

- Python 3.8+
- A Serper API key
- A Google GEMINI API key

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/langchain.git
   cd langchain
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory of the project and add your Serper API key and Google GEMINI API key:
   ```env
   SERPER_DEV_API_KEY=your_serper_api_key
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

## Usage

To run the agent, use the following command:

```sh
python agent.py "Your query here"
```

The agent will respond in Brazilian Portuguese, providing relevant information based on the query.

You can change the `SystemMessage` to have the LLM reply according to your needs. Additionally, you can create new tools to extend the agent's capabilities.

## Contributing

To create a new tool, follow these steps:

1. **Create a new branch**:

   ```sh
   git checkout -b feature/new-tool-branch
   ```

2. **Implement your tool** in the appropriate file.

3. **Commit your changes**:

   ```sh
   git add .
   git commit -m "Add new tool"
   ```

4. **Push the branch** to the repository:

   ```sh
   git push origin feature/new-tool-branch
   ```

5. **Create a pull request** on GitHub to merge your changes into the main branch.

## License

This project is licensed under the MIT License.
