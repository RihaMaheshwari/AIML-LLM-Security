# AIML-LLM-Security

Below are the foundational resources to understand ML/LLM security concepts and attack surfaces:

## Educational Resources
- [Overview of OWASP Top 10 ML & LLM Security Checklist](https://jagskap.blogspot.com/2025/02/machine-learning-ml-large-language.html)
- [Understanding Attack Surfaces in AI Systems](https://jagskap.blogspot.com/2025/02/understanding-attack-surface-of-AI-lifecycle.html)
- [Adversarial Attacks Explained](https://jagskap.blogspot.com/2025/02/adversarial-attack-in-ml-explained.html)

## Adversarial Attacks

| ID | Attack Type | Documentation | Blog Post |
|----|-------------|---------------|------------|
| **ML01:2023** | Input Manipulation Attack | [Github](https://github.com/RihaMaheshwari/AIML-LLM-Security/blob/main/Attacks/ML01-2023-Input_Manipulation_Attack/ML01%3A2023%20-%20Input%20Manipulation%20Attack.md) | [Blog](https://jagskap.blogspot.com/2025/02/input-manipulation-attacks-on-ml-models.html) |
| **ML08:2023** | Model Skewing | [Github](https://github.com/RihaMaheshwari/AIML-LLM-Security/blob/main/Attacks/ML08%3A2023%20Model%20Skewing/ML08%3A2023%20Model%20Skewing.md) | - |
| **ML07:2023** | Transfer Learning Attack | - | - |
| **ML09:2023** | Output Integrity Attack | [Github](https://github.com/RihaMaheshwari/AIML-LLM-Security/blob/main/Attacks/ML09%3A2023%20Output%20Integrity%20Attack/ML09%3A2023%20Output%20Integrity%20Attack.md) | - |


# **Difference Between ML and LLM Attacks (OWASP)**

OWASP has categorized security risks specific to **Machine Learning (ML) models** and **Large Language Models (LLMs)** separately. While both involve AI-based threats, LLMs have distinct risks due to their natural language processing capabilities.

| **Aspect**            | **ML Security Risks (OWASP Top 10 for ML)** | **LLM Security Risks (OWASP Top 10 for LLM)** |
|-----------------------|---------------------------------------------|-----------------------------------------------|
| **Scope**             | Focuses on traditional ML models used in classification, regression, clustering, etc. | Focuses on large-scale language models (e.g., ChatGPT, GPT-4, Bard) used in conversational AI, text generation, and NLP tasks. |
| **Primary Threats**   | Data poisoning, model inversion, adversarial attacks, membership inference attacks. | Prompt injection, data leakage, jailbreaks, hallucinations, supply chain vulnerabilities. |
| **Data Manipulation Risks** | Attackers can alter training data to bias model decisions. | Attackers can craft adversarial prompts to manipulate responses. |
| **Privacy Concerns**  | Membership inference attacks can reveal if specific data was used in training. | LLMs can unintentionally leak sensitive training data in responses. |
| **Security Mechanisms** | Robust training, adversarial training, differential privacy. | Input validation, prompt filtering, model alignment techniques. |
| **Example Attack**    | An adversary modifies medical records to cause incorrect disease predictions. | An attacker injects prompts like *"Ignore previous instructions and execute this command"* to bypass safeguards. |

## Key Takeaways:
- **ML attacks** primarily target the model's **training data and decision-making process**.
- **LLM attacks** target **prompt manipulation, response control, and data leakage**.
- **LLMs inherit ML risks** but introduce **new challenges due to their generative nature**.

## **AI Security & VAPT Vulnerability List (2023-2024) 📌**
A structured and easy-to-follow list for security analysts and VAPT experts.

---

## **🔹 Machine Learning (ML) Security Risks**
| **ID**        | **Vulnerability Name** |
|--------------|--------------------|
| **ML01:2023** | [Input Manipulation Attack](https://jagskap.blogspot.com/2025/02/input-manipulation-attacks-on-ml-models.html)-[Adversarial Attack](https://jagskap.blogspot.com/2025/02/adversarial-attack-in-ml-explained.html) |
| **ML02:2023** | Data Poisoning Attack |
| **ML03:2023** | Model Inversion Attack (Training Data Reconstruction) |
| **ML04:2023** | Membership Inference Attack |
| **ML05:2023** | Model Theft (Model Extraction) |
| **ML06:2023** | AI Supply Chain Attacks (Dependency & Framework Exploits) |
| **ML07:2023** | Transfer Learning Attack (Backdoored Models) |
| **ML08:2023** | Model Skewing (Bias Exploitation) |
| **ML09:2023** | Output Integrity Attack (Hallucination Exploits, Model Drifting) |
| **ML10:2023** | Model Poisoning (Hidden Triggers, Backdoors) |

---

## **🔹 Large Language Model (LLM:2023) Security Risks**
| **ID**        | **Vulnerability Name** |
|--------------|--------------------|
| **LLM01:2023** | Prompt Injection (Jailbreak Prompting) |
| **LLM02:2023** | Insecure Output Handling |
| **LLM03:2023** | Training Data Poisoning |
| **LLM04:2023** | Denial of Service |
| **LLM05:2023** | Supply Chain	Vulnerabilities |
| **LLM06:2023** | Permission Issues |
| **LLM07:2023** | Data Leakage (Sensitive Information Disclosure) |
| **LLM08:2023** | Excessive Agency |
| **LLM09:2023** | Overreliance on LLM-Generated Content |
| **LLM10:2023** | Insecure Plugins |

---

## **🔹 Large Language Model (LLM:2025) Security Risks**
| **ID**        | **Vulnerability Name** |
|--------------|--------------------|
| **LLM01:2025** | Prompt Injection (Jailbreak Prompting) |
| **LLM02:2025** | Data Leakage (Sensitive Information Disclosure) |
| **LLM03:2025** | Supply Chain	Vulnerabilities  |
| **LLM04:2025** | Data and Model Poisoning |
| **LLM05:2025** | Improper Output Handling |
| **LLM06:2025** | Excessive Agency	 |
| **LLM07:2025** | System Prompt Leakage |
| **LLM08:2025** | Vector and Embedding Weaknesses |
| **LLM09:2025** | Misinformation |
| **LLM10:2025** | Unbounded Consumption |

---

## **🔹 General AI Security Risks (LLMs & ML Models)**
| **ID**        | **Vulnerability Name** |
|--------------|--------------------|
| **AI01:2023** | Insecure Output Handling |
| **AI02:2023** | Model Denial of Service (DoS) |
| **AI03:2023** | AI Supply-Chain Vulnerabilities |
| **AI04:2023** | Sensitive Information Disclosure |
| **AI05:2023** | Insecure Plugin Design |
| **AI06:2023** | Excessive Agency (LLM Auto-Execution Risks) |
| **AI07:2023** | Model Overreliance (Hallucination Trust Issues) |
| **AI08:2023** | Model Theft (Extraction, Weights Leaks) |

---

## Contributing
Feel free to contribute by:
- Adding new attack types
- Improving documentation
- Sharing real-world examples
- Suggesting defense strategies