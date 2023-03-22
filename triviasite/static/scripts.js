// Used for filtering the genre 
var categorySelect = document.getElementById('genre-select');
var cards = document.querySelectorAll('.flashcard,.flashcard_movie');

function redirectToPage(redirect_url) {
    var selectElement = document.getElementById('genre-select');
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    if (selectedValue !== "") {
        window.location.href = redirect_url;
    }
}

// Used by the Generate button at the bottom to refresh the page 
function refreshPage(){
    location.reload();
}

// Used for flipping the flashcards upon click 
for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
}

// Used on the Movie page for when there are multiple images and if user wanted to change to another
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


// Used for swiping on image container to get to the next image. 
var container = document.getElementById("imageContainer");
var startX, startY;
var lastScrollPosition = 1

container.addEventListener("touchstart", function(event) {
  // Get the starting position of the touch
  startX = event.touches[0].clientX;
  startY = event.touches[0].clientY;
});

container.addEventListener("touchmove", function(event) {
  // Prevent scrolling
  event.preventDefault();
});

container.addEventListener("touchend", function(event) {
  // Get the end position of the touch
  var endX = event.changedTouches[0].clientX;
  var endY = event.changedTouches[0].clientY;

  // Calculate the distance and direction of the swipe
  var distanceX = startX - endX;
  var distanceY = startY - endY;
  var absX = Math.abs(distanceX);
  var absY = Math.abs(distanceY);
  var direction = "";

  if (absX > absY) {
    // Horizontal swipe
    if (distanceX > 0) {
      // Swipe left
      direction = "left";
    } else {
      // Swipe right
      direction = "right";
    }
  }

  if (direction == "left" && lastScrollPosition <5){
    lastScrollPosition += 1;
    console.log("New Position " + lastScrollPosition);
    changeImage(document.getElementById(lastScrollPosition));
  } else if (direction == "right" && lastScrollPosition >1) {
    lastScrollPosition -= 1;
    console.log("New Position " + lastScrollPosition);
    changeImage(document.getElementById(lastScrollPosition));
  }
  // Do something with the direction of the swipe
  console.log("Swiped " + direction);

});