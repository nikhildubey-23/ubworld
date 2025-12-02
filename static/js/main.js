// Navbar Scroll Effect
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar');
    if (navbar && window.scrollY > 50) {
        navbar.classList.add('shadow-lg');
    } else if (navbar) {
        navbar.classList.remove('shadow-lg');
    }
});

// FAQ Search
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('faq-search');
    if (searchInput) {
        searchInput.addEventListener('keyup', function (e) {
            const query = e.target.value.toLowerCase();
            const items = document.querySelectorAll('#faqAccordion .accordion-item');
            items.forEach(item => {
                const question = item.querySelector('.accordion-button').textContent.toLowerCase();
                const answer = item.querySelector('.accordion-body').textContent.toLowerCase();
                if (question.includes(query) || answer.includes(query)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
});
