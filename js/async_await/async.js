// async function one() {
//     return 'hello'
// }

// let data = one()
//     .then(a => {
//         console.log(a);
//     })

const p = new Promise((res, rej) => {
    setTimeout(() => {
        res('promise resolved')
    }, 10000);
})

const p1 = new Promise((res, rej) => {
    setTimeout(() => {
        res('promise resolved')
    }, 20000);
})

async function getdata() {
    console.log('getdata');
    await p.then((a) => {
        console.log(a);
    })
    await p1.then((a) => {
        console.log(a, '2nd promise res');
    })
    console.log('print');

    return 'returned'
}

getdata()
    .then(a => {
        console.log('getdata .then');
        console.log(a);
    })


console.log('after getdaata fun');