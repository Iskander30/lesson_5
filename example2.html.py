<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page1</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
<a href="page2.html" target="blank">Ссылка на страницу 2</a>
<p class="lead">
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias at deleniti eos error ipsum laboriosam mollitia nisi
nobis nulla obcaecati, quia quidem quisquam quo quod suscipit velit voluptatum. Consectetur, molestiae?
</p>
<form action="">
    <label for="field_1" class="lead">Введите ваше имя:</label>
    <input type="text" id="field_1" class="form-control form-control-lg"><br>
    <label for="field_2">Чек-бокс:</label>
    <input type="checkbox" id="field_2 class="lead"" class="form-check-input" ><br>
    <label for="field_3" class="lead">Введите ваше пароль:</label>
    <input type="password" id="field_3" class="form-control form-control-sm"><br>
    <input type="button" value="Отправить форму" class="btn btn-warning"><br>
    <textarea name="text" cols="60" rows="3" placeholder="Напишите ваши впечатления о сайте"></textarea
</form>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</body>
</html>