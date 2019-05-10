<!doctype html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <title>Tomaco - Your friendly Pomodoro tracker</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fafafa">

  <link rel="styleshet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link rel="stylesheet" href="/static/css/main.css">
</head>

<body>
  <nav>
    <div class="nav-wrapper">
      <a href="#" class="brand-logo center">Tomaco</a>
    </div>
  </nav>

  <div class="container">
    <div class="timer">
      <span class="timer__display" id="timer__display">25:00</span>
      <button class="waves-effect waves-light btn-large red lighten-2 timer__button" id="timer__button">Start!</button>
    </div>
  </div>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>

  <script>
    $(document).ready(() => {
      const oneSecond = 1 * 1000;
      const $display = $('#timer__display');
      const $button = $('#timer__button');

      const pad = (v) => v.toString().length < 2 ? `0${v}` : v;

      const updateTimer = (seconds) => {
        const min = pad(Math.floor(seconds / 60));
        const sec = pad(seconds % 60);

        $display.text(`${min}:${sec}`);
      };

      const resetTimer = () => {
        clearInterval(timer);
        isTimerRunning = false;
        seconds = 25 * 60;

        $button.text('Start!');
        updateTimer(seconds);
      }

      let timer;
      let isTimerRunning;
      let seconds;

      resetTimer();

      $button.click(() => {
        if (isTimerRunning) {
          resetTimer();
        } else {
          isTimerRunning = true;
          $button.text('Stop!');

          timer = window.setInterval(() => {
            if (seconds == 0) {
              resetTimer();
              M.toast({
                html: 'Pomodoro done! :)'
              });
              return;
            }

            seconds -= 1;
            updateTimer(seconds);
          }, oneSecond);
        }
      });
    });
  </script>
</body>

</html>
