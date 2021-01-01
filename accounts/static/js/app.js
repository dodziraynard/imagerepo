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
