use std::io;

pub fn grid_search() {
    let mut t_str: String = String::new();
    io::stdin().read_line(&mut t_str);
    
    for t in 0u32..t_str.trim().parse().unwrap() {
        let g: Vec<String> = read_matrix();
        let p: Vec<String> = read_matrix();

        if contains(&g, &p) { println!("YES"); } else { println!("NO"); }
    }
}

fn contains(g: &Vec<String>, p: &Vec<String>) -> bool {
    let cols = p[0].len();
    for r in 0..g.len() - p.len() + 1 {
        for c in 0..g[r].len() - cols + 1{
            if match_at(&g, &p, r, c) {
                return true;
            }
        }
    }
    false
}

fn match_at(g: &Vec<String>, p: &Vec<String>, r: usize, c: usize) -> bool {
    for i in 0..p.len() {
        let gs = &g[r + i][c..c + p[i].len()];
        let ps = &p[i][..];

        if gs != ps {
            return false;
        }
    }
    true
}



fn read_matrix() -> Vec<String> {

    let mut grgc_str: String = String::new();
    
    
    io::stdin().read_line(&mut grgc_str);
    let mut iter = grgc_str.split(' ');

    let r: usize = iter.next().unwrap().trim().parse().unwrap();
    let c: usize = iter.next().unwrap().trim().parse().unwrap();

    let mut g: Vec<String> = Vec::with_capacity(r);

    for i in 0..r {
        let mut row: String = String::with_capacity(c);
        io::stdin().read_line(&mut row);
        g.push(row.trim().to_string());
    }
    g
}


