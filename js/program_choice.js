document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".SE2022-Button");
    const glasgowButton = document.querySelector(".Glasgow-Button");
    const aboardButton = document.querySelector(".Aboard-Button");
    const internButton = document.querySelector(".Intern-Button");
    const se_Head = document.querySelector(".SE_Head"); // Select the SE_Head element

    // Function to check if an element is in the viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        const elementTop = rect.top;
        const elementBottom = rect.bottom;

        // Adjust the offset to ensure the entire "Glasgow" section is within the viewport
        const offset = -500;
    // adjust this value as needed

        return (
            elementTop - offset <= windowHeight &&
            elementBottom + offset >= 0
        );
    }

    document.querySelectorAll('.navbar-menu a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent the default behavior of a link

            // Get the target section's ID from the link's href
            const targetId = link.getAttribute('href').substring(1);

            // Find the target section element
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                // Scroll to the target section with a delay
                setTimeout(() => {
                    targetSection.scrollIntoView({
                        behavior: 'smooth', // Add smooth scroll behavior
                    });
                }, 50); // Delay in milliseconds (adjust as needed)
            }
        });
    });

    // Function to handle scroll and show/hide the button with a delay
    function handleScroll() {
        const targetSectionSE = document.getElementById("SE2022");
        const targetSectionGlasgow = document.getElementById("Glasgow");
        const targetSectionAboard = document.getElementById("Aboard");
        const targetSectionIntern = document.getElementById("Intern");
        const se_Head = document.querySelector(".SE_Head"); // Select the SE_Head element


        console.log("SE2022 in viewport:", isElementInViewport(targetSectionSE));
        console.log("Glasgow in viewport:", isElementInViewport(targetSectionGlasgow));
        console.log("Aboard in viewport:", isElementInViewport(targetSectionAboard));
        console.log("Intern in viewport:"), isElementInViewport(targetSectionIntern);

        if (isElementInViewport(targetSectionSE)) {
            // Show the button after a 0.25-second delay
            const navbarLinks = document.querySelectorAll('.navbar-menu a');
            navbarLinks.forEach(link => {
                link.style.color = 'black';
                // Add hover styles
                link.addEventListener('mouseenter', () => {
                    link.style.textDecoration = 'underline';
                    link.style.color = '#ff9900';
                });
                // Remove hover styles
                link.addEventListener('mouseleave', () => {
                    link.style.textDecoration = 'none';
                    link.style.color = 'black';
                });
            });
        
        

            setTimeout(function () {
                button.style.display = "block";
                button.style.opacity = 1; // Set opacity to 1 to fade it in
            }, 1000); // 1000 milliseconds = 1 second
            

        } 
        
        else if (isElementInViewport(targetSectionGlasgow)){
            const navbarLinks = document.querySelectorAll('.navbar-menu a');
            navbarLinks.forEach(link => {
                link.style.color = 'white';
                
                link.addEventListener('mouseenter', () => {
                    link.style.textDecoration = 'underline';
                    link.style.color = '#ff9900';
                });
                // Remove hover styles
                link.addEventListener('mouseleave', () => {
                    link.style.textDecoration = 'none';
                    link.style.color = 'white';
                });
            });

            
            // Show the button after a 0.25-second delay
            setTimeout(function () {
                glasgowButton.style.display = "block";
            }, 500); // 4000 milliseconds = 4000 seconds >>> suit for spending scrol for each pages
        }
    


        else if (isElementInViewport(targetSectionAboard)){
            // Change the text color of the navbar links to black with a delay
            const navbarLinks = document.querySelectorAll('.navbar-menu a');
            navbarLinks.forEach(link => {
                link.style.color = 'black';
                link.addEventListener('mouseenter',() => {
                    link.style.textDecoration = 'underline';
                    link.style.color = '#ff9900';
                })
                link.addEventListener('mouseleave',() => {
                    link.style.textDecoration = 'none';
                    link.style.color = 'black';
                })
            });
        
            // Show the button after a 0.25-second delay
            setTimeout(function () {
                aboardButton.style.display = "block";
            }, 1000); // 1000 milliseconds = 1 second
        }
        // Add an event listener to your navigation links


        
        else if (isElementInViewport(targetSectionIntern)){
            // Show the button after a 0.25-second delay
            const navbarLinks = document.querySelectorAll('.navbar-menu a');
            navbarLinks.forEach(link => {
                link.style.color = 'white';
                link.addEventListener('mouseenter',() => {
                    link.style.textDecoration = 'underline';
                    link.style.color = '#ff9900';
                });
                link.addEventListener('mouseleave',() => {
                    link.style.textDecoration = 'none';
                    link.style.color = 'white';
                });
            });

            setTimeout(function () {
                internButton.style.display = "block";
            }, 500); // 4000 milliseconds = 4000 seconds >>> suit for spending scrol for each pages
        }
        
        else {
            // Hide the button immediately
            button.style.display = "none";
            glasgowButton.style.display = "none";
            aboardButton.style.display = "none";
            internButton.style.display = "none";
        }
        
    }



    // Add event listener for scroll
    window.addEventListener("scroll", handleScroll);
});



// --------still not working-------- //

// Function to handle fixed height scrolling
// function fixedHeightScroll(event) {
//     const deltaY = event.deltaY;
//     const linkHeight = 20; // Set the height of your <a> elements in pixels

//     if (deltaY !== 0) {
//         const linksToScroll = Math.floor(Math.abs(deltaY) / linkHeight);
//         const scrollAmount = deltaY > 0 ? linksToScroll * linkHeight : -linksToScroll * linkHeight;
//         window.scrollBy(0, scrollAmount);
//     }
// }



// Add a wheel event listener for fixed height scrolling
window.addEventListener('wheel', fixedHeightScroll);

