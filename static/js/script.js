// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const breakpoints = [768, 1024]
    const currentMode = document.cookie
        .split('; ')
        .find((row) => row.startsWith('currentMode='))
        ?.split("=")[1]

    console.log(currentMode)
    
    function diff(a, b) {return (a-b)}

    window.addEventListener("resize", () => {
        let currentWidth = window.innerWidth;

        if (diff(currentWidth, breakpoints[1]) < 0 && currentMode == 'default') {
            // Set the cookie to the new screenWidth
            document.cookie = "screenWidth=" + window.innerWidth + "; path=/; Secure; SameSite=None";

            // Reload the window with the new screenWidth cookie value
            window.location.reload();
        }


    })


});