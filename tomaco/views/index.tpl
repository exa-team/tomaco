<!doctype html>
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8">
  <title>Tomaco - Your friendly Pomodoro tracker</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#fafafa">

  <link rel="styleshet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link rel="stylesheet" href="/static/build/main.css">
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
  <script src="/static/build/main.js"></script>
  <script>
    const Timer = require('tomaco/static/src/js/main.js').default;

    $(document).ready(() => {
      const timer = new Timer($('#timer__display'), $('#timer__button'));
      timer.init();
    });
  </script>
 </body>

</html>
