// https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

use std::cmp;
use std::collections::HashMap;
use std::hash;
use std::io;

pub fn is_valid() {
    let mut s1: String = String::new();

    io::stdin().read_line(&mut s1).unwrap();

    let word_freqs: HashMap<u8, i32> = freqs(&s1.trim().bytes().collect());
    let freq_freqs: HashMap<i32, i32> = freqs(&word_freqs.clone().into_values().collect());

    let (mode, _): (i32, i32) =
        freq_freqs.iter().fold(
            (0, 0),
            |(mode, freq), (&k, &v)| if v >= freq { (k, v) } else { (mode, freq) },
        );

    let mut free_pass: bool = true;
    let is_valid: bool = word_freqs.into_values().fold(true, |is_valid, v| {
        if v == mode {
            is_valid
        } else if (v - mode).abs() == 1 && free_pass {
            free_pass = false;
            is_valid
        } else {
            false
        }
    });

    if is_valid {
        println!("YES")
    } else {
        println!("NO")
    }
}

fn freqs<T: cmp::Eq + hash::Hash + Copy>(s: &Vec<T>) -> HashMap<T, i32> {
    s.iter().fold(HashMap::new(), |mut freqs, &k| {
        *(freqs.entry(k).or_insert(0)) += 1;
        freqs
    })
}
