# Appendix 4: LLM02 Sensitive Info Disclosure

## 1. What is Sensitive Information Disclosure

Sensitive information disclosure occurs when a Large Language Model (LLM) exposes personal, financial, health, business, or proprietary data[[OWASP LLM02]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
This can include training data, confidential algorithms, security credentials, or legal documents.

Such disclosures can result in privacy violations, unauthorized access, or intellectual property breaches[[OWASP LLM02]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
Users must be aware of the risks of submitting sensitive data to LLMs.

**Potential impacts include:**

- Exposure of personal identifiable information (PII)[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- Leakage of proprietary algorithms or model configurations[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- Confidential business information disclosure[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- Security credentials or secrets leakage[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

## 2. Common Examples of Vulnerability

### 2.1 PII Leakage

Personal identifiable information may be disclosed during interactions with the LLM[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).

### 2.2 Proprietary Algorithm Exposure

Poorly configured outputs can reveal proprietary algorithms or data[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/). For example, training data may be exposed to inversion attacks that reconstruct sensitive inputs.

### 2.3 Sensitive Business Data Disclosure

Generated responses might inadvertently include confidential business information[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).

## 3. Prevention and Mitigation

Organizations should implement multiple layers of safeguards to minimize the risk of sensitive information disclosure[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).

- **3.1 Data Sanitization:**

- Scrub or mask sensitive content before training or processing. Prevent user data from entering the model[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.2 Robust Input Validation:**

- Detect and filter out sensitive or harmful inputs to prevent exposure through outputs[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.3 Access Controls:**

- Enforce least privilege access to sensitive data and restrict data sources[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.4 Federated Learning & Privacy Techniques:**

- Use decentralized training and differential privacy to reduce risk of data exposure[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.5 User Education & Transparency:**

- Guide users on safe LLM usage and maintain clear policies on data usage, retention, and opt-outs[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.6 Secure System Configuration:**

- Limit user access to system prompts and follow security misconfiguration best practices[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).
- **3.7 Advanced Techniques:**

- Implement homomorphic encryption, tokenization, and redaction to keep data confidential during processing[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).

## 4. Example Attack Scenarios
<dl>
<dt>Scenario #1: Unintentional Data Exposure</dt>
<dd>A user receives another user's PII due to insufficient data sanitization[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).</dd>
<dt>Scenario #2: Targeted Prompt Injection</dt>
<dd>An attacker bypasses input filters to extract sensitive information[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).</dd>
<dt>Scenario #3: Data Leak via Training Data</dt>
<dd>Negligent inclusion of sensitive data in training leads to exposure in model outputs[[OWASP]](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/).</dd>
</dl>

## 5. References

- [OWASP LLM02 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)