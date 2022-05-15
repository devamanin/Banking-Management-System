document.getElementsByClassName("logout")[0].addEventListener("click", function(){
    document.getElementById('logout-f').submit();
})
let notBut = document.getElementsByClassName("notifications")[0];
notBut.addEventListener("click", function(){
    let notContainer = document.getElementsByClassName("notification-container")[0];
    let displayValue = window.getComputedStyle(notContainer).display;
    if (displayValue == "none"){
        notContainer.style.display = "block";
    }
    else{
        notContainer.style.display = "none";
    }
})
let prBut = document.getElementsByClassName("usr-profile")[0];
prBut.addEventListener("click", function(){
    let prContainer = document.getElementsByClassName("usr-profile-container")[0];
    displayValue = window.getComputedStyle(prContainer).display;
    if (displayValue == "none"){
        prContainer.style.display = "block";
        prContainer.style.opacity = "1";
    }
    else{
        prContainer.style.display = "none";
        prContainer.style.opacity = "0";
    }
})
let homeBut = document.getElementsByClassName("home")[0];
homeBut.addEventListener("click", function(){
    window.location.href = "/";
})
let tranBut = document.getElementsByClassName("receipt")[0];
tranBut.addEventListener("click", function(){
    window.location.href = "/transfer"
})
