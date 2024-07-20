// How to Copy an Array With the Spread Operator
let studentNames = ["Daniel", "Jane", "Joe"];

let names = [...studentNames];

console.log(names); // ["Daniel","Jane","Joe"]

let arrObj = [{one:1,two:2,three:3},{1:'1',2:'2',3:'3'}]

let arrObj2 = [...arrObj]
console.log(arrObj2)

let studentNames1 = ["Daniel", "Jane", "Joe"];

let names1 = [];

studentNames1.map((name) => {
    names1.push(name);
});

console.log(names1); // ["Daniel","Jane","Joe"]