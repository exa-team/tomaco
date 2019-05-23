import secondsToMinutesAndSeconds from "./utils";

const ONE_SECOND = 1 * 1000;
const FOCUS_STARTING_FROM = 25 * 60;
const BREAK_STARTING_FROM = 5 * 60;
const START_TEXT = "Start!";
const STOP_TEXT = "Stop!";

export default class Timer {
  constructor($display, $button) {
    this.$display = $display;
    this.$button = $button;
    this.seconds = FOCUS_STARTING_FROM;
    this.focusMode = true;
    this.isRunning = false;
    this.timer = null;

    this.$button.addEventListener("click", this.toggleTimer.bind(this));
  }

  updateUI() {
    if (this.focusMode) {
      this.$button.classList.add("red");
      this.$button.classList.remove("green");
    } else {
      this.$button.classList.add("green");
      this.$button.classList.remove("red");
    }

    this.$button.innerHTML = this.isRunning ? STOP_TEXT : START_TEXT;
    this.$display.innerHTML = secondsToMinutesAndSeconds(this.seconds);
  }

  startTimer() {
    this.timer = window.setInterval(this.timerInterval.bind(this), ONE_SECOND);
    this.isRunning = true;
  }

  stopTimer() {
    clearInterval(this.timer);
    this.seconds = this.focusMode ? FOCUS_STARTING_FROM : BREAK_STARTING_FROM;
    this.isRunning = false;
  }

  toggleTimer() {
    if (this.isRunning) {
      this.setFocusTime();
      this.stopTimer();
    } else {
      this.startTimer();
    }

    this.updateUI();
  }

  setFocusTime() {
    this.focusMode = true;
  }

  setBreakTime() {
    this.focusMode = false;
  }

  toggleFocusTime() {
    if (this.focusMode) {
      this.setBreakTime();
    } else {
      this.setFocusTime();
    }
  }

  timerInterval() {
    if (this.seconds <= 0) {
      this.toggleFocusTime();
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
