fn fib(n: u32) -> u64 {
    let (mut a, mut b) = (0u64, 1u64);
    for _ in 0..n {
        (a, b) = (b, a + b);
    }
    a
}

fn main() {
    println!("Salam, Rust!");
    for i in 0..10 {
        println!("fib({}) = {}", i, fib(i));
    }
}
