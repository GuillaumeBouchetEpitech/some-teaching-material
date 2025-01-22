
// 3 types of variable declaration

//
// VAR
//

var oldWayToDeclare = 333; // number

// CAN be reassigned
oldWayToDeclare = 777; // number

// reassigned again
oldWayToDeclare = "hello?"; // string

// the keyword "var" is old and should never be used ever again
// some side effect that are a bit confusing to explain can happen





//
// CONST
//

const newWaytToDeclare1 = 333

// CANNOT be reassigned
// newWaytToDeclare1 = 777; // this would throw an error at runtime

// it is good practice to use the keyword "const" whenever it is possible to do so
// -> Why -> it can prevent human errors, some values must never change




//
// LET
//

let newWaytToDeclare2 = 333; // number

// CAN be reassigned
newWaytToDeclare2 = 777; // number

// reassigned again
newWaytToDeclare2 = "hello?"; // string

// the keyword "let" is behaving like "var" minus the confusing side effects
// it is good practice to use "let" when "const" is not possible


