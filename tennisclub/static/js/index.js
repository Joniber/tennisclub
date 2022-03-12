menu = document.getElementById('menu')
console.log('hello')

menu.onclick = function (){
    document.getElementById('nav').classList.toggle('active')
    menu.classList.toggle('fa-bars')
    menu.classList.toggle('fa-times')
}

let i = 0;
let images = [];
let time = 4000;

images[0] = "static/images/tennisschlaeger.jpg"
images[1] = "static/images/tennis1.jpg"
images[2] = "static/images/tennis-5782695.jpg"
images[3] = "static/images/ClubHaus_neu_350.jpg"

function changeImg(){
    document.slide.src = images[i];

    if(i <images.length -1){
        i++;
    }
    else {
        i = 0
    }

    setTimeout( "changeImg()", time);

}

window.onload = changeImg

