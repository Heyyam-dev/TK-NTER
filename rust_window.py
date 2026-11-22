import tkinter as tk

BG_DARK = "#1a1a2e"
BG_PANEL = "#16213e"
BG_CARD = "#0f3460"
RUST_ORANGE = "#e94560"
RUST_AMBER = "#f5a623"
RUST_GOLD = "#ffd700"
TEXT_PRIMARY = "#e0e0e0"
TEXT_MUTED = "#8892a4"
ACCENT_GREEN = "#4ecca3"
BORDER = "#2a2a4a"


def create_header(parent):
    header = tk.Frame(parent, bg=BG_PANEL, height=60)
    header.pack(fill=tk.X, side=tk.TOP)
    header.pack_propagate(False)

    title_frame = tk.Frame(header, bg=BG_PANEL)
    title_frame.pack(side=tk.LEFT, padx=20, pady=10)

    rust_label = tk.Label(
        title_frame,
        text="🦀 Rust",
        fg=RUST_ORANGE,
        bg=BG_PANEL,
        font=("Consolas", 18, "bold"),
    )
    rust_label.pack(side=tk.LEFT)

    sub_label = tk.Label(
        title_frame,
        text=" — Memory Safe, Blazingly Fast",
        fg=TEXT_MUTED,
        bg=BG_PANEL,
        font=("Consolas", 11),
    )
    sub_label.pack(side=tk.LEFT)

    version_label = tk.Label(
        header,
        text="v1.75.0",
        fg=ACCENT_GREEN,
        bg=BG_PANEL,
        font=("Consolas", 10),
    )
    version_label.pack(side=tk.RIGHT, padx=20)

    separator = tk.Frame(parent, bg=RUST_ORANGE, height=2)
    separator.pack(fill=tk.X)


def create_code_editor(parent):
    frame = tk.Frame(parent, bg=BG_DARK, padx=15, pady=10)
    frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(10, 5), pady=10)

    tk.Label(
        frame,
        text="main.rs",
        fg=RUST_AMBER,
        bg=BG_DARK,
        font=("Consolas", 11, "bold"),
    ).pack(anchor=tk.W, pady=(0, 5))

    editor_frame = tk.Frame(frame, bg=BG_CARD, bd=1, relief=tk.FLAT)
    editor_frame.pack(fill=tk.BOTH, expand=True)

    line_frame = tk.Frame(editor_frame, bg=BG_PANEL, width=40)
    line_frame.pack(side=tk.LEFT, fill=tk.Y)
    line_frame.pack_propagate(False)

    code_text = tk.Text(
        editor_frame,
        bg=BG_CARD,
        fg=TEXT_PRIMARY,
        font=("Consolas", 11),
        insertbackground=RUST_ORANGE,
        selectbackground=BG_PANEL,
        selectforeground=RUST_GOLD,
        relief=tk.FLAT,
        padx=10,
        pady=8,
        wrap=tk.NONE,
    )
    code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(editor_frame, bg=BG_PANEL, troughcolor=BG_DARK)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    code_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=code_text.yview)

    sample_code = """\
use std::collections::HashMap;

fn fibonacci(n: u64) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}

struct MemoryManager {
    allocations: HashMap<String, Vec<u8>>,
}

impl MemoryManager {
    fn new() -> Self {
        MemoryManager {
            allocations: HashMap::new(),
        }
    }

    fn allocate(&mut self, key: &str, size: usize) {
        let buffer = vec![0u8; size];
        self.allocations.insert(key.to_string(), buffer);
        println!("Allocated {} bytes for '{}'", size, key);
    }

    fn free(&mut self, key: &str) -> Option<Vec<u8>> {
        self.allocations.remove(key)
    }
}

fn main() {
    let mut mgr = MemoryManager::new();
    mgr.allocate("buffer_a", 1024);
    mgr.allocate("buffer_b", 2048);

    println!("Fibonacci(10) = {}", fibonacci(10));

    if let Some(buf) = mgr.free("buffer_a") {
        println!("Freed {} bytes", buf.len());
    }
}
"""
    code_text.insert(tk.END, sample_code)

    _apply_syntax_highlighting(code_text)

    lines = sample_code.count("\n") + 1
    line_numbers = "\n".join(str(i) for i in range(1, lines + 1))
    line_num_text = tk.Text(
        line_frame,
        bg=BG_PANEL,
        fg=TEXT_MUTED,
        font=("Consolas", 11),
        relief=tk.FLAT,
        padx=5,
        pady=8,
        state=tk.DISABLED,
        width=4,
    )
    line_num_text.pack(fill=tk.BOTH, expand=True)
    line_num_text.config(state=tk.NORMAL)
    line_num_text.insert(tk.END, line_numbers)
    line_num_text.config(state=tk.DISABLED)

    return code_text


