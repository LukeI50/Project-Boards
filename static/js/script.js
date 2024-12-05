// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // const breakpoints = [768, 1024]
    const breakpoints = {
        large: 1560,
        default: 1024,
        small: 768,
    };

    // Get the value stored in the currentMode cookie
    let currentMode = document.cookie
        .split('; ')
        .find((row) => row.startsWith('currentMode='))
        ?.split("=")[1];

    console.log(currentMode)
    
    // set the cookie values for the screen width and mode
    function setScreenMode(mode) {
        // document.cookie = "screenWidth=" + `${currentWidth}` + "; path=/; Secure; SameSite=None";
        document.cookie = "currentMode=" + `${mode}` + "; path=/; Secure; SameSite=None";
    }

    let resizeTimeout;

    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout);
        console.log(window.innerWidth)

        resizeTimeout = setTimeout(() => {
            const currentWidth = window.innerWidth;
            let newMode = "";

            if (currentWidth < breakpoints.small) {
                newMode = "small";
            } else if (currentWidth >= breakpoints.small) {
                newMode = "default";
            }

            if (currentMode !== newMode) {
                setScreenMode(newMode); 
                currentMode = newMode;

                window.location.reload();
            }

        }, 150);
    });
});
