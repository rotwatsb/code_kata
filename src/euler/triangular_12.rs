use std::f64;
use std::cmp;

pub fn solve() {
    let mut i: usize = 2;
    let mut tri_num: usize = 1;
    let mut max: usize = 0;
    let mut v: usize = 0;
    loop {
        v = num_factors(tri_num);
        if v > max {
            max = v;
            println!("{}", max);
            if max > 500 {
                break;
            }
        }
        i += 1;
        tri_num += i;
    }
    println!("{} has +500 factors", tri_num);
}

fn num_factors(n: usize) -> usize {
    let mut i: usize = 1;
    let mut factors: usize = 0;
    let max_factor: usize = f64::sqrt(n as f64) as usize;
    while i < max_factor {
        if n % i == 0 {
            factors += 2;
        }
        i += 1;
    }
    factors
}
