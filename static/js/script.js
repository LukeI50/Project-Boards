// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    let initialWidth = window.innerWidth;
    
    function diff(a, b) {return Math.abs(a-b)}

    window.addEventListener("resize", () => {
        let width = window.innerWidth;
        
        const breakpoints = (768, 1024)

        if (diff(width, breakpoints[0])){
            document.cookie = "screenWidth=" + window.innerWidth + "; path=/";
            window.location.reload();
        }
    })


});