const pad = numberToPad =>
  numberToPad.toString().length < 2 ? `0${numberToPad}` : numberToPad;

export const secondsToMinutesAndSeconds = seconds => {
  const formattedMinutes = pad(Math.floor(seconds / 60));
  const formattedSeconds = pad(seconds % 60);
  return `${formattedMinutes}:${formattedSeconds}`;
};

export function notify(message) {
  if (window.M) {
    M.toast({ html: message });
  }

  if (window.Notification && Notification.permission === "granted") {
    const notification = new Notification(message);

    // open Tomaco's page on click in notification popup
    notification.onclick = event => {
      event.preventDefault();
      window.focus();
    };
  }
}
