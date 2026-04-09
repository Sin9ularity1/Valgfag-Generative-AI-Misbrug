import os
import re

files_map = {
    "prompt_injection.html": "APPENDIX_3_LLM01_Prompt_Injection.md",
    "sensitive_information_disclosure.html": "APPENDIX_4_LLM02_Sensitive_Info_Disclosure.md",
    "supply_chain.html": "APPENDIX_5_LLM03_Supply_Chain_Risks.md",
    "data_and_model_poisoning.html": "APPENDIX_6_LLM04_Model_Poisoning.md",
    "improper_output_handling.html": "APPENDIX_7_LLM05_Improper_Output_Handling.md",
    "excessive_agency.html": "APPENDIX_8_LLM06_Excessive_Agency.md",
    "system_prompt_leakage.html": "APPENDIX_9_LLM07_System_Prompt_Leakage.md",
    "vector_and_embedding_weaknesses.html": "APPENDIX_10_LLM08_Vector_Weaknesses.md",
    "misinformation.html": "APPENDIX_11_LLM09_Misinformation.md",
    "unbounded_consumption.html": "APPENDIX_12_LLM10_Unbounded_Consumption.md"
}

titles_map = {
    "prompt_injection.html": "Appendix 3: LLM01 Prompt Injection",
    "sensitive_information_disclosure.html": "Appendix 4: LLM02 Sensitive Info Disclosure",
    "supply_chain.html": "Appendix 5: LLM03 Supply Chain Risks",
    "data_and_model_poisoning.html": "Appendix 6: LLM04 Model Poisoning",
    "improper_output_handling.html": "Appendix 7: LLM05 Improper Output Handling",
    "excessive_agency.html": "Appendix 8: LLM06 Excessive Agency",
    "system_prompt_leakage.html": "Appendix 9: LLM07 System Prompt Leakage",
    "vector_and_embedding_weaknesses.html": "Appendix 10: LLM08 Vector Weaknesses",
    "misinformation.html": "Appendix 11: LLM09 Misinformation",
    "unbounded_consumption.html": "Appendix 12: LLM10 Unbounded Consumption"
}

def clean_html(html):
    # Extract content between <main class="content"> and </main>
    match = re.search(r'<main class="content">(.*?)</main>', html, re.DOTALL)
    if not match:
        # Fallback to <section>
        match = re.search(r'<section>(.*?)</section>', html, re.DOTALL)
    
    if match:
        content = match.group(1)
    else:
        content = html

    # Remove the first <h1> if it matches the title
    content = re.sub(r'<h1>.*?</h1>', '', content, count=1, flags=re.DOTALL)

    # Convert <h2> to ##
    content = re.sub(r'<h2>\s*(.*?)\s*</h2>', r'## \1', content)
    # Convert <h3> to ###
    content = re.sub(r'<h3>\s*(.*?)\s*</h3>', r'### \1', content)

    # Convert <ul> to nothing (Markdown handles it via <li>)
    content = re.sub(r'<ul>', '', content)
    content = re.sub(r'</ul>', '', content)

    # Convert <li> to - (handle nested lists roughly)
    content = re.sub(r'<li>\s*', r'- ', content)
    content = re.sub(r'\s*</li>', r'', content)

    # Convert <p> to newline
    content = re.sub(r'<p>\s*', r'\n\n', content)
    content = re.sub(r'\s*</p>', r'\n\n', content)

    # Convert <blockquote> to >
    content = re.sub(r'<blockquote>\s*', r'\n> ', content)
    content = re.sub(r'\s*</blockquote>', r'\n', content)

    # Convert <article> and <section> to nothing
    content = re.sub(r'<article>', '', content)
    content = re.sub(r'</article>', '', content)
    content = re.sub(r'<section>', '', content)
    content = re.sub(r'</section>', '', content)

    # Convert <strong> and <b> to **
    content = re.sub(r'<strong>\s*(.*?)\s*</strong>', r'**\1**', content)
    content = re.sub(r'<b>\s*(.*?)\s*</b>', r'**\1**', content)
    
    # Convert <em> and <i> to *
    content = re.sub(r'<em>\s*(.*?)\s*</em>', r'*\1*', content)
    content = re.sub(r'<i>\s*(.*?)\s*</i>', r'*\1*', content)

    # Convert <sup> to nothing but keep content
    content = re.sub(r'<sup>\s*(.*?)\s*</sup>', r'\1', content)

    # Convert <a href="URL">TEXT</a> to [TEXT](URL)
    content = re.sub(r'<a href="(.*?)"(.*?)>\s*(.*?)\s*</a>', r'[\3](\1)', content)

    # Clean up whitespace and indentation
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line.strip())
    
    content = '\n'.join(cleaned_lines)
    content = re.sub(r'\n{3,}', r'\n\n', content)
    content = content.strip()

    return content

def main():
    source_dir = "docs/research/"
    target_dir = "."

    for html_file, md_file in files_map.items():
        html_path = os.path.join(source_dir, html_file)
        if not os.path.exists(html_path):
            print(f"Skipping {html_file}, not found.")
            continue
        
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        md_content = clean_html(html_content)
        title = titles_map[html_file]
        
        final_content = f"# {title}\n\n{md_content}"
        
        md_path = os.path.join(target_dir, md_file)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Converted {html_file} to {md_file}")

if __name__ == "__main__":
    main()
