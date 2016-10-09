use std::io;
use std::u32;

use utils;

pub fn cut_the_tree() {

    let n: usize = utils::read_int() as usize;
    let vals: Vec<i32> = utils::read_ints();
    let mut tree = utils::read_tree_edges(n);
    let mut subsums: Vec<i32> = vec![0; tree.len()];
    ctf_calc_subsums(0, 0, &mut tree, &vals, &mut subsums);
    
    let mut min_diff: u32 = u32::MAX;
    ctf_calc_diffs(0, 0, &mut tree, &vals, &subsums, &mut min_diff);
    println!("{:?}", min_diff);
}

fn ctf_calc_diffs(par: usize, cur: usize, tree: &mut Vec<Vec<usize>>,
                  vals: &Vec<i32>, subsums: &Vec<i32>, min_diff: &mut u32) {
    for child in tree[cur].clone() {
        if child != par {
            let diff = (subsums[0] - 2 * subsums[child]).abs() as u32;
            if diff < *min_diff {
                *min_diff = diff;
            }
            ctf_calc_diffs(cur, child, tree, vals, subsums, min_diff);
        }
    }
}

fn ctf_calc_subsums(par: usize, cur: usize, tree: &mut Vec<Vec<usize>>, vals: &Vec<i32>,
                    subsums: &mut Vec<i32>) {
    let mut subsum: i32 = 0;
    for node in tree[cur].clone() {
        if node != par {
            ctf_calc_subsums(cur, node, tree, vals, subsums);
            subsum += subsums[node];
        }
    }
    subsums[cur] = subsum + vals[cur];
}




