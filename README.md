# Flowise FastAPI Backend

A powerful, modular FastAPI-based backend for building AI/LLM workflows with a visual interface, inspired by Flowise but built with a focus on developer experience and extensibility.

## 🚀 Features

- **Standardized Node Architecture**: Three-tier node system (Provider, Processor, Terminator)
- **Dynamic Node Discovery**: Automatic detection and registration of new nodes
- **LangChain Integration**: Full compatibility with LangChain ecosystem
- **Modular Design**: Easy to extend with custom nodes
- **Type-Safe**: Built with Pydantic for robust data validation
- **RESTful API**: Clean, documented endpoints for frontend integration

## 📁 Project Structure

```
flowise-fastapi/
├── api/                    # FastAPI routes and schemas
│   ├── routers/           # API route handlers
│   └── schemas.py         # Pydantic models
├── core/                  # Core system components
│   ├── config.py          # Configuration settings
│   ├── node_discovery.py  # Automatic node discovery
│   └── workflow_runner.py # Workflow execution engine
├── nodes/                 # Node implementations
│   ├── base.py           # Base node classes
│   ├── llms/             # Language models
│   ├── tools/            # External tools
│   ├── agents/           # AI agents
│   ├── memory/           # Conversation memory
│   ├── prompts/          # Prompt templates
│   ├── output_parsers/   # Output formatting
│   ├── document_loaders/ # Document processing
│   └── retrievers/       # Information retrieval
├── main.py               # FastAPI application entry point
├── requirements.txt      # Python dependencies
└── readme-gemini.md      # Detailed project memory/documentation
```



3. **Set up environment variables:**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   export GOOGLE_API_KEY="your-google-api-key"  # Optional, for Gemini
   export TAVILY_API_KEY="your-tavily-api-key"  # Optional, for Tavily search
   export LANGCHAIN_API_KEY="your-langchain-api-key"  # Optional, for LangSmith tracing
   ```

## 🚀 Quick Start

1. **Start the server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Visit the API documentation:**
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

3. **List available nodes:**
   ```bash
   curl http://localhost:8000/api/v1/nodes
   ```

## 📊 Available Nodes

### Provider Nodes (Create LangChain objects)
- **OpenAIChat**: OpenAI GPT models
- **TavilySearch**: Web search via Tavily API
- **PromptTemplate**: Chat prompt templates
- **AgentPrompt**: ReAct agent prompts
- **ConversationMemory**: Conversation buffer memory
- **PDFLoader**: PDF document loader

### Processor Nodes (Combine multiple objects)
- **ReactAgent**: ReAct reasoning agent
- **ChromaRetriever**: Vector store retrieval

### Terminator Nodes (Process outputs)
- **StringOutputParser**: Basic string output
- **PydanticOutputParser**: Structured output parsing

## 🔧 API Endpoints

### Nodes
- `GET /api/v1/nodes` - List all available nodes
- `GET /api/v1/nodes/{node_name}` - Get specific node details

### Workflows
- `POST /api/v1/workflows/execute` - Execute a workflow

### Example Workflow Execution
```json
{
  "workflow": {
    "id": "example-workflow",
    "name": "Simple Chat",
    "nodes": [
      {
        "id": "llm-1",
        "type": "OpenAIChat",
        "data": {
          "inputs": {
            "model_name": "gpt-4o-mini",
            "temperature": 0.7
          }
        }
      }
    ],
    "edges": []
  },
  "input": {
    "input": "Hello, how are you?"
  }
}
```



1. **Provider Node Example:**
```python
from nodes.base import ProviderNode, NodeInput, NodeType
from langchain_core.runnables import Runnable

class MyCustomNode(ProviderNode):
    _metadatas = {
        "name": "MyCustomNode",
        "description": "Description of what this node does",
        "node_type": NodeType.PROVIDER,
        "inputs": [
            NodeInput(
                name="param1",
                type="string",
                description="Parameter description",
                required=True
            )
        ]
    }
    
    def _execute(self, param1: str = None) -> Runnable:
        # Your implementation here
        return your_langchain_object
```

2. **Place the file in the appropriate `nodes/` subdirectory**
3. **Restart the server** - the node will be automatically discovered

## 🔍 Node Types

- **ProviderNode**: Creates LangChain objects from scratch (LLMs, Tools, Prompts)
- **ProcessorNode**: Combines multiple LangChain objects (Agents, Chains)
- **TerminatorNode**: Processes final outputs (Parsers, Formatters)
