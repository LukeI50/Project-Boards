document.addEventListener("DOMContentLoaded", () => {

    // Detect the screens resolution
    let screenWidth = window.innerWidth;
    let screenHeight = window.innerHeight;


    // Send info to Django
    document.cookie = "screenWidth=" + screenWidth + "; path=/"
    document.cookie = "screenHeight=" + screenHeight + "; path=/"

})