def _apply_syntax_highlighting(text_widget):
    text_widget.tag_configure("keyword", foreground=RUST_ORANGE)
    text_widget.tag_configure("type_kw", foreground="#569cd6")
    text_widget.tag_configure("string", foreground=ACCENT_GREEN)
    text_widget.tag_configure("comment", foreground=TEXT_MUTED)
    text_widget.tag_configure("number", foreground=RUST_AMBER)
    text_widget.tag_configure("function", foreground=RUST_GOLD)

    keywords = ["fn", "let", "mut", "match", "use", "struct", "impl",
                 "pub", "if", "else", "return", "for", "in", "while",
                 "loop", "break", "continue", "mod", "crate", "self"]
    types = ["u8", "u64", "usize", "i32", "String", "Vec", "HashMap",
             "Option", "Result", "Self", "bool", "Some", "None"]

    content = text_widget.get("1.0", tk.END)
    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        if "//" in line:
            col = line.index("//")
            text_widget.tag_add("comment", f"{line_num}.{col}", f"{line_num}.end")

        for kw in keywords:
            idx = 0
            while True:
                pos = line.find(kw, idx)
                if pos == -1:
                    break
                before = line[pos - 1] if pos > 0 else " "
                after = line[pos + len(kw)] if pos + len(kw) < len(line) else " "
                if not before.isalnum() and before != "_" and not after.isalnum() and after != "_":
                    text_widget.tag_add("keyword", f"{line_num}.{pos}", f"{line_num}.{pos + len(kw)}")
                idx = pos + 1

        for tp in types:
            idx = 0
            while True:
                pos = line.find(tp, idx)
                if pos == -1:
                    break
                before = line[pos - 1] if pos > 0 else " "
                after = line[pos + len(tp)] if pos + len(tp) < len(line) else " "
                if not before.isalnum() and before != "_" and not after.isalnum() and after != "_":
                    text_widget.tag_add("type_kw", f"{line_num}.{pos}", f"{line_num}.{pos + len(tp)}")
                idx = pos + 1


