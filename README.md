# Algorithm-LvUpStudy

## Commit Convention 📌

(리드미 수정예정)

`예시) add: 문제이름`

- add: 풀이추가
- del: 잘못올린 파일 삭제
- fix: 문제수정 및 문서수정
- test: 깃허브 충돌 발생 시 테스트커밋

### 방식

- 주어진 문제를 풀어 각자의 이름으로 브랜치를 생성하고 폴더에 작성하여 push한다.
- 폴더 명은 문제명으로 하되 띄어쓰기는 -으로 대체한다.
- main branch로 PR을 날리고 리뷰어를 등록한다.
- 모두 문제를 풀었는지 확인 후 main branch로 merge한다.
- 다음 문제를 풀기전에 꼭! pull하여 main branch와의 싱크를 맞춰준다.

```
git add .
git branch
git commit -m 'add: 이름'
git push origin 개인브랜치이름

// 커밋하기 전에 확인하기 (레포 파일 싱크 맞추기)
git pull origin main

// 브랜치 생성하기
git clone address .
git remote -v
git checkout -t origin/개인브랜치
git branch
```
