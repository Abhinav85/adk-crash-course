# ADK Crash Course - Complete Course Documentation

This repository provides a comprehensive crash course on building AI agents using the Agent Development Kit (ADK). The course progresses from basic agent concepts to advanced multi-agent architectures and workflow patterns.

---

## Table of Contents

1. [Basic Agent](#1-basic-agent)
2. [Tool Agents](#2-tool-agents)
3. [LiteLLM Integration](#3-litellm-integration)
4. [Structured Output](#4-structured-output)
5. [Sessions and State Management](#5-sessions-and-state-management)
6. [Persistent Storage](#6-persistent-storage)
7. [Multi-Agent Architecture (Manager Pattern)](#7-multi-agent-architecture-manager-pattern)
8. [Stateful Multi-Agent Systems](#8-stateful-multi-agent-systems)
9. [Callbacks](#9-callbacks)
10. [Sequential Agents](#10-sequential-agents)
11. [Parallel Agents](#11-parallel-agents)
12. [Loop Agents](#12-loop-agents)

---

## 1. Basic Agent

**Purpose**: Introduces the fundamental concept of agents in ADK and how to create simple agents that interact with users.

**What you'll learn**:
- Creating your first ADK agent
- Basic agent structure and components
- LLM integration for simple tasks
- Handling user prompts and responses

**Key Files**:
- `greeting_agent/agent.py` - A basic greeting agent example

**Use Case**: Your starting point for learning how to build agents. Understanding the core agent concept before moving to more complex patterns.

---

## 2. Tool Agents

**Purpose**: Demonstrates how agents use external tools (APIs, utilities) to accomplish tasks.

**What you'll learn**:
- How to define and register tools for agents
- How agents call external tools programmatically
- The relationship between agent logic and tool execution
- Error handling with tool responses

**Key Files**:
- `tool_agent/agent.py` - Main tool agent example
- Tool definition patterns

**Use Case**: When your agent needs to interact with external systems, databases, APIs, or perform actions beyond pure text generation.

---

## 3. LiteLLM Integration

**Purpose**: Shows how to use LiteLLM as a unified API for different LLM providers, enabling multi-model experimentation.

**What you'll learn**:
- Integrating multiple LLM providers through a single interface
- Cost-effective experimentation with different models
- Switching between open-source and commercial models at runtime
- Example: Dad Joke Agent using various LLMs to generate jokes

**Key Files**:
- `dad_joke_agent/agent.py` - Demonstrates LiteLLM usage

**Use Case**: When you want flexibility in model selection or want to experiment with different LLM providers without code changes.

---

## 4. Structured Output Agents

**Purpose**: Teaches agents to produce consistent, formatted responses (typically JSON).

**What you'll learn**:
- Generating structured data (JSON) from LLMs reliably
- Schema definitions for output format validation
- Handling unexpected model outputs
- Best practices for consistent API-style responses

**Key Files**:
- `email_agent/agent.py` - Generates well-formatted email structures

**Use Case**: When your agent needs to produce deterministic outputs that can be parsed programmatically (e.g., JSON APIs, structured data for other agents).

---

## 5. Sessions and State Management

**Purpose**: Demonstrates how agents maintain context across multiple interactions through session-based state.

**What you'll learn**:
- Session-based conversation management
- Persistent state between agent calls
- How to access and update state across requests
- Contextual responses based on conversation history

**Key Files**:
- `basic_stateful_session.py` - Core state management utilities
- `question_answering_agent/agent.py` - Example with conversation history

**Use Case**: When your agent needs to remember information from previous interactions (e.g., shopping assistants, customer support bots).

---

## 6. Persistent Storage

**Purpose**: Shows how to save agent data to disk for continued conversations and state persistence.

**What you'll learn**:
- SQLite database integration with ADK agents
- Reading and writing agent output to storage
- Retrieving stored data for continued sessions
- Data persistence across application restarts

**Key Files**:
- `memory_agent/agent.py` - Example agent using persistent storage
- Database utilities (`utils.py`)

**Use Case**: When you need long-term memory for agents (e.g., personal assistants, knowledge bases) or when state needs to survive server restarts.

---

## 7. Multi-Agent Architecture (Manager Pattern)

**Purpose**: Introduces the manager-agent pattern for coordinating multiple specialized sub-agents.

**What you'll learn**:
- Hierarchical agent structures with managers delegating tasks
- Creating specialized sub-agents with distinct responsibilities
- Manager orchestrating independent sub-agents
- Example: Manager with sub-agents (funny_nerd, news_analyst, stock_analyst) each providing different expertise

**Key Files**:
- `manager/agent.py` - Main manager agent
- Sub-agent implementations (`funny_nerd`, `news_analyst`, `stock_analyst`)
- Tools for sub-agent interaction

**Use Case**: When you need multiple specialized agents working together under coordination (e.g., research teams, analytical platforms).

---

## 8. Stateful Multi-Agent Systems

**Purpose**: Demonstrates complex multi-agent systems where multiple specialized agents collaborate and share/modify a common data structure.

**What you'll learn**:
- Agents that work collaboratively to modify shared state
- Complex business workflows with multiple specialized agents
- How sub-agents interact through a shared schema
- Example: Customer Service Agent with sub-agents (order, policy, sales, course_support) handling different aspects of customer requests

**Key Files**:
- `customer_service_agent/agent.py` - Main agent orchestrating the workflow
- Sub-agent implementations (`order`, `policy`, `sales`, `course_support`)
- Shared state management across agents

**Use Case**: When you need multiple specialized experts collaborating to handle complex, multi-step workflows (e.g., order fulfillment systems, knowledge management platforms).

---

## 9. Callbacks

**Purpose**: Teaches how to handle events asynchronously in agent systems using before/after callbacks.

**What you'll learn**:
- Before callbacks: Run operations before model calls (logging, monitoring)
- After callbacks: Run operations after model responses (post-processing, validation)
- Model-level vs Tool-level callback patterns
- Creating custom agents that use callbacks internally

**Key Files**:
- `before_after_agent/agent.py` - Agent using callbacks for flow control
- `before_after_model/agent.py` - Before/After callbacks with model integration
- `before_after_tool/agent.py` - Callbacks around tool execution

**Use Case**: For monitoring, logging, validation, or any operation that needs to happen before/after agent operations (e.g., audit trails, A/B testing, rate limiting).

---

## 10. Sequential Agents

**Purpose**: Demonstrates ordered workflows where agents execute one after another, with each step depending on the previous output.

**What you'll learn**:
- Sequential agent pipelines executing in strict order
- Data flow between steps (validation → scoring → recommendation)
- How to chain multiple processing stages
- Example: Lead Qualification Pipeline (validate → score → recommend action)

**Key Files**:
- `lead_qualification_agent/agent.py` - Main sequential pipeline
- Sub-agents (`validator`, `scorer`, `recommender`)

**Use Case**: When you need deterministic, step-by-step workflows where each step builds on the previous output (e.g., data processing pipelines, review systems).

---

## 11. Parallel Agents

**Purpose**: Shows concurrent execution patterns for independent tasks to improve performance.

**What you'll learn**:
- Running agents simultaneously for speed improvements
- Independent sub-agents that don't share state during execution
- Combining parallel and sequential workflows (hybrid patterns)
- Example: System Monitor (CPU, Memory, Disk gathered concurrently then synthesized)

**Key Files**:
- `system_monitor_agent/agent.py` - Parallel agent example
- Sub-agents (`cpu_info`, `memory_info`, `disk_info`) + synthesizer

**Use Case**: When you need to complete multiple independent tasks quickly without waiting for them in sequence (e.g., gathering metrics from multiple sources, parallel web research).

---

## 12. Loop Agents

**Purpose**: Demonstrates iterative refinement and repeated execution patterns with exit conditions.

**What you'll learn**:
- Loop-based workflows that continue until a condition is met
- Tools to control loop termination (e.g., `exit_loop` tool)
- Feedback-driven improvement cycles
- Example: LinkedIn Post Generator (generate → review → refine iteratively)

**Key Files**:
- `linkedin_post_agent/agent.py` - Sequential agent with embedded loop
- Sub-agents (`post_generator`, `post_refiner`, `post_reviewer`)

**Use Case**: When you need iterative processes that improve over time or repeat until quality requirements are met (e.g., content refinement, optimization loops).

---

## Learning Path Overview

| Level | Focus Area | Key Concept | Example Use Case |
|-------|-----------|-------------|------------------|
| **Level 1** | Foundations | Single agent basics | Greeting agents, simple task completion |
| **Level 2** | Integration | Tools + Multiple models | Tool-using agents, API interactions |
| **Level 3** | State & Persistence | Sessions, Database storage | Chatbots with memory, personal assistants |
| **Level 4** | Architecture | Manager pattern, multi-agent coordination | Research platforms, analytics systems |
| **Level 5** | Workflow Patterns | Sequential/Parallel/Loop agents | Data pipelines, production workflows |
| **Level 6** | Advanced Patterns | Callbacks + Complex orchestration | Production-grade agent systems |

---

## Installation & Setup

### Prerequisites
- Python 3.10+ 
- Virtual environment support
- Git (for cloning, if needed)

### Quick Start
```bash
# Navigate to project root
cd /path/to/adk-crash-course

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/  # macOS/Linux
# or on Windows:
#.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run an example
cd 1-basic-agent && adk web
```

---

## Resources

### Documentation Links
- [ADK Official Documentation](https://google.github.io/adk-docs/)
- [ADK Sequential Agents](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/)
- [ADK Parallel Agents](https://google.github.io/adk-docs/agents/workflow-agents/parallel-agents/)
- [ADK Loop Agents](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/)

### Code Repositories
Each folder contains a self-contained example you can run locally:
- All examples use `adk web` to launch the interactive web UI
- Check individual `README.md` files for specific setup instructions

---

## Contributing

This is an educational repository demonstrating ADK patterns. Feel free to experiment with the examples, fork this repository, and create your own agent implementations using these patterns as a starting point.