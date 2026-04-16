document.querySelector("form")?.addEventListener("submit", function(e) {
    let email = document.querySelector("input[name='email']").value;

    if (!email.includes("@")) {
        alert("Invalid Email!");
        e.preventDefault();
    }
});