def create_sidebar(parent):
    sidebar = tk.Frame(parent, bg=BG_PANEL, width=220)
    sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 10), pady=10)
    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="Compiler Output",
        fg=RUST_AMBER,
        bg=BG_PANEL,
        font=("Consolas", 11, "bold"),
    ).pack(anchor=tk.W, padx=10, pady=(10, 5))

    output_frame = tk.Frame(sidebar, bg=BG_CARD)
    output_frame.pack(fill=tk.X, padx=8, pady=4)

    messages = [
        ("✓", "Compiling project v0.1.0", ACCENT_GREEN),
        ("✓", "Finished dev target", ACCENT_GREEN),
        ("⚠", "warning: unused variable `x`", RUST_AMBER),
        ("✓", "Running `./target/debug/app`", TEXT_PRIMARY),
    ]

    for icon, msg, color in messages:
        row = tk.Frame(output_frame, bg=BG_CARD)
        row.pack(fill=tk.X, padx=5, pady=2)
        tk.Label(row, text=icon, fg=color, bg=BG_CARD, font=("Consolas", 10)).pack(side=tk.LEFT)
        tk.Label(
            row, text=msg, fg=color, bg=BG_CARD,
            font=("Consolas", 9), wraplength=170, justify=tk.LEFT,
        ).pack(side=tk.LEFT, padx=4)

    tk.Label(
        sidebar,
        text="Memory Stats",
        fg=RUST_AMBER,
        bg=BG_PANEL,
        font=("Consolas", 11, "bold"),
    ).pack(anchor=tk.W, padx=10, pady=(15, 5))

    stats = [
        ("Stack", "24 KB", RUST_ORANGE),
        ("Heap", "3.1 MB", "#569cd6"),
        ("Ownership", "Safe ✓", ACCENT_GREEN),
        ("Lifetimes", "Checked ✓", ACCENT_GREEN),
    ]

    for label, value, color in stats:
        stat_frame = tk.Frame(sidebar, bg=BG_CARD)
        stat_frame.pack(fill=tk.X, padx=8, pady=2)
        tk.Label(stat_frame, text=label, fg=TEXT_MUTED, bg=BG_CARD,
                 font=("Consolas", 10), width=12, anchor=tk.W).pack(side=tk.LEFT, padx=5)
        tk.Label(stat_frame, text=value, fg=color, bg=BG_CARD,
                 font=("Consolas", 10, "bold")).pack(side=tk.RIGHT, padx=5)

    tk.Label(
        sidebar,
        text="Actions",
        fg=RUST_AMBER,
        bg=BG_PANEL,
        font=("Consolas", 11, "bold"),
    ).pack(anchor=tk.W, padx=10, pady=(15, 5))

    buttons = [
        ("▶  cargo run", RUST_ORANGE),
        ("🔧  cargo build", "#569cd6"),
        ("🧪  cargo test", ACCENT_GREEN),
        ("📦  cargo check", RUST_AMBER),
    ]

    for text, color in buttons:
        btn = tk.Button(
            sidebar,
            text=text,
            fg=color,
            bg=BG_CARD,
            activebackground=BG_DARK,
            activeforeground=color,
            font=("Consolas", 10),
            relief=tk.FLAT,
            bd=0,
            padx=10,
            pady=5,
            cursor="hand2",
        )
        btn.pack(fill=tk.X, padx=8, pady=2)


def create_statusbar(parent):
    bar = tk.Frame(parent, bg=RUST_ORANGE, height=24)
    bar.pack(fill=tk.X, side=tk.BOTTOM)
    bar.pack_propagate(False)

    items = [
        ("🦀 Rust 1.75.0", BG_DARK),
        ("  UTF-8", BG_DARK),
        ("  Ln 1, Col 1", BG_DARK),
        ("  main.rs", BG_DARK),
    ]

    for text, fg in items:
        tk.Label(bar, text=text, fg=fg, bg=RUST_ORANGE,
                 font=("Consolas", 9, "bold")).pack(side=tk.LEFT, padx=8)

    tk.Label(bar, text="Memory Safe ✓", fg=BG_DARK, bg=RUST_ORANGE,
             font=("Consolas", 9, "bold")).pack(side=tk.RIGHT, padx=12)


def main():
    root = tk.Tk()
    root.title("🦀 Rust IDE — rust_window.py")
    root.geometry("980x650")
    root.minsize(800, 500)
    root.configure(bg=BG_DARK)

    try:
        root.tk.call("tk", "scaling", 1.2)
    except tk.TclError:
        pass

    create_header(root)
    create_statusbar(root)

    content = tk.Frame(root, bg=BG_DARK)
    content.pack(fill=tk.BOTH, expand=True)

    create_code_editor(content)
    create_sidebar(content)

    root.mainloop()


if __name__ == "__main__":
    main()
