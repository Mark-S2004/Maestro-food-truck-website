function toggleMenu() {
  const menu = document.querySelector("#menu");
  menu.classList.toggle("menu-open");
  
createMenuItems(); // create initial menu items


}

function createMenuItems() {
  const container = document.getElementById("menu-items");
  const menuItems = [
    { text: "Home", url: "/" },
    { text: "Food Menu", url: "/" },
    { text: "Cart", url: "/" },
    { text: "About Us", url: "/" },
  ];

  // Remove any existing menu items
  container.innerHTML = "";

  // Add new menu items
  menuItems.forEach((menuItem) => {
    const link = document.createElement("a");
    link.href = menuItem.url;
    link.textContent = menuItem.text;
    link.classList.add("menu-item");
    container.appendChild(link);
  });
}

createMenuItems(); // create initial menu items

