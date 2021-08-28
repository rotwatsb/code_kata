use std::io;
use std::str::FromStr;

/*
macro_rules! read_vec {
    ($func_name:ident, $type:ty) => {
        pub fn $func_name() -> Vec<$type> {
            let mut line = String::new();
            io::stdin().read_line(&mut line).unwrap();
            line.split(' ')
                .map(|slice| slice.trim().parse::<$type>().unwrap())
                .collect::<Vec<$type>>()
        }
    };
}
*/

pub fn read_int() -> i32 {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: i32 = line.trim().parse().unwrap();
    n
}

pub fn read_string() -> String {
    let mut line = String::new();
    if let Ok(_) = io::stdin().read_line(&mut line) {
        line
    } else {
        line
    }
}

pub fn read_one<T: FromStr>() -> Result<T, <T as FromStr>::Err> {
    read_string().trim().parse::<T>()
}

pub fn read_vec<T: FromStr>() -> Vec<T> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();

    line.split(' ')
        .filter_map(|slice| slice.trim().parse::<T>().ok())
        .collect()
}

pub fn read_int_pair() -> (i32, i32) {
    let vals: Vec<i32> = read_vec();
    (vals[0], vals[1])
}

pub fn read_usize_pair() -> (usize, usize) {
    let vals: Vec<i32> = read_vec();
    (vals[0] as usize, vals[1] as usize)
}

pub fn read_tree_edges(nodes: usize) -> Vec<Vec<usize>> {
    let mut tree: Vec<Vec<usize>> = vec![vec![]; nodes as usize];
    for _ in 1..nodes {
        let (a, b): (i32, i32) = read_int_pair();
        tree[a as usize - 1].push(b as usize - 1);
        tree[b as usize - 1].push(a as usize - 1);
    }
    tree
}

pub fn read_matrix<T: FromStr>(rows: usize) -> Vec<Vec<T>> {
    let mut m: Vec<Vec<T>> = Vec::with_capacity(rows);

    for _ in 0..rows {
        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();

        let row: Vec<T> = line
            .split(' ')
            .filter_map(|slice| slice.trim().parse::<T>().ok())
            .collect();

        m.push(row);
    }
    m
}

pub fn word_freqs(s: &str) -> [i32; 26] {
    s.chars().fold([0; 26], |mut freqs, c| {
        freqs[c.to_ascii_lowercase() as usize - 'a' as usize] += 1;
        freqs
    })
}
