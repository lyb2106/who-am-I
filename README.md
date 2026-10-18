# who-am-I

이윤범의 디지털 명함 저장소.

| 항목 | 경로 | 공개 URL |
|---|---|---|
| 랜딩(명함) | `index.html` | https://lyb2106.github.io/who-am-I/ |
| CV | `cv/index.html` | https://lyb2106.github.io/who-am-I/cv/ |
| CV QR 코드 | `assets/qr/cv-qr.svg`, `assets/qr/cv-qr.png` | https://lyb2106.github.io/who-am-I/assets/qr/cv-qr.png |

## 구조

```
index.html          # 랜딩 페이지 (CV 링크 + QR)
cv/index.html       # CV 본문 (단일 HTML)
assets/qr/          # CV 링크 QR 코드 (SVG: 인쇄용, PNG: 디지털용)
scripts/make_qr.py  # QR 재생성 스크립트
.nojekyll           # GitHub Pages의 Jekyll 처리 비활성화
```

## CV 갱신

`cv/index.html` 을 새 버전으로 교체하고 push 하면 된다. 공개 URL이 고정되어 있으므로 **QR 코드는 다시 만들 필요가 없다.**

## QR 재생성 (URL이 바뀐 경우에만)

```bash
pip install segno
python scripts/make_qr.py                      # 기본 URL
python scripts/make_qr.py https://example.com  # 다른 URL
```

오류 정정 레벨 H(최대 약 30% 손상 복원)로 생성한다.

## 배포 (GitHub Pages)

Settings → Pages → Build and deployment → Source: **Deploy from a branch** → 배포 브랜치 / `/(root)` 선택.
공개 저장소이므로 별도 권한 없이 URL만으로 누구나 열람할 수 있다.
