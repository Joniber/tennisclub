menu = document.getElementById('menu')
console.log('hello')

menu.onclick = function (){
    document.getElementById('nav').classList.toggle('active')
    menu.classList.toggle('fa-bars')
    menu.classList.toggle('fa-times')
}