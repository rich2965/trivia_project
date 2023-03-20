var categorySelect = document.getElementById('category-select');
var cards = document.querySelectorAll('.flashcard,.flashcard_movie');

function redirectToPage(redirect_url) {
    var selectElement = document.getElementById('category-select');
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    if (selectedValue !== "") {
        window.location.href = redirect_url;
    }
}

function generateRandomMovie(){
    location.reload();
}

for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
}