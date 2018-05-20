도커 이미지 빌드

```
쉘> docker build -t cholsoo22001/orly .
```

테스트 실행

```
쉘> docker run \
    --env AZURE_ACCOUNT_NAME="" \
    --env AZURE_ACCOUNT_KEY="" \
    -p 8080:8080 \
    cholsoo22001/orly
```

Docker Hub에 이미지 배포

```
쉘> docker push cholsoo22001/orly
```
