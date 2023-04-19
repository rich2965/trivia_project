//// Used for filtering the genre 
var categorySelect = document.getElementById('genre-select');
var cards = document.querySelectorAll('.flashcard,.flashcard_movie,.flashcard_person,.flashcard_event');

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
  on: {
    slideChange: function () {
      var activeSlideIndex = this.activeIndex + 1;
      var totalSlides = this.slides.length;
      var counter = document.querySelector('.swiper-counter');
      counter.textContent = activeSlideIndex + '/' + totalSlides;
    }
  }
});

///Calling Google Maps

// create an object containing all variables you want to store in localstorage
var mapConfig = {
  show_cities: "off",
  show_landscape: "off"
};
console.log(mapConfig)


// Check to see if mapConfig exists in localStorage
if (localStorage.getItem("mapConfig") !== null) {
  // retrieve the JSON string from localStorage
  var mapConfigString = localStorage.getItem("mapConfig");
  console.log(mapConfigString)
  // convert the JSON string back to an object
  var mapConfig_prev = JSON.parse(mapConfigString);
  mapConfig.show_cities = mapConfig_prev.show_cities;
  mapConfig.show_landscape = mapConfig_prev.show_landscape;
  console.log(mapConfig)
}

// check the value of "show_cities" and set the toggle button state accordingly
if (mapConfig.show_cities === "on") {
  // set the toggle button to the "on" state
  document.querySelector(".toggle-cities").checked = true;
} else {
  // set the toggle button to the "off" state
  document.querySelector(".toggle-cities").checked = false;
}

// check the value of "show_landscape" and set the toggle button state accordingly
if (mapConfig.show_landscape === "on") {
  // set the toggle button to the "on" state
  document.querySelector(".toggle-landscape").checked = true;
} else {
  // set the toggle button to the "off" state
  document.querySelector(".toggle-landscape").checked = false;
}

function initMap() {
  var latitude = parseFloat(document.getElementById('mapContainer').getAttribute('data-latitude'));
  var longitude = parseFloat(document.getElementById('mapContainer').getAttribute('data-longitude'));
  var location = {lat: latitude, lng: longitude}; 
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 5,
    center: location,
    streetViewControl: false,
    mapTypeControl: false,
    fullscreenControl: false,
    zoomControl: false,
    disableDefaultUI: true, // Disable default UI
    keyboardShortcuts: false, // Disable keyboard shortcuts
    mapTypeControlOptions: {
      mapTypeIds: []
    }, // Remove "Terms of Use" link
    styles: [
    {
      featureType: "all",
      elementType: "labels",
      stylers: [
        { visibility: "off" }
      ]
    },
    {
      featureType: "all",
      elementType: "geometry",
      stylers: [
        { visibility: "on" }
      ]
    },
      {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [{visibility: 'off'}]
      },
      {
        featureType: 'administrative.province',
        elementType: 'geometry.stroke',
        stylers: [{visibility: 'off'}]
      },
      {
        featureType: 'administrative.locality',
        elementType: 'geometry.stroke',
        stylers: [{visibility: 'off'}]
      },
      {
        featureType: 'administrative.country',
        elementType: 'geometry.stroke',
        stylers: [{color: '#000000'}, {weight: 2}]
      },
      {
        featureType: "administrative.country",
        elementType: "labels",
        stylers: [
          { visibility: "off" }
        ]
      },
      {
        featureType: "administrative.locality",
        elementType: "labels",
        stylers: [
          { visibility: mapConfig.show_cities }
        ]
      },
      {
        featureType: "landscape.natural",
        elementType: "labels",
        stylers: [
          { visibility: mapConfig.show_landscape }
        ]
      },
      {
        featureType: "water",
        elementType: "labels",
        stylers: [
          { visibility: mapConfig.show_landscape }
        ]
      }
  ]

  });
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
  /// Set the map config values into localstorage
  var mapConfigString = JSON.stringify(mapConfig);
  localStorage.setItem("mapConfig", mapConfigString);
  console.log(mapConfigString)
}
initMap();