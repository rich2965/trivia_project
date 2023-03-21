var categorySelect = document.getElementById('genre-select');
var cards = document.querySelectorAll('.flashcard,.flashcard_movie');

function redirectToPage(redirect_url) {
    var selectElement = document.getElementById('genre-select');
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    if (selectedValue !== "") {
        window.location.href = redirect_url;
    }
}

function refreshPage(){
    location.reload();
}


for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
}

function changeImage(imageURL) {
  document.getElementById("contentImage").src = imageURL.value;
  
  var activeButtons = document.querySelectorAll("button.active");

  for (var i = 0; i < activeButtons.length; i++) {
    activeButtons[i].classList.remove("active");
  }
  const myButton = document.getElementById(imageURL.id);
  myButton.classList.add('active');

}
