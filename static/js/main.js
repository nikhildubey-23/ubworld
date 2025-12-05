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

// Theme Switcher
document.addEventListener('DOMContentLoaded', () => {
    const themeSwitcher = document.getElementById('theme-switcher');
    const body = document.body;
    const icon = themeSwitcher.querySelector('i');

    const updateIcon = () => {
        if (body.classList.contains('light-mode')) {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    };

    const toggleTheme = () => {
        body.classList.toggle('light-mode');
        localStorage.setItem('theme', body.classList.contains('light-mode') ? 'light' : 'dark');
        updateIcon();
    };

    themeSwitcher.addEventListener('click', toggleTheme);

    // On page load, set the theme
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('light-mode');
    }
    updateIcon();
});

