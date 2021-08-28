// https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

use utils;
use std::cmp;

pub fn min() {
    let v: Vec<i32> = utils::read_vec();

    let mut sorted = v.clone();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());

    let min_swaps: i32 =
        v.iter().enumerate().fold(
            0,
            |swaps, (i, &x)| if sorted[i] != x { swaps + 1 } else { swaps },
        );

    println!("{:?}", cmp::max(0, min_swaps - 1));
}
