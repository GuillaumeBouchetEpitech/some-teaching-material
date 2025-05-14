
window.addEventListener("load", () => {

  console.log("the page is now loaded");

  // get and save the pages's useful parts (buttons and "result area")
  const results = document.querySelector("#results");
  const addButton = document.querySelector("#add-button");
  const listButton = document.querySelector("#list-button");

  //
  //
  //

  const lisAllEntries = async () => {

    console.log("requesting the list of entries");

    results.innerHTML = "LOADING"; // empty the content

    // fetch the route
    const response = await fetch("/list-all?startIndex=0&maxSize=100");
    // ask the data as json payload (JS object)
    const jsonData = await response.json();

    console.log('jsonData', jsonData);

    // build an html table
    let newText = "";
    newText += "<table border=\"1\">";
    newText += "  <tr>"
    newText += `    <th>row-id</th>`
    newText += `    <th>first-name</th>`
    newText += `    <th>last-name</th>`
    newText += `    <th>age</th>`
    newText += "  </tr>"
    for (const data of jsonData.allData) {
      newText += "  <tr>"
      newText += `    <td>${data.rowId}</td>`
      newText += `    <td>${data.firstName}</td>`
      newText += `    <td>${data.lastName}</td>`
      newText += `    <td>${data.age}</td>`
      newText += `    <td><button onclick="deleteEntry(${data.rowId})">DELETE</button></td>`
      newText += "  </tr>"
    }
    newText += "</table>";

    // replace the HTML content
    results.innerHTML = newText;
  }

  //
  //
  //

  const addNewEntry = async () => {

    console.log("requesting new entry to be added");

    // fetch the route -> will not return any response
    await fetch("/add-new", {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ firstName: 'john', lastName: 'doe', age: 40 }),
    });

    // reuse the list function
    await lisAllEntries();
  }

  //
  //
  //

  // the use of the 'global' object 'window' will ensure we can access it from the table
  window.deleteEntry = async (rowId) => {

    console.log("requesting new entry to be removed", rowId);

    // fetch the route -> will not return any response
    await fetch("/delete-existing", {
      method: 'DELETE',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ rowId: rowId }),
    });

    // reuse the list function
    await lisAllEntries();
  }

  //
  //
  // ADD BUTTON

  addButton.addEventListener('click', addNewEntry);

  //
  //
  // LIST BUTTON

  listButton.addEventListener('click', lisAllEntries);

});
