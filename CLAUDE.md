# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 개발 명령어

### 테스트
- 모든 테스트 실행: `pytest`
- 특정 테스트 파일 실행: `pytest tests/test_common_re.py`
- 상세 출력으로 실행: `pytest -v`

### 애플리케이션 실행
- 메인 모듈 실행: `python main.py`
- 로거 유틸리티 데모 실행: `python logger/logger_util.py`

### 패키지 관리
- 의존성 설치: `uv sync` (uv.lock 사용)
- 새 의존성 추가: `uv add <package>`

## 아키텍처 개요

두 개의 주요 컴포넌트를 가진 Python 유틸리티 라이브러리입니다:

### 로거 모듈 (`logger/`)
중앙화된 로깅 설정을 제공합니다:
- ANSI 이스케이프 코드를 사용한 컬러 콘솔 출력
- 로테이션 기능이 있는 파일 로깅 (10MB 파일, 5개 백업)
- 두 핸들러를 모두 설정하는 전역 설정 함수
- 기본 로그 위치: `logs/app.log`

### 정규식 헬퍼 모듈 (`rehelper/`)
공통 정규식 패턴을 열거형으로 포함:
- `CommonRe` 열거형에 미리 정의된 패턴들 (EMAIL, PHONE_NUMBER)
- 각 패턴은 `.value` 속성으로 접근 가능
- 한국 전화번호 형식 지원

### 프로젝트 구조
- Python >=3.13 요구사항과 함께 `pyproject.toml`을 설정에 사용
- pytest 프레임워크를 사용하는 `tests/` 디렉토리의 테스트들
- `logs/` 디렉토리에 자동으로 생성되는 로그