const order = new Promise((res, rej) => {
    setTimeout(() => {
        res("ordered")
        // rej("order rejected")
    }, 1000);
})

const pay = new Promise((res, rej) => {
    setTimeout(() => {
        res('payment done')
        // rej('pay rejected')
    }, 5000)
})

async function vaibhavi() {
    try {
        console.log('function start');
        await pay.then(data2 => {
            console.log(data2);
        })

        // .catch(err => {
        //     console.log('payment catch', err);
        // })

        await order.then(data => {
            console.log(data);
        })

        // .catch(err => {
        //     console.log('order catch', err);
        // })
    }
    catch (err) {
        console.log(err);
    }


}

vaibhavi()
console.log('after function call');