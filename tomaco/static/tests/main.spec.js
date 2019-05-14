import Timer from "../src/js/main";

describe("Timer", () => {
  let $fakeButton;
  let $fakeDisplay;
  let timer;
  let clearIntervalSpy;
  let setIntervalSpy;
  let timerIntervalSpy;

  beforeEach(() => {
    $fakeButton = {
      on: jest.fn(),
      text: jest.fn()
    };
    $fakeDisplay = {
      text: jest.fn()
    };

    timer = new Timer($fakeDisplay, $fakeButton);

    clearIntervalSpy = jest.spyOn(global, "clearInterval");
    setIntervalSpy = jest.spyOn(global, "setInterval");
    timerIntervalSpy = jest.spyOn(timer.timerInterval, "bind");

    timer.init();
  });

  describe("init", () => {
    it("should reset the timer", () => {
      expect(timer.isRunning).toBe(false);
      expect($fakeButton.text).toHaveBeenCalledWith("Start!");
      expect($fakeDisplay.text).toHaveBeenCalledWith("25:00");
    });

    it("should bind a click event to $button element", () => {
      expect($fakeButton.on).toHaveBeenCalled();
    });
  });

  describe("updateDisplay", () => {
    it("should print seconds in the minutes format", () => {
      timer.updateDisplay(1500);
      expect($fakeDisplay.text).toHaveBeenCalledWith("25:00");
    });

    it("should respect the limit of 60 for seconds", () => {
      timer.updateDisplay(1499);
      expect($fakeDisplay.text).toHaveBeenCalledWith("24:59");
    });

    it("should pad a zero to the left of the minute so we will always have two numbers", () => {
      timer.updateDisplay(60);
      expect($fakeDisplay.text).toHaveBeenCalledWith("01:00");
    });

    it("should pad a zero to the left of the second so we will always have two numbers", () => {
      timer.updateDisplay(5);
      expect($fakeDisplay.text).toHaveBeenCalledWith("00:05");
    });
  });

  describe("resetTimer", () => {
    it("should clear the interval engine", () => {
      timer.resetTimer();

      expect(clearIntervalSpy).toHaveBeenCalled();
    });

    it("should set timer as it's initial state", () => {
      timer.resetTimer();

      expect(timer.isRunning).toBe(false);
      expect($fakeButton.text).toHaveBeenCalledWith("Start!");
    });

    it("should update the display with the initial amount of seconds", () => {
      timer.resetTimer();
      expect($fakeDisplay.text).toHaveBeenCalledWith("25:00");
    });
  });

  describe("toggleTimer", () => {
    it("should set the state as running mode, if it is not running already", () => {
      timer.resetTimer(); // Make sure it's not running
      timer.toggleTimer();

      expect(timer.isRunning).toBe(true);
      expect($fakeButton.text).toHaveBeenCalledWith("Stop!");
    });

    it("should triggers the interval engine", () => {
      timer.resetTimer(); // Make sure it's not running
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
      expect($fakeDisplay.text).toHaveBeenCalledWith("24:59");
    });

    it("should reset the timer when it reaches zero", () => {
      timer.seconds = 1;
      timer.timerInterval();

      expect(timer.isRunning).toBe(false);
    });
  });
});
