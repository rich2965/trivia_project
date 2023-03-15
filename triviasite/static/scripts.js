var categorySelect = document.getElementById('category-select');
var cards = document.querySelectorAll('.flashcard');

function redirectToPage(redirect_url) {
    var selectElement = document.getElementById('category-select');
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    if (selectedValue !== "") {
        window.location.href = redirect_url;
    }
}

categorySelect.addEventListener('change', function() {
    var selectedCategory = categorySelect.value;
    for (var i = 0; i < cards.length; i++) {
        var cardCategory = cards[i].getAttribute('data-category');
        if (selectedCategory === 'all' || selectedCategory === cardCategory) {
            cards[i].style.display = 'block';
        } else {
            cards[i].style.display = 'none';
        }
    }
});

for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
}