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

    onLoad(window.innerWidth, currentMode)

    // set the cookie values for the screen width and mode
    function setScreenMode(mode) {
        // document.cookie = "screenWidth=" + `${currentWidth}` + "; path=/; Secure; SameSite=None";
        document.cookie = "currentMode=" + `${mode}` + "; path=/; Secure; SameSite=None";
    }

    // Determine the Next Mode for Display size cookie
    function determineNewMode(currentWidth, breakpoints) {
        if (currentWidth < breakpoints.small) {
            return "small";
        } else if (currentWidth >= breakpoints.small && currentWidth < breakpoints.large ) {
            return "default";
        } else if (currentWidth >= breakpoints.large) {
            return "large";
        }
    }

    // On Loading the page initiate this function as a check to ensure the page is loaded to correct state
    function onLoad(currentWidth, currentMode) {
        console.log(currentWidth);
        let newMode = "";

        newMode = determineNewMode(currentWidth, breakpoints)

        setScreenMode(newMode);
        reloadWindow(currentMode, newMode)
    }

    // Reload the window if currentMode and newMode are different
    function reloadWindow(currentMode, newMode) {
        if (currentMode !== newMode) {
            setScreenMode(newMode); 
            currentMode = newMode;

            window.location.reload();
        }
    }

    let resizeTimeout;

    // trigger event upon window being resized
    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout);
        console.log(window.innerWidth)

        resizeTimeout = setTimeout(() => {
            const currentWidth = window.innerWidth;
            let newMode = "";
            newMode = determineNewMode(currentWidth, breakpoints);

            console.log("current mode is", currentMode)
            console.log("breakpoints are", breakpoints)
            console.log("new mode is", newMode)

            reloadWindow(currentMode, newMode);

        }, 150);
    });
});
