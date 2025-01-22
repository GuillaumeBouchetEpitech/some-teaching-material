

# How does "the web" work

## Part 1
### How does the internet works

```mermaid

flowchart
  browser[browser]

  subgraph internet
    webserver[web server]
  end

  browser <-- network --> webserver

```

## Part 2:
### Get an html file to render in the browser

```mermaid

flowchart
  browser[browser]

  subgraph internet
    webserver[web server]
  end

  browser -- "#1
  http request
  GET index.html" ---> webserver

  webserver -. "#2
  http response
  give index.html file content" ...-> browser

```



# job types: overview

```mermaid

flowchart
  backend[back end]
  frontend[front end]
  fullstack[full stack]

  backend --> fullstack
  frontend --> fullstack
```

# Focus on frontend

```mermaid

flowchart

  browser([browser])

  html["
  HTML
  _
  the 'skeleton' of the website
  _
  ex: titles, texts, buttons, tables, etc.
  "]

  css["
  CSS
  _
  the 'makeup' of the website
  _
  ex: colors, front types, font sizes, etc.
  "]

  javascript["
  JavasSript
  _
  the 'brain' of the website
  _
  ex: action when click on a button, server requests, etc.
  "]

  browser -- load --> html -- load --> css & javascript

```

# Focus on backend


```mermaid

flowchart

  browser(["browser"])

  webserver["
  Web Server
  _
  accept and process
  users' request(s)
  "]

  database[(database)]

  webserver2["
  Another Web Server
  _
  accept and process
  services' request(s)
  "]


  browser -- request data --> webserver
  webserver -. reply data .-> browser

  webserver -- query data (SQL) --> database
  database -. get result as tables .-> webserver

  webserver -- request data ----> webserver2
  webserver2 -. reply data payload ...-> webserver

```


# Deeper Focus on backend


```mermaid

flowchart


  user(("user"))

  browser(["browser"])

  user -- "want to shop on the website" --> browser



  entry_webserver["
  Web Server
  _
  serve the website
  connect the user to other services
  "]

  browser -- load page --> entry_webserver






  items_sold_webserver["
  Web Server
  Products Service
  _
  list items by name
  list items by categories
  list items with a search by name
  etc.
  "]

  items_sold_database[("
  Database
  _
  All Item(s) Sold
  -> bike, TVs, etc.
  _
  item name
  item price
  item stock left
  ")]

  items_sold_webserver <--> items_sold_database
  entry_webserver <-- "user want to search and list the items sold, can be sorted by category, prices, etc.
  " --> items_sold_webserver




  user_service["
  Web Server
  Users Service
  _
  register users
  authenticate users (login)
  logout users
  delete users
  "]

  users_database[("Database
  _
  Contains
  registered
  Users
  _
  user name
  delivery address
  phone number")]

  entry_webserver <-- "users want to register/login to their account" --> user_service

  user_service <--> users_database







  basket_service["
  Web Server
  Baskets Service
  _
  register users
  authenticate users (login)
  logout users
  delete users
  "]

  basket_database[("Database
  _
  Contains
  Users Baskets
  _
  user name
  selected items and quantity
  ")]

  entry_webserver <-- "the user create a basket and fill it with items to buy" --> basket_service

  basket_service <---> basket_database


  basket_service -.-> user_service
  basket_service -.-> items_sold_webserver




```

