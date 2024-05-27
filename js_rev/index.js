// let p1 = new Promise((res, rej) => {
//   setTimeout(() => {
//     rej("p1 rejected ");
//   }, 3000);
// });

// setTimeout(() => {
//   console.log(p1);
// }, 4000);

// Promise is an object which is used to handle success and failiure of an asynchronous operation

// let p1 = new Promise((res, rej) => {
//   setTimeout(() => {
//     // res("p1 sesolved ");
//     rej(10 + 5);
//   }, 3000);
// });

// p1.then(a => {
//   console.log(a);
// }).catch(err => {
//   console.log(err);
// });

// let api = fetch("https://api.github.com/users");
// let root = document.getElementById("root");
// let ol = document.querySelector("ol");
// console.log(ol);
// api.then(a => {
//   console.log("before json()", a);
//   let y = a.json();
//   console.log(y);
//   y.then(b => {
//     b.map(ele => {
//       //   console.log(ele.login);
//       ol.innerHTML += `<li>${ele.login}</li>`;
//       //   document.body.innerHTML += ele.avatar_url;
//       //   root.innerHTML += `<img src="${ele.avatar_url}" alt="">`;
//     });
//   }).catch(err => {
//     console.log(err);
//   });
// });

async function handleapi() {
  let fetching = await fetch("https://api.github.com/users");
  // console.log(fetching);
  let ans = await fetching.json();
  console.log(ans);
}
handleapi();
