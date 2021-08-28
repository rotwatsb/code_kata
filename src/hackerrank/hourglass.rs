// https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

use std::cmp;
use std::collections::HashMap;
use utils;

pub fn sum() {
    let matrix_size: usize = 6;
    let m: Vec<Vec<i32>> = utils::read_matrix(matrix_size);
    let mut span_sums: HashMap<(usize, usize), i32> = HashMap::new();

    let mut span_sum = |r: usize, c: usize| {
        if let Some(&sum) = span_sums.get(&(r, c)) {
            sum
        } else {
            let sum = m[r][c - 1..c + 2].iter().sum();
            span_sums.insert((r, c), sum);
            sum
        }
    };

    let max: i32 =
        m[1..matrix_size - 1]
            .iter()
            .enumerate()
            .fold(i32::MIN, |outer_max, (ri, col)| {
                cmp::max(
                    outer_max,
                    col[1..matrix_size - 1].iter().enumerate().fold(
                        outer_max,
                        |inner_max, (ci, v)| {
                            cmp::max(
                                inner_max,
                                v + span_sum(ri, ci + 1) + span_sum(ri + 2, ci + 1),
                            )
                        },
                    ),
                )
            });

    println!("{:?}", max);
}
