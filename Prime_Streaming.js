function isPrime(num) {
    if (num == 3 || num == 2 || num == 5)
        return true
    let prime = false;


    if ((num) % 6 == 1 || (num) % 6 == 5)
        prime = true;
    // if (num % 5 == 0)
    //     prime = false

    return prime;

}


function sieve(n) {
    limit = parseInt(Math.sqrt(n))
    temp = 0
    nos = []
    lst = []
    while (temp < n) {
        nos.push(temp);
        temp++;
    }
    for (i = 2; i <= limit; i++) {
        temp = i
        k = 2
        while (temp * k < n) {
            if (nos[temp * k] != true)
                nos[temp * k] = true;
            ++k
        }
    }
    lst = nos.filter(item => item != true)
    return lst.slice(1)
}

class Primes {
    static * stream() {
        temp = sieve(200000)
            // replace this with your solution
        let n = 2;
        for (var item of temp)
            yield item
            //         while (true) {
            //             if (isPrime(n)) {
            //                 yield n;
            //             }
            //             ++n;
            //         }
    }
}


function verify(from_n, ...vals) {
    const stream = Primes.stream()
    for (let i = 0; i < from_n; ++i) stream.next()
    for (let v of vals) console.log(stream.next().value, v)
}


sieve(200)
verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)