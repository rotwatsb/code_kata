const UPPER_BOUND: usize = 1000000;

pub fn circularprimes() {
    let mut primes: Vec<usize> = Vec::with_capacity(100000);
    primes.push(2);
    let mut x: usize = 3;
    while x < UPPER_BOUND {
        if is_prime(x, &primes) {
            primes.push(x);
        }
        x += 2;
    }

    let primes2 = primes.clone();
    let mut circular_primes: usize = 0;
    let mut num_digits: usize;
    let mut t: usize;
    let mut d: usize;
    'outer: for p in primes {
        num_digits = 0;
        t = p;
        loop {
            if t > 0 {
                num_digits += 1;
                t /= 10;
            } else {
                break;
            }
        }

        t = p;
        for _i in 1..num_digits {
            d = t % 10;
            t = t / 10;
            t = t + d * (10 as usize).pow(num_digits as u32 - 1);
            if let Err(_) = primes2[..].binary_search(&t) {
                continue 'outer;
            }
        }
        circular_primes += 1;
    }
    println!("{}", circular_primes);
}

fn is_prime(n: usize, primes: &Vec<usize>) -> bool {
    let max = (n as f64).sqrt() as usize;
    for v in primes {
        if *v > max {
            return true;
        } else if n % v == 0 {
            return false;
        }
    }
    true
}
