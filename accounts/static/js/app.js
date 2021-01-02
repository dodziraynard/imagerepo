const operation = document.querySelector("#operation")
const hamgurger = document.querySelector(".hamburger")
const actions = document.querySelector(".actions")

const PRIVATE = "private"
const PUBLIC = "public"
const DELETE = "delete"

document.querySelector("#my-images-form")?.addEventListener("submit", (Event) => {
    let message = "Are your sure you want to delete?"
    switch (operation.value) {
        case DELETE:
            let response = confirm(message)
            if (response !== true) {
                Event.preventDefault()
            }
    }
})

hamgurger?.addEventListener("click", () => {
    actions.classList.toggle("open")
})

const toggleSwitch = document.querySelector('#toggle-theme');

document.documentElement.setAttribute('data-theme', localStorage.getItem('theme'));
if (localStorage.getItem('theme') === "dark")
    toggleSwitch?.setAttribute("checked", true)


console.log(document.documentElement)
function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
    else {
        document.documentElement.setAttribute('data-theme', 'light');
    }
}

toggleSwitch?.addEventListener('change', switchTheme, false);

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark'); //add this
    }
    else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light'); //add this
    }
}