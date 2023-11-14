document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".SE2022-Button");
    const glasgowButton = document.querySelector(".Glasgow-Button");
    const aboardButton = document.querySelector(".Aboard-Button");
    const internButton = document.querySelector(".Intern-Button");
    const se_Head = document.querySelector(".SE_Head"); 
    
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        const elementTop = rect.top;
        const elementBottom = rect.bottom;

        const offset = -500;

        return (
            elementTop - offset <= windowHeight &&
            elementBottom + offset >= 0
        );
    }

    document.querySelectorAll('.navbar-menu a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault(); 

            const targetId = link.getAttribute('href').substring(1);

            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                setTimeout(() => {
                    targetSection.scrollIntoView({
                        behavior: 'smooth', 
                    });
                }, 50); 
            }
        });
    });

    function handleScroll() {
        const targetSectionSE = document.getElementById("SE2022");
        const targetSectionGlasgow = document.getElementById("Glasgow");
        const targetSectionAboard = document.getElementById("Aboard");
        const targetSectionIntern = document.getElementById("Intern");
        const se_Head = document.querySelector(".SE_Head"); 

        console.log("SE2022 in viewport:", isElementInViewport(targetSectionSE));
        console.log("Glasgow in viewport:", isElementInViewport(targetSectionGlasgow));
        console.log("Aboard in viewport:", isElementInViewport(targetSectionAboard));
        console.log("Intern in viewport:"), isElementInViewport(targetSectionIntern);

        if (isElementInViewport(targetSectionSE)) {
            const navbarLinks = document.querySelectorAll('.navbar-menu a');
            navbarLinks.forEach(link => {
                link.style.color = 'black';
                link.addEventListener('mouseenter', () => {
                    link.style.textDecoration = 'underline';
                    link.style.color = '#ff9900';
                });
                link.addEventListener('mouseleave', () => {
                    link.style.textDecoration = 'none';
                    link.style.color = 'black';
                });
            });
        
        

            setTimeout(function () {
                button.style.display = "block";
                button.style.opacity = 1; 
            }, 1000); 
            

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
            }, 500); 
        }
    


        else if (isElementInViewport(targetSectionAboard)){
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
        
            setTimeout(function () {
                aboardButton.style.display = "block";
            }, 1000); 
        }


        
        else if (isElementInViewport(targetSectionIntern)){
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



    window.addEventListener("scroll", handleScroll);
});

window.addEventListener('wheel', fixedHeightScroll);

