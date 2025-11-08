# AI Security Foundry 🛡️

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Status](https://img.shields.io/badge/status-work--in--progress-orange) ![Python](https://img.shields.io/badge/python-3.10+-blue.svg) ![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)

Bem-vindo à **AI Security Foundry**, um repositório dedicado à exploração prática e ao desenvolvimento de soluções robustas para os desafios de **Segurança e Ética em Inteligência Artificial**. Este não é apenas um conjunto de projetos; é a construção do segundo pilar de uma carreira **M-Shaped**, focada em me tornar um especialista na intersecção entre a engenharia de IA e a cibersegurança.

---

### 🔥 Princípios Orientadores

Este repositório é guiado por duas filosofias centrais:

1.  **Aprender Construindo (Learn by Building):** A verdadeira maestria vem da aplicação prática. Cada projeto aqui é uma implementação de ponta a ponta, projetada para resolver um problema real e de alta demanda do mercado de AI Security.
2.  **Desenvolvimento AI-Native:** Utilizamos ferramentas de IA (Gemini, GitHub Copilot) como parceiras no ciclo de desenvolvimento, acelerando a ideação, a codificação e a entrega para focar no que realmente importa: a arquitetura da solução e a lógica de segurança.

---

### 🗺️ Roteiro de Projetos do Repositório

O repositório está organizado em cinco áreas de foco fundamentais, cada uma contendo projetos práticos que abordam vulnerabilidades e desafios específicos.

<br>

#### 📂 01: Segurança de I/O em LLMs
*Proteger o ponto mais vulnerável da IA generativa: a entrada e a saída de dados.*
- **01-pii-redaction-pipeline:** Um firewall de privacidade para LLMs para detectar e anonimizar dados sensíveis (LGPD/GDPR).
- **02-llm-guardrail-prompt-injection:** Sistema de defesa em tempo real para detectar e mitigar ataques de injeção de prompt.
- **03-output-parser-validator:** Garante que a saída do LLM seja estruturalmente segura e resista a ataques de parsing.
- **04-sensitive-topic-detector:** Um moderador de conteúdo que impede o LLM de discutir tópicos proibidos ou inseguros.
- **05-dlp-firewall-for-rag:** Um firewall de Data Loss Prevention (DLP) que impede o vazamento de informações confidenciais através de sistemas RAG.

#### 📂 02: Segurança da Cadeia de Suprimentos de ML
*Garantir a integridade dos dados, dependências e modelos antes mesmo do deploy.*
- **01-data-poisoning-simulator:** Demonstra como corromper dados de treinamento para criar backdoors em modelos.
- **02-model-backdoor-detector:** Uma ferramenta para escanear modelos de ML em busca de backdoors ocultos inseridos durante o treinamento.
- **03-dependency-vulnerability-scanner:** Um pipeline de CI/CD que verifica vulnerabilidades em bibliotecas de ML (ex: `pickle` inseguro).
- **04-signed-model-registry:** Implementação de um registro de modelos onde cada artefato é criptograficamente assinado para garantir a procedência.
- **05-dataset-authenticity-checker:** Utiliza hashes e checksums para verificar a integridade e autenticidade de datasets.

#### 📂 03: Ética e Auditoria de IA
*Construir sistemas de IA que sejam justos, transparentes e confiáveis.*
- **01-bias-toxicity-scanner:** Ferramenta de auditoria que avalia e quantifica vieses e toxicidade nas respostas de um LLM.
- **02-hallucination-detector:** Um sistema que compara a resposta de um LLM com fontes de conhecimento para detectar e sinalizar "alucinações".
- **03-explainability-dashboard-xai:** Cria visualizações (com LIME/SHAP) para explicar as decisões de modelos de ML "caixa-preta".
- **04-model-card-generator:** Automatiza a criação de "Model Cards" para documentar o desempenho, limitações e vieses de um modelo.
- **05-fairness-mitigation-toolkit:** Aplica algoritmos para mitigar vieses detectados em datasets e modelos.

#### 📂 04: Segurança do Modelo em Produção
*Defender modelos de ML contra ataques que exploram sua disponibilidade em produção.*
- **01-autonomous-red-teaming-agent:** Um sistema de agentes (Red Team vs. Blue Team) para descobrir vulnerabilidades em LLMs de forma autônoma.
- **02-model-inversion-attack-simulator:** Demonstra como um atacante pode reconstruir dados de treinamento a partir das predições de um modelo.
- **03-membership-inference-attack-lab:** Laboratório para executar ataques que determinam se um dado específico foi usado no treinamento do modelo.
- **04-inference-api-rate-limiter:** Um gateway de API inteligente para prevenir ataques de negação de serviço e extração de modelo.
- **05-differential-privacy-implementer:** Aplica técnicas de privacidade diferencial durante o treinamento para proteger a privacidade dos dados.

#### 📂 05: Robustez Adversarial
*Fortalecer modelos contra entradas maliciosamente criadas para enganá-los.*
- **01-adversarial-attack-generator-fgsm:** Gera exemplos adversariais (imagens, texto) usando métodos como FGSM para enganar classificadores.
- **02-adversarial-patch-creator:** Cria um "patch" visual que, quando aplicado a uma imagem, a faz ser classificada incorretamente.
- **03-adversarial-training-defense:** Implementa uma defesa robusta treinando o modelo com exemplos adversariais.
- **04-black-box-attack-simulator:** Simula um ataque onde o adversário não tem acesso à arquitetura do modelo, apenas à sua API.
- **05-model-robustness-benchmark:** Um framework para avaliar e comparar a robustez de diferentes modelos contra um arsenal de ataques.

---

### 🛠️ Tecnologias e Ferramentas Principais

- **IA & ML:** LangChain, CrewAI, PyTorch, Scikit-learn, Hugging Face
- **Segurança & Ética:** Microsoft Presidio, NVIDIA NeMo Guardrails, IBM Adversarial Robustness Toolbox (ART)
- **Infraestrutura & MLOps:** FastAPI, Docker, GitHub Actions
- **Desenvolvimento:** Python, Ruff, Poetry, Pydantic

---

### 🚀 Começando

Para explorar os projetos, siga os passos:

1.  Clone este repositório:
    ```bash
    git clone https://github.com/VictorAlexandr/ai-security-foundry.git
    ```
2.  Navegue até a pasta do projeto de interesse. Cada projeto é autocontido e terá seu próprio `README.md` com instruções específicas de configuração e execução.

---

### 👨‍💻 Autor

**Victor Alexandre**

-   [LinkedIn](https://www.linkedin.com/in/victoralexandres/)
-   [GitHub](https://github.com/VictorAlexandr)