let ic_menu = document.getElementById("icon-menu"); //we have create the var ic_menu for use it as reference

//Now, we will declare a function called show_menu for show the vertical nav with an animation for mobile dispositives 

function show_menu() {
    document.getElementById("move-content").classList.toggle('move-container-all');
    document.getElementById("show-menu").classList.toggle('show-lateral')
}

ic_menu.addEventListener("click", show_menu);