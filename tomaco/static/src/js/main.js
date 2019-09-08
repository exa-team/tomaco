import { fetch } from "whatwg-fetch";
import {
  BREAK_STARTING_FROM,
  FOCUS_STARTING_FROM,
  INTERVAL,
  MESSAGES,
  ONE_SECOND,
  PAUSE_TEXT,
  RESUME_TEXT,
  START_TEXT,
  STOP_TEXT
} from "./constants";
import { notify, secondsToMinutesAndSeconds } from "./utils";

export default class Timer {
  constructor($display, $button, $finishedCounter, $pauseButton) {
    this.$display = $display;
    this.$button = $button;
    this.$finishedCounter = $finishedCounter;
    this.$pauseButton = $pauseButton;
    this.seconds = FOCUS_STARTING_FROM;
    this.focusMode = true;
    this.isRunning = false;
    this.isPaused = false;
    this.timer = null;
    this.finishedPomodoros = 0;

    this.$button.addEventListener("click", this.toggleTimer.bind(this));
    this.$pauseButton.addEventListener(
      "click",
      this.togglePauseTimer.bind(this)
    );
  }

  updateUI() {
    if (this.focusMode) {
      this.$button.classList.add("red");
      this.$button.classList.remove("green");
    } else {
      this.$button.classList.add("green");
      this.$button.classList.remove("red");
    }

    // updating main button
    this.$button.innerHTML = this.isRunning ? STOP_TEXT : START_TEXT;

    // updating break time button
    if (this.isRunning) {
      this.$pauseButton.disabled = false;
      this.$pauseButton.innerText = this.isPaused ? RESUME_TEXT : PAUSE_TEXT;
    } else {
      this.$pauseButton.disabled = true;
      this.$pauseButton.innerText = PAUSE_TEXT;
    }

    this.setTimerTitle();

    // updatime time
    this.$display.innerHTML = secondsToMinutesAndSeconds(this.seconds);
    this.$finishedCounter.innerHTML = Array.from({
      length: this.finishedPomodoros
    }).reduce(
      accumulator =>
        `${accumulator} <span class="timer__finished_item"></span>`,
      ""
    );
  }

  setTimerTitle() {
    if (!document.originalTitle) {
      // Why not store the original title in this object? Because document must
      // be the responsable for its own title
      document.originalTitle = document.title;
    }

    if (this.isRunning) {
      const seconds = secondsToMinutesAndSeconds(this.seconds);
      document.title = `${seconds} - ${document.originalTitle}`;
    } else {
      document.title = document.originalTitle;
    }
  }

  startTimer() {
    this.timer = window.setInterval(this.timerInterval.bind(this), ONE_SECOND);
    this.isRunning = true;
  }

  stopTimer() {
    clearInterval(this.timer);
    this.seconds = this.focusMode ? FOCUS_STARTING_FROM : BREAK_STARTING_FROM;
    this.isRunning = false;
    this.isPaused = false;
  }

  togglePauseTimer() {
    if (!this.isRunning) {
      return; // only toggle if pommodoro is running
    }

    // recreate setInterval avoids unnecessary processing
    if (this.isPaused) {
      this.startTimer();
    } else {
      clearInterval(this.timer);
    }

    this.isPaused = !this.isPaused;
    this.updateUI();
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
    let message;

    if (this.focusMode) {
      Timer.recordProgress(INTERVAL.POMODORO);
      this.finishedPomodoros += 1;
      message = MESSAGES.FOCUS_MODE_DONE;
    } else {
      Timer.recordProgress(INTERVAL.BREAK);
      message = MESSAGES.REST_MODE_DONE;
    }

    this.toggleFocusTime();
    this.stopTimer();

    notify(message);
  }

  static recordProgress(type) {
    fetch("/interval", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ type })
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

  static build($display, $button, $finishedCounter, $pauseButton) {
    const timer = new Timer($display, $button, $finishedCounter, $pauseButton);
    timer.stopTimer();
    timer.updateUI();

    return timer;
  }
}
