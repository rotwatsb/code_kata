use std::collections::HashMap;

const UPPER_BOUND: usize = 1000000;

pub fn longest_collatz() {
    let mut stored_vals: HashMap<usize, usize> = HashMap::new();
    let mut max: usize = 0;
    let mut best: usize = 0;

    for i in 0..UPPER_BOUND {
        let cur = cmp_collatz(i, &mut stored_vals);
        if cur > max {
            best = i;
            max = cur;
        }
    }
    println!("map len: {:?}", stored_vals.len());
    println!("best: {:?}\nmax: {:?}", best, max);
}

fn cmp_collatz(n: usize, stored_vals: &mut HashMap<usize, usize>) -> usize {
    if n <= 1 {
        return 1;
    }
    if let Some(&val) = stored_vals.get(&n) {
        return val;
    } else {
        let chain_len = if n % 2 == 0 {
            1 + cmp_collatz(n / 2, stored_vals)
        } else {
            1 + cmp_collatz(3 * n + 1, stored_vals)
        };
        stored_vals.insert(n, chain_len);
        chain_len
    }
}
