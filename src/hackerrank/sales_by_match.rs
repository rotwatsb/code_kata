// https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

use std::collections::HashMap;
use utils;

pub fn sock_merchant() {
    let _: i32 = utils::read_int();
    let ar: Vec<i32> = utils::read_vec();
    let mut mem: HashMap<i32, bool> = HashMap::new();

    let result: i32 = ar.iter().fold(0, |acc, color| {
        if let Some(_) = mem.get(color) {
            mem.remove(color);
            acc + 1
        } else {
            mem.insert(*color, true);
            acc
        }
    });

    println!("{:?}", result);
}
