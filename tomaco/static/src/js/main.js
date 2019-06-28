import secondsToMinutesAndSeconds from "./utils";

const ONE_SECOND = 1 * 1000;
const FOCUS_STARTING_FROM = 25 * 60;
const BREAK_STARTING_FROM = 5 * 60;
const START_TEXT = "Start!";
const STOP_TEXT = "Stop!";

export default class Timer {
  constructor($display, $button, $finishedCounter) {
    this.$display = $display;
    this.$button = $button;
    this.$finishedCounter = $finishedCounter;

    this.seconds = FOCUS_STARTING_FROM;
    this.focusMode = true;
    this.isRunning = false;
    this.timer = null;
    this.finishedPomodoros = 0;

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
    this.$finishedCounter.innerHTML = Array.from({
      length: this.finishedPomodoros
    }).reduce(
      accumulator =>
        `${accumulator} <span class="timer__finished_item"></span>`,
      ""
    );
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

  setPomodoroAsDone() {
    this.toggleFocusTime();
    this.stopTimer();
    this.finishedPomodoros += 1;

    M.toast({
      html: "Pomodoro done! :)"
    });
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
      this.setPomodoroAsDone();
    } else {
      this.seconds -= 1;
    }

    this.updateUI();
  }

  static build($display, $button, $finishedCounter) {
    const timer = new Timer($display, $button, $finishedCounter);
    timer.stopTimer();
    timer.updateUI();

    return timer;
  }
}
