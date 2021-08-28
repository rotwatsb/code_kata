// https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

use std::io;
use utils;

pub fn count() {
    let _: i32 = utils::read_int();
    let mut path = String::new();
    io::stdin().read_line(&mut path).unwrap();

    let mut elevation: i32 = 0;

    let valleys: i32 = path.as_bytes().iter().fold(0, |acc, &step| {
        if step == b'D' {
            elevation -= 1;

            acc
        } else {
            elevation += 1;

            if elevation == 0 {
                acc + 1
            } else {
                acc
            }
        }
    });

    println!("{:?}", valleys);
}
