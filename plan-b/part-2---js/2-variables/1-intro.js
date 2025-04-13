
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

// a "var" defined variable is accessible globally from everywhere,
// which is making everything very complicated as a var with the same name
// could be re-defined elsewhere and create a very confusing source code





//
// CONST
//

const newWayToDeclare1 = 333

// CANNOT be reassigned
// newWaytToDeclare1 = 777; // this would throw an error at runtime

// the keyword "const" SHOULD be sued whenever it is possible to do so
// -> Why -> it can prevent human errors, some values MUST never change




//
// LET
//

let newWaytToDeclare2 = 333; // number

// CAN be reassigned
newWaytToDeclare2 = 777; // number

// reassigned again
newWaytToDeclare2 = "hello?"; // string

// the keyword "let" is behaving like "var" except it's only accessible locally


