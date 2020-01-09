window.onload = function () {
    elem = document.querySelectorAll('.input-print');
    for (var i = 0; i < elem.length; i++) {
        elem[i].addEventListener("click", function () {
            href = this.parentElement.parentElement.previousElementSibling.lastElementChild.firstElementChild.href;
            console.log(href);
            new_window = window.open(href, '_blank');
            new_window.print();
        })
    }
};
