let p1 = new Promise((res, rej) => {
    setTimeout(() => {
        // res('p1 res')
        rej('p1 rej')
    }, 3000);
})

let p2 = new Promise((res, rej) => {
    setTimeout(() => {
        // res('p2 res')
        rej('p2 rej')
    }, 3000);
})

let p3 = new Promise((res, rej) => {
    setTimeout(() => {
        // res('p3 res')
        rej('p3 rej')
    }, 3000);
})


Promise.any([p1, p2, p3])
    .then((res) => console.log(res))
    .catch(e => {
        console.error(e)
        console.log(e.errors);
    })