#!/usr/bin/env python3
"""공개 CV 링크의 QR 코드를 생성한다 (SVG + PNG).

사용법:
    pip install segno
    python scripts/make_qr.py [URL]
"""
import sys
from pathlib import Path

import segno

DEFAULT_URL = "https://lyb2106.github.io/who-am-I/cv/"
OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "qr"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    # 오류 정정 레벨 H(~30% 복원): 인쇄물 훼손·로고 삽입에 대비
    qr = segno.make(url, error="h", micro=False)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    qr.save(OUT_DIR / "cv-qr.svg", scale=10, border=4)
    qr.save(OUT_DIR / "cv-qr.png", scale=20, border=4)
    print(f"QR generated for {url} -> {OUT_DIR} (version {qr.version}, error {qr.error})")


if __name__ == "__main__":
    main()
