// let obj = {
//   name: "anand",
// };

// function getname(message, gender) {
//   return this.name + "is" + message + gender;
// }

// let binding = getname.bind(obj, "good", "man");
// console.log(binding());

var x = "case uh kaaranglae naanga than da";

function findgas() {
  let x = "im fake";
  console.log(x);
}
// findgas();

// function makeFunc() {
//   const namee = "Mozilla";
//   function displayNamee() {
//     console.log(namee);
//   }
//   return displayNamee;
// }

// const myFunc = makeFunc();
// myFunc();
// console.log(namee);

// function outer() {
//   let x = "from outer";
//   console.log("in outer function");
//   function inner() {
//     console.log("accessinng x from inner func", x);
//   }
//   return inner;
// }

// let call = outer();
// console.log("before call");
// console.log("going to call", call());
// console.dir(outer());

// function divideByHalf(sum) {
//   console.log(object);
// }

// function multiplyBy2(sum) {
//   console.log(sum * 2);
// }

// function operationOnSum(num1, num2, operation) {
//   var sum = num1 + num2;
//   operation(sum);
// }

// operationOnSum(3, 3, divideByHalf); // Outputs 3

// operationOnSum(5, 5, multiplyBy2); // Outputs 20

// function hell(sum) {
//   console.log(sum * 10);
// }

// let obj = {
//   name: "anand",
//   getpow() {
//     return 10;
//   },
// };

// console.log(obj.getpow());
function f(x) {
  x = "x-" + x;
  return function (y) {
    y = "y-" + x;
    return function (z) {
      return "z-" + y;
    };
  };
}
let g = f("a")("b")("c");
console.log(g);
