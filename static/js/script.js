// Ensure the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    let resizeTimeout;

    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout); //Clear existing timeout
        resizeTimeout = setTimeout(() => {
            window.location.reload();
        }, 200);
    });


});