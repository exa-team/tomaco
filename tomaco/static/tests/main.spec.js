import Timer from "../src/js/main";

describe("Timer", () => {
  let $fakeButton;
  let $fakeCounter;
  let $fakeDisplay;
  let timer;
  let clearIntervalSpy;
  let setIntervalSpy;
  let timerIntervalSpy;

  beforeEach(() => {
    $fakeButton = {
      addEventListener: jest.fn(),
      classList: {
        add: jest.fn(),
        remove: jest.fn()
      },
      innerHTML: ""
    };
    $fakeCounter = {
      innerHTML: ""
    };
    $fakeDisplay = {
      innerHTML: ""
    };

    timer = Timer.build($fakeDisplay, $fakeButton, $fakeCounter);

    clearIntervalSpy = jest.spyOn(global, "clearInterval");
    setIntervalSpy = jest.spyOn(global, "setInterval");
    timerIntervalSpy = jest.spyOn(timer.timerInterval, "bind");

    global.M = {
      toast: jest.fn()
    };
  });

  describe("build", () => {
    it("should reset the timer", () => {
      expect(timer.isRunning).toBe(false);
      expect($fakeButton.innerHTML).toEqual("Start!");
      expect($fakeCounter.innerHTML).toEqual("");
      expect($fakeDisplay.innerHTML).toEqual("25:00");
    });

    it("should bind a click event to $button element", () => {
      expect($fakeButton.addEventListener).toHaveBeenCalled();
    });
  });

  describe("updateUI", () => {
    it("should print seconds in the minutes format", () => {
      timer.seconds = 1500;
      timer.updateUI();
      expect($fakeDisplay.innerHTML).toEqual("25:00");
    });

    it("should respect the limit of 60 for seconds", () => {
      timer.seconds = 1499;
      timer.updateUI();
      expect($fakeDisplay.innerHTML).toEqual("24:59");
    });

    it("should pad a zero to the left of the minute so we will always have two numbers", () => {
      timer.seconds = 60;
      timer.updateUI();
      expect($fakeDisplay.innerHTML).toEqual("01:00");
    });

    it("should pad a zero to the left of the second so we will always have two numbers", () => {
      timer.seconds = 5;
      timer.updateUI();
      expect($fakeDisplay.innerHTML).toEqual("00:05");
    });

    it("should print button with start text", () => {
      timer.isRunning = false;
      timer.updateUI();

      expect($fakeButton.innerHTML).toEqual("Start!");
    });

    it("should print button with stop text", () => {
      timer.isRunning = true;
      timer.updateUI();

      expect($fakeButton.innerHTML).toEqual("Stop!");
    });

    it("should be a focus button when in focus mode", () => {
      timer.setFocusTime();
      timer.updateUI();

      expect($fakeButton.classList.add).toHaveBeenCalledWith("red");
      expect($fakeButton.classList.remove).toHaveBeenCalledWith("green");
    });

    it("should be a rest button when it is not focus mode", () => {
      timer.setBreakTime();
      timer.updateUI();

      expect($fakeButton.classList.add).toHaveBeenCalledWith("green");
      expect($fakeButton.classList.remove).toHaveBeenCalledWith("red");
    });

    it("should add a visual element to inform the user that a session has been completed", () => {
      timer.setPomodoroAsDone();
      timer.updateUI();

      expect($fakeCounter.innerHTML).toContain(
        '<span class="timer__finished_item"></span>'
      );
    });
  });

  describe("resetTimer", () => {
    it("should clear the interval engine", () => {
      timer.stopTimer();

      expect(clearIntervalSpy).toHaveBeenCalled();
    });

    it("should set timer as it's initial state", () => {
      timer.stopTimer();

      expect(timer.isRunning).toBe(false);
      expect(timer.seconds).toEqual(1500);
    });
  });

  describe("toggleTimer", () => {
    it("should set the state as running mode, if it is not running already", () => {
      timer.stopTimer(); // Make sure it's not running
      timer.toggleTimer();

      expect(timer.isRunning).toBe(true);
      expect(timer.focusMode).toBe(true);
      expect($fakeButton.innerHTML).toEqual("Stop!");
    });

    it("should triggers the interval engine", () => {
      timer.stopTimer(); // Make sure it's not running
      timer.toggleTimer();

      expect(timer.timer).toBeTruthy();
      expect(setIntervalSpy).toHaveBeenCalled();
      expect(timerIntervalSpy).toHaveBeenCalledWith(timer);
    });

    it("should stop the interval engine if timer is already running", () => {
      timer.isRunning = true;
      timer.toggleTimer();

      expect(clearIntervalSpy).toHaveBeenCalled();
      expect(timer.isRunning).toBe(false);
    });
  });

  describe("timerInterval", () => {
    it("should decrease seconds by one, and display the result", () => {
      timer.timerInterval();

      expect(timer.seconds).toEqual(1499);
      expect($fakeDisplay.innerHTML).toEqual("24:59");
    });

    it("should reset the timer when it reaches zero", () => {
      timer.seconds = 0;
      timer.timerInterval();

      expect(timer.isRunning).toBe(false);
    });

    it("should set the rest mode when it reaches zero", () => {
      timer.seconds = 0;
      timer.timerInterval();

      expect(timer.focusMode).toBe(false);
      expect(timer.seconds).toEqual(300);
    });

    it("should show a toast when timer reaches zero", () => {
      timer.seconds = 0;
      timer.timerInterval();

      expect(M.toast).toHaveBeenCalledWith({
        html: "Pomodoro done! :)"
      });
    });

    it("should increase the finished counter", () => {
      timer.seconds = 0;
      timer.timerInterval();

      expect(timer.finishedPomodoros).toEqual(1);
    });
  });
});
