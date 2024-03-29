use utils;

pub fn connected_cell_in_grid() {
    let m: Vec<Vec<u32>> = utils::read_matrix(10);
    let mut max_path: u32 = 0;

    for i in 0..m.len() {
        for j in 0..m[0].len() {
            if m[i][j] != 0 {
                let l = explore(&mut m.clone(), i as isize, j as isize);
                if l > max_path {
                    max_path = l;
                }
            }
        }
    }
    println!("{}", max_path);
    //println!("{:?}", m);
}

fn explore(m: &mut Vec<Vec<u32>>, r: isize, c: isize) -> u32 {
    
    if r < 0 || r >= m.len() as isize || c < 0 || c >= m[0].len() as isize {
        return 0;
    }

    let mut sum = 0;
    
    if m[r as usize][c as usize] == 1 {
        m[r as usize][c as usize] = 0;
        sum = 1 +
            explore(m, r - 1, c) +
            explore(m, r - 1, c - 1) +
            explore(m, r + 1, c) +
            explore(m, r + 1, c + 1) +
            explore(m, r, c - 1) +
            explore(m, r + 1, c - 1) +
            explore(m, r, c + 1) +
            explore(m, r - 1, c + 1);
    }
    sum
}


