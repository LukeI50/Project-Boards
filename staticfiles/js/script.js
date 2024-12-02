document.addEventListener("DOMContentLoaded", () => {

    // If the carousel element it present within DOM, then initialise the variable.
    if (document.getElementById('myCarousel')) {
        const myCarousel = bootstrap.Carousel.getInstance('#myCarousel');
    }

})