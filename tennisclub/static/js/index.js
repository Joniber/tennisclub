menu = document.getElementById('menu')

menu.onclick = function (){
    document.getElementById('nav').classList.toggle('active')
    menu.classList.toggle('fa-bars')
    menu.classList.toggle('fa-times')
}



