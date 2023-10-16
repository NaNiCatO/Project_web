const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied');
const count = document.getElementById('count');
const total = document.getElementById('total');
const CoSeatSelect = document.getElementById('CoSeat');
const confirmButton = document.getElementById('confirm-button');


populateUI();

function setCoSeatData(CoSeatIndex) {
  localStorage.setItem('selectedCoSeatIndex', CoSeatIndex);
}

function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.row .seat.selected');

  const seatsIndex = [...selectedSeats].map((seat) => [...seats].indexOf(seat));

  localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

  //copy selected seats into arr
  // map through array
  //return new array of indexes

  const selectedSeatsCount = selectedSeats.length;

  count.innerText = selectedSeatsCount;
}

// get data from localstorage and populate ui
function populateUI() {
  const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
  if (selectedSeats !== null && selectedSeats.length > 0) {
    seats.forEach((seat, index) => {
      if (selectedSeats.indexOf(index) > -1) {
        seat.classList.add('selected');
      }
    });
  }

  const selectedCoSeatIndex = localStorage.getItem('selectedCoSeatIndex');

  if (selectedCoSeatIndex !== null) {
    CoSeatSelect.selectedIndex = selectedCoSeatIndex;
  }
}

// CoSeat select event
CoSeatSelect.addEventListener('change', (e) => {
  setCoSeatData(e.target.selectedIndex, e.target.value);
  updateSelectedCount();
});

// Seat click event
container.addEventListener('click', (e) => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');

    updateSelectedCount();
  }
});

updateSelectedCount();


confirmButton.addEventListener('click', () => {
    // Mark selected seats as occupied
    const selectedSeats = document.querySelectorAll('.row .seat.selected');
    selectedSeats.forEach((seat) => {
      seat.classList.remove('selected');
      seat.classList.add('occupied');
    });
  
    const selectedSeatsCount = selectedSeats.length;
  
    // Display a confirmation message using alert
    alert("You have successfully booked the seat for " + selectedSeatsCount + " seats");
  
    updateSelectedCount();
  });
  
  function updateSelectedCount() {
    const selectedSeats = document.querySelectorAll('.row .seat.selected');
    const selectedSeatsCount = selectedSeats.length;
  
    count.innerText = selectedSeatsCount;
  }