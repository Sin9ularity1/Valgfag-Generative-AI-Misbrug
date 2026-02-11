document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('main section[id]');
    const navLinks = document.querySelectorAll('.sidebar ul li a');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href').substring(1) === entry.target.id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '-50px 0px -25% 0px'
    });

    sections.forEach(section => {
        observer.observe(section);
    });
});
