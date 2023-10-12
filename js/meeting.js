function mic() {
    var image = document.getElementById("mic");
    if (image.src.match("image/mic.png")) {
      image.src = "image/mute.png";
    } else {
      image.src = "image/mic.png";
    }
}
  
function hand() {
    var image = document.getElementById("hand");
    if (image.src.match("image/hand.png")) {
      image.src = "image/raise.png";
    } else {
      image.src = "image/hand.png";
    }
}


const peerConnections = [];
const remoteVideosDiv = document.getElementById('remoteVideos');

// Function to create a new peer connection and add it to the array
function createPeerConnection(userId, stream) {
    const peerConnection = new RTCPeerConnection(configuration);

    // Add your signaling logic to exchange offer/answer and ICE candidates

    // Add the stream to the peer connection
    stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));

    // Handle remote video stream when it's received
    peerConnection.ontrack = event => {
        const video = document.createElement('video');
        video.srcObject = event.streams[0];
        video.autoplay = true;
        video.playsinline = true;
        remoteVideosDiv.appendChild(video);
    };

    peerConnections[userId] = peerConnection;
}

// Function to remove a peer connection and associated video element
function removePeerConnection(userId) {
    if (peerConnections[userId]) {
        peerConnections[userId].close();
        delete peerConnections[userId];

        const video = remoteVideosDiv.querySelector(`video[data-user="${userId}"]`);
        if (video) {
            video.srcObject.getTracks().forEach(track => track.stop());
            video.remove();
        }
    }
}


async function setupVideo() {
  try {
      const localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      const localVideo = document.getElementById('localVideo');
      localVideo.srcObject = localStream;
  } catch (error) {
      console.error('Error accessing camera and microphone:', error);
  }
}

setupVideo();