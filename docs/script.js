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
});
