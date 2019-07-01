<!DOCTYPE html>
<html class="no-js" lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Tomaco - Your friendly Pomodoro tracker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="apple-touch-icon" sizes="180x180" href="/static/src/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/src/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/src/images/favicon-16x16.png">
    <link rel="manifest" href="/static/src/images/site.webmanifest">
    <link rel="mask-icon" href="/static/src/images/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#fafafa">

    <link
      rel="styleshet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"
    />
    <link rel="stylesheet" href="/static/build/main.css" />
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
        <button
          class="waves-effect waves-light btn-large red lighten-2 timer__button"
          id="timer__button"
        >
          Start!
        </button>
        <button
          class="waves-effect waves-light btn-large blue lighten-2 pause__button"
          id="pause__button"
          disabled
        >
          Pause!
        </button>
        <div class="timer__finished_counter" id="timer__finished_counter"></div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script src="/static/build/main.js"></script>
    <script>
      const Timer = require("tomaco/static/src/js/main.js").default;
      const $display = document.getElementById("timer__display");
      const $button = document.getElementById("timer__button");
      const $finishedCounter = document.getElementById("timer__finished_counter");
      const $pauseButton = document.getElementById("pause__button");

      Timer.build($display, $button, $finishedCounter, $pauseButton);
    </script>
  </body>
</html>
