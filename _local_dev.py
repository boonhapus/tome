import contextlib
import subprocess as sp
import shlex


def main() -> int:
    """Tiny cli."""

    with contextlib.suppress(KeyboardInterrupt):
        cp = sp.run(shlex.split("pnpm run build"))
        cp = sp.run(shlex.split("litestar --app 'src.api.main:app' run"))

    return cp.returncode


if __name__ == "__main__":
    raise SystemExit(main())
