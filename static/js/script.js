// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    let initialWidth = window.innerWidth;
    const breakpoints = [768, 1024]
    let currentMode = null
    
    function diff(a, b) {return Math.abs(a-b)}

    window.addEventListener("resize", () => {
        let currentWidth = window.innerWidth;

        if (diff(currentWidth, breakpoints[1]) != true && currentMode != 'small') {
            // set current mode to avoid refreshing within same breakpoint
            currentMode = 'small'

            // Set the cookie to the new screenWidth
            document.cookie = "screenWidth=" + window.innerWidth + "; path=/";

            // Reload the window with the new screenWidth cookie value
            window.location.reload();
        }


    })


});