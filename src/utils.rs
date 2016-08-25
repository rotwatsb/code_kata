use std::io;

macro_rules! read_num_vec {
    ($func_name:ident, $num_type:ty) => (
        fn $func_name() -> Vec<$num_type> {
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
