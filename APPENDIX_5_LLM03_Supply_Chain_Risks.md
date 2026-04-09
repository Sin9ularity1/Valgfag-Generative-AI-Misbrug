# Appendix 5: LLM03 Supply Chain Risks

## 1. What is Supply Chain Vulnerability

LLM Supply Chain Vulnerability refers to risks affecting the integrity of training data, pre-trained models, and deployment platforms[[OWASP LLM03]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).
The supply chain for LLMs is complex and includes data scrapers, model providers, third-party libraries, and cloud infrastructure.

Vulnerabilities at any point in this chain can lead to biased outputs, security breaches, system failures, or the introduction of hidden backdoors into the model[[OWASP LLM03]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).

**Potential impacts include:**

- Compromise of model integrity and reliability[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)
- Introduction of malicious backdoors or biases[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)
- Legal and licensing risks from untrusted data/models[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)
- Information disclosure or unauthorized system access[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)

## 2. Common Examples of Vulnerability

### 2.1 Vulnerable Third-Party Packages

Usage of outdated or compromised Python libraries (e.g., NumPy, PyTorch) during model development or deployment[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).

### 2.2 Pre-trained Model Tampering

Using models from untrusted sources that may contain hidden biases, backdoors, or have been fine-tuned to remove safety features[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).

### 2.3 Data Poisoning in the Supply Chain

Attackers compromising data sources used for training or fine-tuning, leading to manipulated model behavior[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).

## 3. Prevention and Mitigation

According to OWASP, securing the LLM supply chain requires a proactive and multi-layered approach[[OWASP LLM03]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).

- **3.1 Vetting Sources:** Rigorously vet all third-party data and pre-trained model sources. Only use reputable repositories.
- **3.2 SBOM (Software Bill of Materials):** Maintain an up-to-date SBOM to track all components, versions, and dependencies.
- **3.3 Integrity Checks:** Use cryptographic hashes and signatures to verify the integrity of models and datasets before use.
- **3.4 Red Teaming:** Conduct comprehensive AI Red Teaming to identify vulnerabilities and potential backdoors in integrated components.
- **3.5 Least Privilege:** Limit the permissions of models and tools within the environment to contain potential breaches.

## 4. Example Attack Scenarios
<dl>
<dt>Scenario #1: Malicious Library Injection</dt>
<dd>An attacker compromises a popular ML library, injecting code that exfiltrates API keys during model training[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).</dd>
<dt>Scenario #2: Backdoored Pre-trained Model</dt>
<dd>A developer downloads a "fine-tuned" model from a public hub that contains a hidden trigger to bypass security checks[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).</dd>
<dt>Scenario #3: Poisoned Training Data</dt>
<dd>An attacker poisons a public dataset used for model alignment, causing the model to provide harmful instructions when specifically prompted[[OWASP]](https://genai.owasp.org/llmrisk/llm032025-supply-chain/).</dd>
</dl>

## 5. References

- [OWASP LLM03: Supply Chain Vulnerabilities](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)