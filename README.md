# 빌더스게이트 AX 상품 소개 페이지

**보기: https://bluuhans.github.io/bg-ax-page/** (외부 공유 시에는 `?share`를 붙이면 편집 버튼이 숨겨진다)

빌더스게이트의 AX(AI 전환) 상품을 소개하는 원페이지. 단일 HTML 파일로 GitHub Pages에서 서빙한다.

## 수정 방법

페이지에서 직접 고치는 것이 기본이다.

1. 페이지 우하단 **편집** 버튼 클릭 → 본문을 직접 수정
2. **저장** 클릭 → 암구호 입력 → 5분 이내에 자동으로 이 저장소에 커밋·반영된다

저장이 반영되지 않으면 [Actions 탭](https://github.com/bluuhans/bg-ax-page/actions)에서 `apply-edit` 실행 로그를 확인한다.

## 파일 구성

| 파일 | 역할 |
|---|---|
| `index.html` | 페이지 전체 (마크업·스타일·스크립트 단일 파일) |
| `img/` | 페이지에서 쓰는 사진 8장 |
| `apply_edit.py` | 웹 편집 저장분을 `<main>`에 반영하는 스크립트 (안전 점검 포함) |
| `.github/workflows/apply-edit.yml` | 5분마다 저장 응답을 확인해 위 스크립트를 실행 |
| `.last-sync` | 마지막으로 반영한 저장 시각 기록 |

## 관리 주의사항

- **원본은 사내 Drive** (`Buildersgate/manager_han/BuildersGate_AX/05_상품설계/index.html`). 이 저장소에 직접 커밋했다면 Drive 원본에도 반영할 것. 반대로 Drive에서 고쳐 푸시하기 전에는 반드시 `git pull` — 웹 저장 커밋이 먼저 들어와 있을 수 있다.
- 웹 편집 저장은 구글 폼 → 응답 시트 → Actions 경로로 들어온다. 암구호와 시트 주소는 저장소 Secrets(`EDIT_PASSPHRASE`, `SHEET_CSV_URL`)로 관리한다.
