const calculateTotalPrice = () => {
    let totalPrice = 0;
    const prices = document.body.querySelectorAll(".price")
    for (let i = 0; i < prices.length; i++) {
        totalPrice += Number(prices[i].textContent)
    }
    document.body.querySelector("#total-price").textContent = totalPrice
}
calculateTotalPrice()

const calculateProductPrice = parentNode => {
    const quantity = Number(parentNode.querySelector(".quantity").textContent)
    parentNode.querySelector(".price").textContent = 72*quantity
    calculateTotalPrice()
}

document.body.querySelectorAll(".add").forEach(item => {
    item.addEventListener("click", () => {
        const quantityNode = item.parentElement.querySelector(".quantity")
        quantityNode.textContent = Number(quantityNode.textContent) + 1
        calculateProductPrice(item.parentElement.parentElement)
    })
})

document.body.querySelectorAll(".remove").forEach(item => {
    item.addEventListener("click", () => {
        const quantityNode = item.parentElement.querySelector(".quantity")
        if (Number(quantityNode.textContent) != 1) {
            quantityNode.textContent = Number(quantityNode.textContent) - 1
        }
        calculateProductPrice(item.parentElement.parentElement)
    })
})