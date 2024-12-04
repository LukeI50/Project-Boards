// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // const breakpoints = [768, 1024]
    const breakpoints = {default: 1024, small: 768};

    // Get the value stored in the currentMode cookie
    const currentMode = document.cookie
        .split('; ')
        .find((row) => row.startsWith('currentMode='))
        ?.split("=")[1];
    
    // set the cookie values for the screen width and mode
    function setScreenValues(currentWidth, mode) {
        document.cookie = "screenWidth=" + `${currentWidth}` + "; path=/; Secure; SameSite=None";
        document.cookie = "currentMode=" + `${mode}` + "; path=/; Secure; SameSite=None";
        window.location.reload();
    }


    
    window.addEventListener("resize", () => {
        const currentWidth = window.innerWidth;

        // Set screen width logic
        if (currentWidth < breakpoints.small && currentMode !== 'small') {
            setScreenValues(currentWidth, "small");
        } else if (currentWidth >= breakpoints.small && currentWidth < breakpoints.default && currentMode !== "default") {
            setScreenValues(currentWidth, 'default');
        } 
    })

});