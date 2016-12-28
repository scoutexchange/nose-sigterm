# nose-sigterm

Nose plugin to raise KeyboardInterrupt on SIGTERM.

Nose abruptly terminates on SIGTERM but handles KeyboardInterrupt (SIGINT)
gracefully, by printing failed test and coverage output up to the point of
termination.

There are cases when a SIGINT cannot be sent to nose, such as when running
as a child background process from the shell.

---

## Installation and Setup

`pip install nose-sigterm`

---

### Usage

Add `--with-sigterm` to the nosetest CLI options.
