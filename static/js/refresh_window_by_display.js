// Ensure the DOM is fully loaded before executing any script
document.addEventListener("DOMContentLoaded", function() {

    // Define breakpoints for different screen sizes
    const breakpoints = {
        large: 1560,
        default: 1024,
        small: 768
    };

    // Retrieve the value stored in the currentMode cookie
    let currentMode = document.cookie
        .split('; ')
        .find((row) => row.startsWith('currentMode='))
        ?.split("=")[1];

    // Initialize the page by determining and setting
    // the screen mode based on the current width
    onLoad(window.innerWidth, currentMode);

    /**
     * Set the cookie value for the screen mode.
     * @param {string} mode - The screen mode to be set (e.g., "small", "default", "large").
     */
    function setScreenMode(mode) {
        document.cookie = "currentMode=" +
        `${mode}` + "; path=/; Secure; SameSite=None";
    };

    /**
     * Determine the next mode based on the current width and defined breakpoints.
     * @param {number} currentWidth - The current width of the window.
     * @param {Object} breakpoints - An object containing the breakpoints for different screen sizes.
     * @returns {string} - The determined screen mode ("small", "default", "large").
     */
    function determineNewMode(currentWidth, breakpoints) {
        if (currentWidth < breakpoints.small) {
            return "small";
        } else if (currentWidth >= breakpoints.small && currentWidth <
            breakpoints.large ) {
            return "default";
        } else if (currentWidth >= breakpoints.large) {
            return "large";
        }
    };

    /**
     * Initialize the page by setting the screen mode and reloading if necessary.
     * @param {number} currentWidth - The current width of the window.
     * @param {string|null} currentMode - The current screen mode stored in a cookie.
     */
    function onLoad(currentWidth, currentMode) {
        let newMode = "";

        newMode = determineNewMode(currentWidth, breakpoints);

        setScreenMode(newMode);
        reloadWindow(currentMode, newMode);
    };

    /**
     * Reload the window if the current mode and new mode are different.
     * @param {string|null} currentMode - The current screen mode stored in a cookie.
     * @param {string} newMode - The newly determined screen mode.
     */
    function reloadWindow(currentMode, newMode) {
        if (currentMode !== newMode) {
            setScreenMode(newMode);
            currentMode = newMode;

            window.location.reload();
        }
    };

    let resizeTimeout;

    // Trigger event upon window being resized
    window.addEventListener("resize", function() {
        clearTimeout(resizeTimeout);

        resizeTimeout = setTimeout(() => {
            const currentWidth = window.innerWidth;
            let newMode = "";
            newMode = determineNewMode(currentWidth, breakpoints);

            reloadWindow(currentMode, newMode);

        }, 150);  // Debounce the resize event for better performance
    });
});
