// Get the URL parameters
const urlParams = new URLSearchParams(window.location.search);

// Get the 'room' parameter from the URL
const roomNumber = urlParams.get('room');

// Select the span element with the id 'room-number'
const roomNumberElement = document.getElementById('room-number');

// Update the content with the room number
if (roomNumber) {
  roomNumberElement.textContent = roomNumber;
} else {
  roomNumberElement.textContent = 'Unknown';
}
