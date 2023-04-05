//// Used for filtering the genre 
var categorySelect = document.getElementById('genre-select');
var cards = document.querySelectorAll('.flashcard,.flashcard_movie');

function redirectToPage(id) {
    var selectElement = document.getElementById(id);
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    if (selectedValue !== "") {
        window.location.href = selectedValue;
    }
}

//// Used by the Generate button at the bottom to refresh the page 
function refreshPage(){
    location.reload();
}

//// Used for flipping the flashcards upon click 
for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
}

//// Used on the Movie page for when there are multiple images and if user wanted to change to another
function changeImage(imageURL) {
  document.getElementById("contentImage").src = imageURL.value;
  
  var activeButtons = document.querySelectorAll("button.active");

  for (var i = 0; i < activeButtons.length; i++) {
    activeButtons[i].classList.remove("active");
  }
  const myButton = document.getElementById(imageURL.id);
  myButton.classList.add('active');
  lastScrollPosition = parseInt(imageURL.id)
  
}


//// Used for swiping on image container to get to the next image. 
var mySwiper = new Swiper('.swiper-container', {
  // Add options here
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});

// Add event listeners to the navigation buttons
var prevButton = document.querySelector('.swiper-button-prev');
var nextButton = document.querySelector('.swiper-button-next');
prevButton.addEventListener('click', function(event) {
  event.stopPropagation(); // Prevent click event from propagating
  // Your code for handling the click event for the prev button
});
nextButton.addEventListener('click', function(event) {
  event.stopPropagation(); // Prevent click event from propagating
  // Your code for handling the click event for the next button
});