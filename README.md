<div align="center">

# Saurabh Pareek
### AI Systems & Infrastructure

<p>
  My thesis is that the next wave of AI innovation will be unlocked by superior developer infrastructure, not just model scale. I build foundational tools and systems designed to abstract complexity and accelerate the machine learning lifecycle—from autonomous research to production-grade deployment.
</p>

<p>
  <a href="https://www.linkedin.com/in/saurabh-pareek-5b1702331">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  &nbsp;
  <a href="mailto:saurabhpareek228@gmail.com">
    <img src="https://img.shields.io/badge/saurabhpareek228@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
</p>

</div>

---

### ◈ Engineering Philosophy

<table>
  <tr>
    <td valign="top" width="33.33%">
      <h3 align="center">⚡️ Velocity & Iteration</h3>
      <p align="center">Build robust CI/CD pipelines and developer-first tooling to compress the idea-to-deployment cycle and enable rapid, high-quality iteration.</p>
    </td>
    <td valign="top" width="33.33%">
      <h3 align="center">🏗️ Scalable Primitives</h3>
      <p align="center">Design systems as a set of clean, reusable, and scalable components that serve as the fundamental building blocks for complex applications.</p>
    </td>
    <td valign="top" width="33.33%">
      <h3 align="center">🤖 Automate Complexity</h3>
      <p align="center">Abstract away low-level infrastructure and workflow complexity, allowing developers to focus on core business logic and innovation.</p>
    </td>
  </tr>
</table>

---

### ◈ Core Technology Stack

<table>
  <tr>
    <td valign="top"><strong>Languages</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
    </td>
  </tr>
  <tr>
    <td valign="top"><strong>Backend & DevOps</strong></td>
    <td>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
      <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
      <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="GCP"/>
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
    </td>
  </tr>
  <tr>
    <td valign="top"><strong>AI / ML</strong></td>
    <td>
      <img src="https://img.shields.io/badge/LangChain-3D9962?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
      <img src="https://img.shields.io/badge/Vector_Databases-9B59B6?style=for-the-badge&logo=google-cloud-spanner&logoColor=white" alt="Vector DBs"/>
      <img src="https://img.shields.io/badge/Large_Language_Models-FF6F61?style=for-the-badge&logo=openai&logoColor=white" alt="LLMs"/>
    </td>
  </tr>
</table>

---

### ◈ Thesis in Practice: Core Developments

<details open>
<summary><strong>VertexAutoGPT</strong> /// Production-Grade Agentic Workflow Engine</summary>
<br>
An execution engine designed to solve the final-mile problem for autonomous AI: production deployment. It provides core primitives for agentic systems—radically reducing the engineering overhead required to move from prototype to scalable deployment. This is the infrastructure layer for building reliable, task-driven AI.
<br><br>
<strong>Technical Highlights:</strong>
<ul>
  <li><b>Persistent Vector Memory:</b> Integrates FAISS to provide agents with long-term memory, enabling context retention across complex, multi-step tasks.</li>
  <li><b>Dynamic Tool Orchestration:</b> Agents can dynamically select and execute from a suite of external tools (APIs, custom functions) to interact with outside systems.</li>
  <li><b>Cost-Optimized on GCP:</b> Architected for event-driven, serverless execution on Google Cloud to minimize idle resource costs and scale on demand.</li>
</ul>
<p>
  <code>Python</code> ⋅ <code>LangChain</code> ⋅ <code>GCP</code> ⋅ <code>FastAPI</code> ⋅ <code>FAISS</code> ⋅ <code>Llama 2</code>
</p>
</details>

<details>
<summary><strong>Snap2Slides</strong> /// AI-Native Content Transformation Pipeline</summary>
<br>
Targets a high-friction enterprise workflow—transforming unstructured data into communication-ready assets. The system acts as a generative fabric, using a multimodal pipeline to synthesize raw inputs (notes, images) into structured presentations in near real-time. This project validates a core product thesis: that the greatest immediate value of generative AI lies in building intuitive, high-velocity tools for tangible business workflows.
<br><br>
<strong>Technical Highlights:</strong>
<ul>
  <li><b>Multimodal Processing:</b> Leverages the Gemini Vision API to interpret both textual and visual data from a single input source.</li>
  <li><b>Real-Time Streaming:</b> Implements an asynchronous backend to process and stream structured slide content back to the client for a near-instant user experience.</li>
  <li><b>Scalable Data Layer:</b> Built on MongoDB Atlas to handle unstructured document storage and flexible querying for user-generated content.</li>
</ul>
<p>
  <code>Next.js</code> ⋅ <code>TypeScript</code> ⋅ <code>Gemini Vision API</code> ⋅ <code>MongoDB</code> ⋅ <code>Tailwind CSS</code>
</p>
</details>

<details>
<summary><strong>Core Dev Workflow</strong> /// Standardized Infrastructure for Engineering Velocity</summary>
<br>
A prescriptive architecture for CI/CD that serves as the system of record for building and deploying backend services. It eliminates environment drift and compresses the code-to-cloud lifecycle by enforcing containerization and automation. This isn't just a workflow; it's a strategic asset that underpins the ability to ship complex systems reliably and at high velocity.
<br><br>
<strong>Technical Highlights:</strong>
<ul>
  <li><b>Containerized Environments:</b> Uses Docker to ensure perfect environmental parity between local development, testing, and production.</li>
  <li><b>Declarative CI/CD Pipelines:</b> Implements CI/CD using GitHub Actions workflows, defining the entire build-test-deploy process as code.</li>
  <li><b>Reproducible Builds:</b> Creates a locked, version-controlled process that guarantees consistent and reliable artifacts for every deployment.</li>
</ul>
<p>
  <code>Python</code> ⋅ <code>Docker</code> ⋅ <code>GitHub Actions</code> ⋅ <code>Workflow Orchestration</code>
</p>
</details>

---

### ◈ Signal & Analytics

<table>
  <tr>
    <td width="55%" valign="top">
      <a href="https://github.com/SaurabhCodesAI">
        <img src="https://github-readme-stats.vercel.app/api?username=SaurabhCodesAI&show_icons=true&theme=aura_dark&count_private=true&hide_border=true&border_radius=10" alt="GitHub Stats"/>
      </a>
    </td>
    <td width="45%" valign="top">
      <p align="center"><strong>Language Proficiency</strong></p>
      <p align="center">
        <img src="https://img.shields.io/badge/Python-75%25-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
        <img src="https://img.shields.io/badge/TypeScript-15%25-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript"/>
        <img src="https://img.shields.io/badge/Shell-10%25-89E051?style=for-the-badge&logo=gnubash&logoColor=white" alt="Shell"/>
      </p>
    </td>
  </tr>
</table>

---
