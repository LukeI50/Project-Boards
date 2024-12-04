// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const breakpoints = [768, 1024]
    const currentMode = document.cookie
        .split('; ')
        .find((row) => row.startsWith('currentMode='))
        ?.split("=")[1]

    console.log(currentMode)
    
    function diff(a, b) {return (a-b)}

    function setScreenValues(currentWidth, mode) {
        document.cookie = "screenWidth=" + `${currentWidth}` + "; path=/; Secure; SameSite=None";
        document.cookie = "currentMode=" + `${mode}` + "; path=/; Secure; SameSite=None";
        window.location.reload();
    }

    window.addEventListener("resize", () => {
        let currentWidth = window.innerWidth;

        if (diff(currentWidth, breakpoints[0]) < 0 && currentMode != 'small') {
            // Set the cookie to the new screenWidth
            setScreenValues(currentWidth, "small");

        } else if (diff(currentWidth, breakpoints[1]) < 0 && currentMode != 'default') {
            setScreenValues(currentWidth, "default");

        }


    })


});