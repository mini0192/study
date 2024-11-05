# DispatcherServlet

![img](https://jaegukim.github.io/assets/img/post/Spring/SpringMVC.png)

DispatcherServlet은 HTTP 프로토콜로 들어오는 모든 요청을 받아 적합한 컨트롤러에 위임하는 역할을 한다.
클라이언트로부터의 요청은 Tomcat과 같은 서블릿 컨테이너가 수신하고,
이 요청을 DispatcherServlet이 처리하여 적절한 컨트롤러에 전달한다.

#### Despatch
발송하다 파견, 발송

#### Servlet
Java 기반 서버 측 컴포넌트로 웹 어플리케이션에서 클라이언트의 요청을 처리하고 그에 대한 응답을 생성하는데 사용됨

---

### HTTP 프로토콜 지원
Servlet은 HTTP 요청을 처리하기 위해 설계되었으며, 클라이언트와의 상호작용을 관리

### 서버 측 실행
Servlet은 서버에서 실행되며, 클라이언트의 요청을 받아 처리한 후 응답을 클라이언트에 반환한다.

### 확장성
Servlet은 클래스의 형태로 작성되며, Java의 객체 지향 특성을 활용하여 재사용성과 확장성을 제공한다.

### 요청 및 응답 객체
Servlet은 HttpServletRequest와 HttpServletResponse 객체를 사용하여 요청 정보를 수신하고 응답을 생성한다.
이를 통해 쿼리 파라미터, 세션 데이터, 쿠키 등을 관리 할 수 있다.
 

## Spring MVC에서 DispatcherServlet의 작동 방식

1. 요청 수신
Tomcat과 같은 서블릿 컨테이너가 클라이언트로 부터 요청을 수신하게 되면, 요청은 DispatcherServlet으로 전달된다.
이는 모든 HTTP 요청의 진입점이 된다.

2. 핸들러 매핑
DispatcherServlet은 요청 URL을 분석하여 해당 요청을 처리할 적합한 컨트롤러를 찾기 위해 Handler Mapping을 사용한다.

3. 핸들러 호출
매핑된 컨르롤러가 호출 되어 비지니스 로직을 실행하고, 결과를 모델과 뷰 정보로 반환한다.

4. 뷰 리졸빙
반환된 뷰 이름을 바탕으로 View Resolver를 통해 실제 뷰 객체를 찾아 랜더링 한다.

5. 응답 반환
최종적으로 생성된 응답을 클라이언트에세 반환한다.

## REST API에서 DispatcherServlet의 작동 방식

1. 요청 수신
Tomcat과 같은 서블릿 컨테이너가 클라이언트로 부터 요청을 수신하게 되면, 요청은 DispatcherServlet으로 전달된다.
이는 모든 HTTP 요청의 진입점이 된다.

2. 핸들러 매핑
DispatcherServlet은 요청 URL을 분석하여 해당 요청을 처리할 적합한 컨트롤러를 찾기 위해 Handler Mapping을 사용한다.

3. 핸들러 호출
매핑된 컨르롤러가 호출 되어 비지니스 로직을 실행하고, 결과를 모델과 뷰 정보로 반환한다.

4. 응답 생성
처리 결과를 JSON, XML 등으로 직렬화 하여 클라이언트에세 반환할 응답 객체를 생성

5. 응답 반환
최종적으로 생성된 응답을 클라이언트에게 반환한다.