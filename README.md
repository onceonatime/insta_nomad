# Nomadgram

> ##### [ 강의 출처 ] ["Django 풀스택 : 인스타그램 클론 코딩”](https://academy.nomadcoders.co/courses/enrolled/216935) by [NOMAD CODERS](https://academy.nomadcoders.co/)

----

## 공부 목표

#### 1. 심플한 Rest API 구성 방법 재습득

> 2017.10 ~ 2018.12 현재 재직중 런칭한 서비스는 Django, Jquery, Ajax 로 구성 되어 있어 Django Template 를 이용하여 구현함

> 과거 공부 했던 Rest API에 대한 기억을 상기 시킬 필요가 있음.

#### 2. 실제 서비스 런칭 하면서 아쉬웠던 점, 미흡했던 점 보완

> 확장, 이전이 쉬운 DB Model APP 구조설계 / 관리 등에 대한 아쉬움이 큼

> ( 이럴줄 알았으면 이렇게 하지 말아야 했는데 ) => 핑계 : 온전히 혼자 런칭해본 서비스가 처음..ㅋㅋ => 다시 이런 실수는 하면 안됨

> 기본 셋팅 및 Django App 구조가 강의와 다르지만 최대한 런칭하면서 아쉬웠던 점을 다시 공부하면서 바로 잡아보기 위함.



## 강의 내용과 다른 구성

#### 1. 쿠키커터 사용하지 않음

> 프로덕트에서는 불필요한 라이브러리 최소화하여 **가능한한** 심플하게 구성해야 하며, ( 장고 기본 만으로도 라이브러리가 가득함 )

> Django 및 라이브러리를 직접 설정하며 본인이 사용한 라이브러리에 대한 이해를 위함

#### 2. 별도 앱 ( db app ) 으로 데이터 베이스 모델링 관리

> 실 서비스 런칭시 그 전에 배워왔던 대로 앱 단위로 분할하여, view, model 을 같이 구성하였는데,

> 버전업 혹은 서비스 확장시 DB Model만 옮길 수 있다면 간단하겠지만, 새 프로젝트에 app 구조 까지 동일하게 구성해야 하는 단점이 있음

> DB Model 만을 관리하는 app을 만들어 해당 app만 이관하면 데이터베이스 모델을 그대로 사용 할 수 있게 하기 위함



## 강의 완강 후 변경 해야 할 점

#### 1. DB : AWS RDS 이용

#### 2. Static 파일 관리 : AWS S3 이용

#### 3. 각종 보안 설정 키 값 분할 => 공부가 아닌 프로덕트 개발시 라면 가장 먼저 해야 하는 부분

> 개인적으로 좋아하는 Project Structure

```
project_folder/
        .conf_secret/
                settings_common.json
                settings_debug.json
                settings_deploy.json
        .django_app/
        ...
        ...
```

또는

```
project_folder/
        .django_app/
                .conf_secret/
                        settings_common.json
                        settings_debug.json
                        settings_deploy.json
        ...
        ...
```

- settings_common.json
 : 기본공통 설정 정보 관리 ( ex: Django Secret Key.. )

- settings_debug.json
 : 로컬 개발용 설정 정보 관리

- settings_deploy.json
 : 서버 배포용 설정 정보 관리

**[ 중요 ] : 프로덕트 프로젝트의 경우 대부분 Private 저장소겠지만, 위 settings 파일들의 경우 Private 저장소가 아닐 경우 git에 포함 하면 안됨!!!**

#### 4. 현재 수강중인 패캠 DebOps 강의에서 배운 클라우드 서비스 서버 아키텍쳐에 따라 AWS 에서 제시하는 프랙티스에 맞게 배포 해보기.