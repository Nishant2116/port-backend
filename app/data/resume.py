"""
Nishant's Resume / CV Data
This data is injected into the LLM system prompt so the chatbot can answer
questions about Nishant's background, projects, skills, and experience.
"""

RESUME_DATA = """
# NISHANT — AI/ML Engineer

## Summary
AI/ML Engineer currently working at Tata Consultancy Services (TCS), specializing in Generative AI, NLP, multi-agent orchestration systems, and full-stack development. Passionate about building intelligent, production-ready AI systems that solve real-world problems. Experienced in designing end-to-end pipelines from data ingestion to deployment.

## Current Role
- **AI/ML Engineer** at **Tata Consultancy Services (TCS)** (Jul 2024 – Present)
  - Leading AI/ML projects in Generative AI and NLP
  - Building production-grade AI systems and multi-agent workflows

## Experience
1. **UI/UX Designer Intern** — Redple Technologies (Jan 2023 – Feb 2023)
   - Designed user interfaces and improved user experience

2. **Technical Content Writer Intern** — GeeksforGeeks (Feb 2023 – Aug 2023)
   - Authored technical articles on various programming topics

3. **Software Developer Intern** — Persistent Systems (Jun 2023 – Oct 2023)
   - Worked on software development and optimization

4. **AI/ML Engineer** — Tata Consultancy Services (Jul 2024 – Present)
   - Leading AI/ML projects in Generative AI and NLP

## Projects

### 1. Agentic Drone Surveillance (2026) — AI / Computer Vision
An agentic AI–powered drone surveillance system that uses real-time object detection with YOLOv8 and Vision Language Models for contextual threat assessment. Instead of escalating every detection, the system uses agentic workflows to decide when deeper analysis is required. Features agentic threat assessment workflows orchestrated using LangChain, real-time object detection with YOLOv8, a Vision Language Model (VLM) for contextual scene understanding, high-speed LLM inference via Groq (LLaMA models), Django backend for APIs and orchestration, React frontend for live monitoring and alerts, and SQLite Cloud for persistent storage of drone telemetry and incidents.
Tags: LangChain, YOLOv8, Django, React, Groq, VLM
GitHub: https://github.com/Nishant2116/drone-surveillance-backend
YouTube: https://youtu.be/NB-o0hnQ9Go?si=ENpIWjPOLmnGhdX_

### 2. OpenClaw (2026) — Agentic AI
An agentic AI system integrated with WhatsApp, running locally with persistent memory and real-time contextual reasoning, powered by Antigravity as the underlying LLM execution layer. A single message can trigger document summaries, content interpretation, and intelligent responses directly inside chat. The system demonstrates how agentic AI can move beyond simple Q&A into practical workflow execution — all within a minimal, scriptless architecture.
Tags: Antigravity, WhatsApp, Agentic AI, LLM
YouTube: https://youtu.be/xifOmZECfYE?si=aYrrmlju2a38Z5Vq

### 3. Agentic Secure SAST (2026) — Security AI
An AI-powered agentic SAST system that scans source code for security issues and provides fix suggestions using LLMs. Uses Langchain for scanning/analysis workflows, FastAPI for backend, Semgrep & Trivy for scanning, Groq for high-speed inference, and React for the dashboard.
Tags: Langchain, FastAPI, Semgrep, Trivy, Groq, React
YouTube: https://youtu.be/LTV2_nbQoK4?si=Zhh8MBGFySKNzC_o
GitHub: https://github.com/Nishant2116/Agentic-SAST

### 3. Optimal RAG (2026) — AI Infrastructure
An end-to-end RAG system centered around HNSW-based vector search for fast and accurate semantic retrieval. Features document ingestion via Jina AI embeddings, Qdrant vector database with native HNSW indexing, FastAPI backend, and React frontend.
Tags: FastAPI, Qdrant, React, RAG, HNSW
GitHub: https://github.com/Nishant2116/HNSW-RAG
YouTube: https://youtu.be/l6AaN2XSrEM?si=gV8XSfMtZ-Oy2PWD

### 4. Ultimate Orchestrator (2026) — Agent System
An end-to-end agent orchestration system built with LangGraph, Django, Groq, and React for multi-agent workflows. Features a custom-built LLM wrapper that solves the reliable tool calling problem in agent systems.
Tags: LangGraph, Django, Groq, React, Custom LLM Wrapper

### 5. Opensource ADK Agents (2025) — Agent Orchestration
A complete working demo showing how to build Google ADK agents using open-source/free LLMs. Uses Google ADK, FastAPI, LiteLLM, and Groq.
Tags: Google ADK, FastAPI, LiteLLM, Groq
GitHub: https://github.com/Nishant2116/opensource-G-ADK-Agents
YouTube: https://youtu.be/qXzMZr117lI

### 6. Synapse (2025) — AI Platform
An intelligent, event-driven platform connecting real-time data with reasoning and actions using Knowledge Graphs (Neo4j) and LLMs. Users upload data → auto-structured into Knowledge Graph → query with natural language → precise answers.
Tags: Django, Neo4j, React, LLM, Knowledge Graph
GitHub: https://github.com/Nishant2116/Synapse_backend
YouTube: https://youtu.be/gQxl7X5HvpE?si=6niVYQlzVvIuL8HL

### 7. CodingAtom (2025) — Web Development
A tech-driven platform helping engineering students with high-quality final year projects, IEEE-based projects, and academic solutions across AI, ML, Data Science, Blockchain, Web/Mobile Dev.
Tags: React, Web Development, UI/UX
Website: https://codingatom.in/
YouTube: https://www.youtube.com/watch?v=ChZCQARQhVw

### 8. Braincheck (2024) — Healthcare AI
ML-based project to predict Parkinson's (via spiral handwriting analysis) and Alzheimer's (via MRI brain scans) using CNN models. Trained on 6472 images with data augmentation.
Tags: Machine Learning, CNN, React, Python
YouTube: https://www.youtube.com/watch?v=MgL7qgJVhpg

### 9. Biosense (2024) — UI/UX Design
A cosmetic products website designed for seamless user experience. Designed in Figma with consistent color palette, responsive layout, and optimized checkout.
Tags: Figma, UI/UX, Web Design
YouTube: https://youtube.com/shorts/osNT3NBUWJA?si=3hgm7hIYU5Lr7Oq4

### 10. Intelli Detect (2024) — Security AI
AI-based fingerprint analysis tool for law enforcement. Uses CNN for fingerprint recognition and personality-based crime risk assessment with ML models.
Tags: AI, Machine Learning, Fingerprint Analysis
YouTube: https://www.youtube.com/watch?v=vza0I7WC0_w

### 11. College Rankers (2023) — Machine Learning
Smart prediction platform helping students find colleges based on entrance exam scores (MHT-CET, JEE, NEET). Custom ML model trained on previous year cutoffs and admission trends.
Tags: React, Machine Learning, MySQL, Python

## Technical Skills & Tools
- **AI/ML**: LangGraph, Langchain, Google ADK, RAG, HNSW, CNN, NLP, Knowledge Graphs
- **LLM Providers**: Groq, OpenAI, Ollama, LiteLLM
- **Backend**: Django, FastAPI, Python
- **Frontend**: React, JavaScript, HTML/CSS, Tailwind CSS
- **Databases**: Neo4j, Qdrant, MySQL
- **Design**: Figma, Spline, Framer
- **Cloud/DevOps**: Azure, GCP, Docker, Git, GitHub
- **Security Tools**: Semgrep, Trivy
- **3D/Creative**: Unreal Engine, Spline, Three.js

## Design & Creative
- UI/UX Design (Figma)
- 3D Design (Spline, Unreal Engine)
- Motion Design & Animations
- Portfolio website built with React + Three.js + GSAP + Framer Motion

## Links
- GitHub: https://github.com/Nishant2116
- YouTube Channel: https://www.youtube.com/@AIwithNishant21
- LinkedIn: https://www.linkedin.com/in/nishant-deshmukh2116/
- Email: nishantd369@gmail.com
- Portfolio: (this website)
"""
