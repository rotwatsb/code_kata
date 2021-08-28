use std::collections::HashMap;
use utils;

pub fn solve() {
    if let Ok(n) = utils::read_one::<usize>() {
        for _ in 0..n {
            calc_pairs(utils::read_string().trim());
        }
    }
}

fn calc_pairs(s: &str) {
    let mut freqs = HashMap::new();
    for i in 0..s.len() {
        for j in i..s.len() {
            *(freqs.entry(utils::word_freqs(&s[i..j + 1])).or_insert(0)) += 1;
        }
    }

    let pairs: i32 = freqs
        .into_values()
        .filter(|&x| x > 1)
        .map(|x| x * (x - 1) / 2)
        //.filter_map(|x| if x > 1 { Some(x * (x - 1) / 2) } else { None })
        .sum();

    println!("{:?}", pairs);
}

/*def solve_sa(s):
    freqs = collections.defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            freqs[''.join(sorted(s[i:j+1]))] += 1
    print(sum(v * (v-1) // 2 for v in freqs.values()))
*/
