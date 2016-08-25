#![feature(inclusive_range_syntax)]
extern crate num;

#[macro_use]
mod utils;

mod euler;
mod hackerrank;

fn main() {
    //euler::circular_primes_35::circularprimes();
    //hackerrank::modfib::modified_fib();
    //hackerrank::cut_the_tree::cut_the_tree();
    //euler::longest_collatz_14::longest_collatz();
    //hackerrank::connected_cell_in_grid::connected_cell_in_grid();
    hackerrank::the_grid_search::grid_search();
}


