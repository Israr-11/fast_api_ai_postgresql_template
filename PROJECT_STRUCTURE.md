# Chatbot Backend - Project Structure

This project follows a layered architecture designed for building production-ready AI applications using FastAPI, PostgreSQL, RAG, embeddings, and Agentic AI.

---

# Root Structure

```
chatbot_2/
│
├── api/
├── core/
├── db/
├── integrations/
├── middleware/
├── models/
├── repositories/
├── schemas/
├── services/
├── tests/
├── utils/
├── vectorstore/
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# main.py

Application entry point.

Responsibilities:

- Creates FastAPI application
- Registers routers
- Loads configuration
- Starts middleware
- Initializes database connections

---

# api/

Contains all HTTP API endpoints.

```
api/
└── v1/
```

The `v1` folder represents API Version 1.

If breaking changes are introduced later, a `v2` folder can be created while keeping existing clients working.

---

# api/v1/routes/

Defines HTTP endpoints.

Responsibilities:

- URL routing
- HTTP methods
- Calls controllers
- No business logic

Example:

```
POST /chat
GET /health
```

Files:

### chat.py

Chat API endpoints.

### rag.py

Document retrieval endpoints.

### embeddings.py

Embedding creation endpoints.

### health.py

Health check endpoint.

### agents.py

Agent execution endpoints.

---

# api/v1/controllers/

Controllers connect HTTP requests to business logic.

Responsibilities:

- Receive validated request
- Call service layer
- Return formatted response

Files:

### chat_controller.py

Controls chat requests.

### rag_controller.py

Controls RAG requests.

### embedding_controller.py

Controls embedding operations.

### agent_controller.py

Controls AI agent requests.

---

# core/

Application-wide functionality.

## config.py

Loads environment variables and application settings.

Examples:

- Database URL
- Gemini API Key
- Dashguard URL
- Vector DB URL

---

## logging.py

Centralized logging configuration.

---

## exceptions.py

Custom exception classes.

---

## constants.py

Application constants.

Examples:

- Default chunk size
- Maximum tokens
- API limits

---

# services/

Contains all business logic.

Services should NOT know anything about HTTP.

---

# services/chat/

Core chat orchestration.

## chat_service.py

Main entry point for chat processing.

Responsibilities:

- Load conversation history
- Decide whether to call RAG
- Decide whether to call Agent
- Call Gemini
- Save conversation

---

## memory_service.py

Conversation memory management.

Responsibilities:

- Load previous messages
- Maintain conversation history

---

# services/llm/

Large Language Model layer.

---

## gemini_client.py

Wrapper around Gemini API.

Responsibilities:

- Send prompts
- Receive responses

No application logic should exist here.

---

## prompt_builder.py

Creates prompts for Gemini.

---

## response_parser.py

Converts model output into structured responses.

---

# services/rag/

Retrieval-Augmented Generation.

---

## retriever.py

Retrieves documents from vector database.

---

## context_builder.py

Formats retrieved documents into prompt context.

---

## rag_pipeline.py

Coordinates complete RAG flow.

Pipeline:

```
Query
↓
Embedding
↓
Similarity Search
↓
Context Building
↓
Gemini
```

---

# services/embeddings/

Embedding creation.

---

## embedder.py

Generates vector embeddings.

---

## chunking.py

Splits documents into chunks before embedding.

---

# services/agents/

Agent execution layer.

---

## agent_executor.py

Runs agent workflows.

Responsibilities:

- Decide tools
- Execute tools
- Collect observations
- Generate final response

---

## tool_registry.py

Registers available tools.

---

# services/agents/tools/

Contains all tools available to agents.

## web_search.py

Internet search tool.

---

## db_tool.py

Database lookup tool.

---

## rag_tool.py

RAG retrieval tool.

---

# repositories/

Database access layer.

Repositories isolate SQL/database logic from services.

Services never directly query the database.

---

## base.py

Shared repository functionality.

---

## user_repository.py

User CRUD operations.

---

## chat_repository.py

Conversation storage.

---

## document_repository.py

Document storage.

---

## vector_repository.py

Vector database operations.

---

# models/

Database models.

Usually SQLAlchemy models.

Examples:

- User
- Chat
- Documents
- Embeddings

---

# schemas/

Pydantic request/response models.

Responsibilities:

- Request validation
- Response serialization

Files:

- chat_schema.py
- rag_schema.py
- agent_schema.py
- user_schema.py

---

# db/

Database configuration.

---

## session.py

Creates database session.

---

## base.py

Base SQLAlchemy model.

---

## migrations/

Alembic migration scripts.

---

# vectorstore/

Vector database abstraction.

Supports systems such as:

- Qdrant
- Pinecone
- Weaviate

---

## qdrant_client.py

Qdrant connection.

---

## indexer.py

Indexes embeddings.

---

## similarity_search.py

Performs nearest-neighbor searches.

---

# integrations/

External service integrations.

---

## dashguard/

Authentication integration.

### client.py

Dashguard SDK/API wrapper.

---

### auth.py

Authentication helper.

---

### exceptions.py

Dashguard-specific exceptions.

---

## gemini/

### client.py

Low-level Gemini SDK wrapper.

---

# middleware/

Application middleware.

Runs before requests reach the API.

---

## auth.py

Validates Dashguard tokens.

Adds authenticated user information to request.

---

## rate_limit.py

Rate limiting.

---

## logging_middleware.py

Logs requests and responses.

---

# utils/

Reusable helper functions.

---

## text_processing.py

General text utilities.

---

## file_loader.py

Loads documents such as PDF, DOCX, TXT, etc.

---

## helpers.py

Miscellaneous helper functions.

---

# tests/

Automated tests.

Examples:

- test_chat.py
- test_rag.py
- test_agents.py

---

# Dockerfile

Builds application container.

---

# docker-compose.yml

Runs local services.

Examples:

- FastAPI
- PostgreSQL
- Qdrant
- Redis

---

# requirements.txt

Python dependencies.

Generated using:

```
pip freeze > requirements.txt
```

---

# README.md

Project documentation.

Should include:

- Setup
- Installation
- Running locally
- API usage
- Architecture overview

---

# Architecture Flow

```
Client
   │
   ▼
Routes
   │
   ▼
Controllers
   │
   ▼
Services
   │
   ├── Chat
   ├── RAG
   ├── Agents
   └── LLM
   │
   ▼
Repositories
   │
   ▼
PostgreSQL / Vector Database
```

---

# Design Principles

- Thin Routes
- Thin Controllers
- Business Logic in Services
- Database Access through Repositories
- External APIs isolated in Integrations
- Middleware for Authentication & Logging
- Pydantic Schemas for Validation
- Modular and Scalable Architecture