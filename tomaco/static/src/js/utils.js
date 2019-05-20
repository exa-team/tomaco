const pad = numberToPad =>
  numberToPad.toString().length < 2 ? `0${numberToPad}` : numberToPad;

const secondsToMinutesAndSeconds = seconds => {
  const formattedMinutes = pad(Math.floor(seconds / 60));
  const formattedSeconds = pad(seconds % 60);
  return `${formattedMinutes}:${formattedSeconds}`;
};

export default secondsToMinutesAndSeconds;