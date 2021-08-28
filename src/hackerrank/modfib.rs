// https://www.hackerrank.com/challenges/fibonacci-modified/problem

use num::bigint::BigInt;
use utils;

pub fn modified_fib() {
    let v: Vec<i32> = utils::read_vec();
    let mut a = BigInt::from(v[0]);
    let mut b = BigInt::from(v[1]);
    let mut tmp: BigInt;

    let n = v[2] as usize;

    let result = if n == 1 {
        a
    } else if n == 2 {
        b
    } else {
        for _ in 0..(n - 2) {
            tmp = a.clone() + (b.clone() * b.clone());
            a = b;
            b = tmp;
        }
        b
    };

    println!("{}", result.to_str_radix(10));
}
