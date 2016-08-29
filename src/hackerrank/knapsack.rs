// https://www.hackerrank.com/contests/bits-goa-day-3/challenges/knapsack-problem

use utils::{read_usize_pair};

use std::cmp;

pub fn knapsack() {
    let (s, n) = read_usize_pair();
    let mut sizes: Vec<usize> = Vec::with_capacity(n);
    let mut values: Vec<usize> = Vec::with_capacity(n);
    for i in 0..n {
        let (size, value) = read_usize_pair();
        sizes.push(size);
        values.push(value);
    }
    let mut memoized: Vec<Vec<Option<usize>>> = vec![vec![None; 2001]; n];
    let max_val = max_knapsack(s, n - 1, &sizes, &values, &mut memoized);
    println!("{}", max_val);
}

fn max_knapsack(c: usize, n: usize, sizes: &Vec<usize>, values: &Vec<usize>,
                memoized: &mut Vec<Vec<Option<usize>>>) -> usize {
    if let Some(v) = memoized[n][c] {
        return v;
    }
    
    let max_val =
        (if sizes[n] > c {
            if n == 0 { return 0; }
            max_knapsack(c, n - 1, sizes, values, memoized)
         }
         else {
             if n == 0 { return values[0]; }
             cmp::max(values[n] + max_knapsack(c - sizes[n], n - 1, sizes, values, memoized),
                      max_knapsack(c, n - 1, sizes, values, memoized))
         });
    memoized[n][c] = Some(max_val);
    max_val
}
    

