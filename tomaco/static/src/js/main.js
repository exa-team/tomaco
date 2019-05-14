const ONE_SECOND = 1 * 1000;
const STARTING_FROM = 25 * 60;
const START_TEXT = "Start!";
const STOP_TEXT = "Stop!";

export default class Timer {
  constructor($display, $button, startingFrom = STARTING_FROM) {
    this.$display = $display;
    this.$button = $button;
    this.isRunning = false;
    this.timer = null;
    this.startingFrom = startingFrom;
    this.seconds = startingFrom;
  }

  init() {
    this.resetTimer();
    this.$button.on("click", this.toggleTimer.bind(this));
  }

  updateDisplay(seconds) {
    const formattedMinutes = Timer.pad(Math.floor(seconds / 60));
    const formattedSeconds = Timer.pad(seconds % 60);
    this.$display.text(`${formattedMinutes}:${formattedSeconds}`);
  }

  resetTimer() {
    clearInterval(this.timer);

    this.isRunning = false;
    this.$button.text(START_TEXT);
    this.updateDisplay(this.startingFrom);
  }

  toggleTimer() {
    if (this.isRunning) {
      this.resetTimer();
      return;
    }

    this.isRunning = true;
    this.$button.text(STOP_TEXT);
    this.timer = window.setInterval(this.timerInterval.bind(this), ONE_SECOND);
  }

  timerInterval() {
    if (this.seconds <= 0) {
      this.resetTimer();
      M.toast({
        html: "Pomodoro done! :)"
      });

      return;
    }

    this.seconds -= 1;
    this.updateDisplay(this.seconds);
  }

  static pad(numberToPad) {
    return numberToPad.toString().length < 2 ? `0${numberToPad}` : numberToPad;
  }
}
