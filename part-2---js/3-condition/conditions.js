

if (true) {
  // will run
}

if (false) {
  // will not run
}






if (1 < 2) {
  // will run
}

if (1 > 2) {
  // will not run
}

if (3 == 3) {
  // will run
}

if (3 == 3) {
  // will not run
}





if (true) {
  // will run
} else {
  // will not run
}

if (false) {
  // will not run
} else {
  // will run
}






if (false) {
  // will not run
} else if (true) {
  // will run
} else {
  // will not run
}




// complex conditions

if (false && true) { // false AND true
  // will not run
} else if (false || true) { // false OR true
  // will run
} else {
  // will not run
}





// ternary conditions
const value1 = true ? "yes" : "no"; // -> value1 is "yes"
const value2 = false ? "yes" : "no"; // -> value2 is "no"



// ugly ternary conditions
const value3 = false ? "yes" : true ? "maybe" : "no"; // -> value1 is "maybe"

// less ugly ternary conditions
const value4 = (false ? "yes" : (true ? "maybe" : "no")); // -> value1 is "maybe"








// concrete example

const userIsAuthenticated = true;
const userIsPaidUser = true;

if (!userIsAuthenticated) {
  console.log("forbidden");
} else if (userIsAuthenticated && userIsPaidUser) {
  console.log("welcome sir");
} else {
  console.log("welcome");
}







