const container = document.querySelector(".container1");
const container2 = document.querySelector(".container2");
const container3 = document.querySelector(".container3");
const container4 = document.querySelector(".container4");
const RoomBarEL = document.getElementById("RoomBarEL");

const count = document.getElementById("count");
const CoSeatSelect = document.getElementById("CoSeat");
const seats = document.querySelectorAll(".row .seat");

showRoom(1);

function showRoom(roomNumber) {
  RoomBarEL.style.display = "flex";

  for (let i = 1; i <= 4; i++) {
    const roomEl = document.getElementById("Room" + i);
    console.log("roomEl =", roomNumber);
    const containerEl = document.getElementById("container" + i);
    if (i === roomNumber) {
      roomEl.style.display = "flex";
      containerEl.style.display = "flex";
      console.log("if container =", i);
    } else {
      roomEl.style.display = "flex";
      containerEl.style.display = "none";
      // console.log('else container =', i);
    }
  }

  updateSelectedCount();
}

function save_booking(username) {
  // Mark selected seats as occupied
  const selectedSeats = document.querySelectorAll(".row .seat.selected");
  // selectedSeats.forEach((seat) => {
  //   seat.classList.remove("selected");
  //   seat.classList.add("occupied");
  // });

  const selectedSeatsIndexes = [...selectedSeats].map(
    (seat) => [...seats].indexOf(seat)
  );

  const selectedSeatsCount = selectedSeats.length;

  // Display a confirmation message using alert
  if (selectedSeatsCount > 0) {
    // Check what div is currently visible
    let currentRoom = 1;
    for (let i = 1; i <= 4; i++) {
      const roomEl = document.getElementById("container" + i);
      if (roomEl.style.display !== "none") {
        currentRoom = i;
        break;
      }
    }

    fetch('/save_booking/' + username, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        roomnumber: currentRoom,
        selected_seat: selectedSeatsIndexes,
      })
    })
    .then(response => {
      if (response.ok){
        response.json().then(data => {
              if (data['message'] == "Booking successfully"){
                alert("You have successfully booked the seat for " + selectedSeatsCount + " seats");
                  location.reload();
                  return;
              }
          })
      }else{
          alert('An error occurred');
      }
  })
  }
  else {
    alert("Please select a seat to book");
  }

  updateSelectedCount();
}


container.addEventListener("click", (e) => {
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("occupied")
  ) {
    e.target.classList.toggle("selected");
    console.log("Selected");

    updateSelectedCount();
  }
  console.log("container");
});

container2.addEventListener("click", (e) => {
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("occupied")
  ) {
    e.target.classList.toggle("selected");
    console.log("Selected");

    updateSelectedCount();
  }
  console.log("container2");
});

// Seat click event
container3.addEventListener("click", (e) => {
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("occupied")
  ) {
    e.target.classList.toggle("selected");
    console.log("Selected");

    updateSelectedCount();
  }
  console.log("container3");
});

// Seat click event
container4.addEventListener("click", (e) => {
  if (
    e.target.classList.contains("seat") &&
    !e.target.classList.contains("occupied")
  ) {
    e.target.classList.toggle("selected");
    console.log("Selected");

    updateSelectedCount();
  }
  console.log("container4");
});

updateSelectedCount();

function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll(".row .seat.selected");
  const selectedSeatsCount = selectedSeats.length;

  count.innerText = selectedSeatsCount;
}
