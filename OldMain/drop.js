let dropDown = document.getElementsByClassName(menu - items)[0];
let isOpen = false;

function openDropDown() {
    isOpen = !isOpen;
    if (isOpen) {
        dropDown.setAttribute('class', 'dropdown-open');
    } else {
        dropDown.setAttribute('class', 'dropdown-close');
    }
}
