const hamburger = document.getElementById('hamburgerIcon');
const nav = document.querySelector('.nav-2');

hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
    hamburger.classList.toggle('active');
});
