use std::env;
use std::fs;
use std::process;

fn main() {
    // İstifadə: cargo run -- [fayl_yolu]   (standart: README.md)
    let path = env::args().nth(1).unwrap_or_else(|| "README.md".to_string());

    let content = match fs::read_to_string(&path) {
        Ok(text) => text,
        Err(err) => {
            eprintln!("Xəta: '{}' oxunmadı: {}", path, err);
            process::exit(1);
        }
    };

    println!("=== {} ({} sətir) ===", path, content.lines().count());
    for (i, line) in content.lines().enumerate() {
        println!("{:>4} | {}", i + 1, line);
    }
}
