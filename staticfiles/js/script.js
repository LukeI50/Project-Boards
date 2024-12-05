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


    // following two listeners are made to hide toast-containers when new project form model is loaded.
    // Otherwise, model is placed behind the toast containers.
    document.getElementById('AddProjectButton').addEventListener('click', () => {
        if (document.getElementsByClassName('toast-container')) {
            let toastContainers = document.querySelectorAll('.toast-container');

            toastContainers.forEach(container => {
                container.classList.add('d-none');
            })
        }
    });

    document.getElementById("AddProjectButton-Close").addEventListener('click', () => {
        if (document.getElementsByClassName('toast-container')) {
            let toastContainers = document.querySelectorAll('.toast-container');

            toastContainers.forEach(container => {
                const show = setInterval(() => {
                    container.classList.remove('d-none');
                    if (toastContainers[1].classList.contains('d-none') == false) {
                        clearInterval(show);
                    }
                }, 250)
            });

        }
    })


});
