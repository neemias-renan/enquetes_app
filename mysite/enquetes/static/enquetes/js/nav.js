const hamMenu = document.querySelector('.hamburger-menu');
const navMenu = document.querySelector('.nav-mobile');
const body = document.querySelector('body');

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    navMenu.classList.toggle('active-nav-mobile');
    body.classList.toggle('no-scroll');

});