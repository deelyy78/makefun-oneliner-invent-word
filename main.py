# griefscroll — a make.fun program/v1 entry.
# Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output
# outside this repo). Python 3.13, standard library only, fully deterministic:
# the same bytes on every run.
import os

LINE = "griefscroll (n.): rereading old messages from someone who has died, scrolling slowly, as if the thread might still light up."


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out)


if __name__ == "__main__":
    main()
