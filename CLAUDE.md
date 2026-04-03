# Dotfiles

개인 설정 파일 관리 레포. `setup.sh`로 심링크 기반 설치.

## 구조
- `config/` - 홈 디렉토리에 심링크될 설정 파일들 (`.`가 prefix로 붙음)
- `config/claude/` - Claude Code 설정 (`~/.claude/`로 심링크)
- `3rd/` - 서브모듈 (antigen, pwndbg 등)
- `bin/` - 실행 파일
- `setup.sh` - 심링크 설치 스크립트
- `install.sh` - 시스템 패키지 설치 스크립트

## 규칙
- 한국어로 대화
- 민감 정보 (API 키, credentials) 절대 커밋하지 않기
