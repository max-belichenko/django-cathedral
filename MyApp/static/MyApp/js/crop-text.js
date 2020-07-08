`use strict`;

(function () {

    const cropElement = document.querySelectorAll('.crop-text'), // выбор элементов
          size = 120                                             // кол-во символов
          endCharacter = '...';                                  // окончание

    cropElement.forEach(el => {
        let text = el.innerHTML;

        if (el.innerHTML.length > size) {
            text = text.substr(0, size);
            el.innerHTML = text + endCharacter;
        }
    });

}());