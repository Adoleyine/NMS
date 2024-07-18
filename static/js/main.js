let btn = document.querySelector('#btn');
let sidebar = document.querySelector('.sidebar');
btn.onclick = function () {
    sidebar.classList.toggle('active');
}
const navLinkEls = document.querySelectorAll('div ul li a');
const windowPathname = window.location.pathname;
navLinkEls.forEach(navLinkEl => {
    const navLinkPathname = new URL(navLinkEl.href ).pathname;
    if((windowPathname == navLinkPathname) || (windowPathname === '/base.html' && navLinkPathname === '/')){
        navLinkEl.classList.add('nav-active');
    }
});
