use num::bigint::BigInt;
use std::io;

use utils;

read_num_vec!(read_bigints, BigInt);

pub fn modified_fib() {
    let starts = read_bigints();
    let mut mod_fibs: Vec<BigInt> =
        vec![starts[0].clone(), starts[0].clone(), starts[1].clone()];
    let (sign, v) = starts[2].to_bytes_le();
    let n = v[0] as usize;
    let nth: BigInt = calc_mod_fib(n, &mut mod_fibs);
    println!("{}", nth);
}

fn calc_mod_fib(n: usize, mod_fibs: &mut Vec<BigInt>) -> BigInt {
    if mod_fibs.len() > n {
        mod_fibs[n].clone()
    }
    else {
        let x: BigInt =
            calc_mod_fib(n - 1, mod_fibs) * calc_mod_fib(n - 1, mod_fibs) +
            calc_mod_fib(n - 2, mod_fibs);
        mod_fibs.push(x.clone());
        x
    }
}
