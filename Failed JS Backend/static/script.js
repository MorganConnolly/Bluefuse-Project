function fibShow() {
    const fibsec = document.getElementById("fibsec");
    const fibsec_computed = window.getComputedStyle(fibsec);
    const palsec = document.getElementById("palsec");
    const palsec_computed = window.getComputedStyle(palsec);

    showBreak();

    if (fibsec_computed.opacity == "0" && palsec_computed.opacity == "0") {
        fibsec.style.display = "block";
        setTimeout(() => {
            fibsec.style.opacity = "1"; 
        }, 100); 
    } else if (palsec_computed.opacity == "1") {
        palsec.style.opacity = "0";
        setTimeout(() => {
            palsec.style.display = "none";
            fibsec.style.display = "block";
            setTimeout(() => {
                fibsec.style.opacity = "1"; 
            }, 100); 
        }, 1000);
    }
}

function palShow() {
    const fibsec = document.getElementById("fibsec");
    const fibsec_computed = window.getComputedStyle(fibsec);
    const palsec = document.getElementById("palsec");
    const palsec_computed = window.getComputedStyle(palsec);

    showBreak();

    if (palsec_computed.opacity == "0" && fibsec_computed.opacity == "0") {
        palsec.style.display = "block";
        setTimeout(() => {
            palsec.style.opacity = "1"; 
        }, 100); 
    } else if (fibsec_computed.opacity == "1") {
        fibsec.style.opacity = "0";
        setTimeout(() => {
            fibsec.style.display = "none";
            palsec.style.display = "block";
            setTimeout(() => {
                palsec.style.opacity = "1"; 
            }, 100); 
        }, 1000);
    }
}

function showBreak() {
    const linebreak = document.getElementById("linebreak");
    const linebreak_computed = window.getComputedStyle(linebreak);
    if (linebreak_computed.width == "0px") {
        linebreak.style.width = "75%";
    }
}

function fibSubmit() {
    const fib_in = document.getElementById("fib_in")
    
}