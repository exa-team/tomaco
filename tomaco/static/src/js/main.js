import secondsToMinutesAndSeconds from "./utils";

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

    this.$button.addEventListener("click", this.toggleTimer.bind(this));
  }

  updateUI() {
    this.$button.innerHTML = this.isRunning ? STOP_TEXT : START_TEXT;
    this.$display.innerHTML = secondsToMinutesAndSeconds(this.seconds);
  }

  startTimer() {
    this.timer = window.setInterval(this.timerInterval.bind(this), ONE_SECOND);
    this.isRunning = true;
  }

  stopTimer() {
    clearInterval(this.timer);
    this.seconds = STARTING_FROM;
    this.isRunning = false;
  }

  toggleTimer() {
    if (this.isRunning) {
      this.stopTimer();
    } else {
      this.startTimer();
    }

    this.updateUI();
  }

  timerInterval() {
    if (this.seconds <= 0) {
      this.stopTimer();
      M.toast({
        html: "Pomodoro done! :)"
      });
    } else {
      this.seconds -= 1;
    }

    this.updateUI();
  }

  static build($display, $button) {
    const timer = new Timer($display, $button);
    timer.stopTimer();
    timer.updateUI();

    return timer;
  }
}
