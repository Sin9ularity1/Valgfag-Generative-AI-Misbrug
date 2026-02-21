document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('main section[id]');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const pageSidebarLinks = document.querySelectorAll('.sidebar ul li a');
                pageSidebarLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href').substring(1) === entry.target.id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, {
        threshold: 0,
        rootMargin: '-40% 0px -60% 0px'
    });

    sections.forEach(section => {
        observer.observe(section);
    });


    const researchTopics = [
        { title: "Research Home", path: "research.html" },
        { title: "LLM01: Prompt Injection", path: "research/prompt_injection.html" },
        { title: "LLM02: Sensitive Information Disclosure", path: "research/sensitive_information_disclosure.html" },
        { title: "LLM03: Supply Chain", path: "research/supply_chain.html" },
        { title: "LLM04: Data and Model Poisoning", path: "research/data_and_model_poisoning.html" },
        { title: "LLM05: Improper Output Handling", path: "research/improper_output_handling.html" },
        { title: "LLM06: Excessive Agency", path: "research/excessive_agency.html" },
        { title: "LLM07: System Prompt Leakage", path: "research/system_prompt_leakage.html" },
        { title: "LLM08: Vector and Embedding Weaknesses", path: "research/vector_and_embedding_weaknesses.html" },
        { title: "LLM09: Misinformation", path: "research/misinformation.html" },
        { title: "LLM10: Unbounded Consumption", path: "research/unbounded_consumption.html" },
    ];

    function generateResearchSidebar() {
        const sidebarLists = document.querySelectorAll('.sidebar ul');
        if (sidebarLists.length === 0) return;

        const currentHref = window.location.href;
        const isInResearchDirectory = currentHref.includes('/research/');

        sidebarLists.forEach(ul => {
            ul.innerHTML = ''; 

            researchTopics.forEach(topic => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.textContent = topic.title;

                let hrefPath = topic.path;

                if (isInResearchDirectory) {
                    if (topic.path === "research.html") {
                        hrefPath = "../research.html";
                    } else {
                        hrefPath = topic.path.split('/').pop();
                    }
                }

                a.href = hrefPath;

                let topicFileName = topic.path.split('/').pop();
                if (currentHref.endsWith(topicFileName) || (currentHref.endsWith('/') && topicFileName === 'index.html')) {
                    a.classList.add('active');
                } else if (currentHref.includes(topicFileName)) {
                     a.classList.add('active');
                }

                li.appendChild(a);
                ul.appendChild(li);
            });
        });
    }

    if (document.querySelector('.sidebar')) {
        const currentHref = window.location.href;
        if (currentHref.includes('research.html') || currentHref.includes('/research/')) {
            generateResearchSidebar();
        }
    }
});
