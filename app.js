// Browser-side JavaScript for microphone access
async function startRealTimeTranscription() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const audioContext = new AudioContext();
    const source = audioContext.createMediaStreamSource(stream);
    
    // Process audio chunks and send to your backend
    const processor = audioContext.createScriptProcessor(4096, 1, 1);
    source.connect(processor);
    processor.connect(audioContext.destination);
    
    processor.onaudioprocess = async (e) => {
      const audioData = e.inputBuffer.getChannelData(0);
      // Send audio chunk to your Whisper backend
      const transcription = await sendAudioToBackend(audioData);
      displayTranscription(transcription);
    };
  } catch (error) {
    console.error("Error accessing microphone:", error);
  }
}