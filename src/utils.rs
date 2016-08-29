use std::io;

macro_rules! read_num_vec {
    ($func_name:ident, $num_type:ty) => (
        pub fn $func_name() -> Vec<$num_type> {
            let mut line = String::new();
            io::stdin().read_line(&mut line);
            line.split(' ')
                .map(|slice| slice.trim().parse::<$num_type>().unwrap())
                .collect::<Vec<$num_type>>()
        }
    )
}

pub fn read_int() -> i32 {
    let mut line = String::new();
    io::stdin().read_line(&mut line);
    let n: i32 = line.trim().parse().unwrap();
    n
}

read_num_vec!(read_ints, i32);

pub fn read_int_pair() -> (i32, i32) {
    let vals: Vec<i32> = read_ints();
    (vals[0], vals[1])
}

pub fn read_usize_pair() -> (usize, usize) {
    let vals: Vec<i32> = read_ints();
    (vals[0] as usize, vals[1] as usize)
}

pub fn read_tree_edges(nodes: usize) -> Vec<Vec<usize>> {
    let mut tree: Vec<Vec<usize>>
        = vec![vec![]; nodes as usize];
    for i in 1 .. nodes {
        let (a, b): (i32, i32) = read_int_pair();
        tree[a as usize - 1].push(b as usize - 1);
        tree[b as usize - 1].push(a as usize - 1);
    }
    tree
}

pub fn read_matrix_u32() -> Vec<Vec<u32>> {

    let mut r_str: String = String::new();
    let mut c_str: String = String::new();
    
    
    io::stdin().read_line(&mut r_str);
    io::stdin().read_line(&mut c_str);

    let r: usize = r_str.trim().parse().unwrap();
    let c: usize = c_str.trim().parse().unwrap();

    let mut g: Vec<Vec<u32>> = Vec::with_capacity(r);

    for i in 0..r {
        let mut v: Vec<u32> = Vec::new();
        let mut row: String = String::new();
        io::stdin().read_line(&mut row);
        let mut wsi = row.split_whitespace();
        for j in 0..c {
            v.push(wsi.next().unwrap().parse().unwrap());
        }
        g.push(v.clone());
    }
    g
}
