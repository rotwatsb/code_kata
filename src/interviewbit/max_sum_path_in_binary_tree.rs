use std::cmp::max;
use std::i32;
use utils;

pub fn max_sum() {
    let vals: Vec<i32> = utils::read_vec();
    let cnxs: Vec<Vec<usize>> = utils::read_tree_edges(vals.len());
    let mut max_sum: i32 = i32::MIN;

    let _ = max_path(0, 0, &vals, &cnxs, &mut max_sum);
    println!("{}", max_sum);
}

fn max_path(
    i: usize,
    par: usize,
    vals: &Vec<i32>,
    cnxs: &Vec<Vec<usize>>,
    max_sum: &mut i32,
) -> i32 {
    let mut subsums = Vec::new();

    for node in cnxs[i].clone() {
        if node != par {
            subsums.push(max_path(node, i, vals, cnxs, max_sum));
        }
    }

    let mut best_subsum = if subsums.is_empty() { 0 } else { i32::MIN };
    let mut sum_of_sums = 0;
    for sum in subsums {
        sum_of_sums += sum;
        if sum > best_subsum {
            best_subsum = sum;
        }
    }
    *max_sum = max(*max_sum, sum_of_sums + vals[i]);
    max(best_subsum + vals[i], vals[i])
}
