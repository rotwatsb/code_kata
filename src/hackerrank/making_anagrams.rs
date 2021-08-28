// https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

use std::io;
use utils;

pub fn min_deletions() {
    let mut s1: String = String::new();
    let mut s2: String = String::new();

    io::stdin().read_line(&mut s1).unwrap();
    io::stdin().read_line(&mut s2).unwrap();

    let freqs1: [i32; 26] = utils::word_freqs(&s1.trim());
    let freqs2: [i32; 26] = utils::word_freqs(&s2.trim());

    let min: i32 = freqs1.iter().enumerate().fold(0, |diffs, (i, n)| diffs + (n - freqs2[i]).abs());

    println!("{:?}", min);
}
