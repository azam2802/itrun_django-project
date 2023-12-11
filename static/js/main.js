window.addEventListener('scroll', function() {
    let scroll = document.querySelector('.onTop')
    scroll.classList.toggle("active", window.scrollY>500)
})
