# JVM이란?
Java Virtual Machine의 줄임말로 자바를 실행하기 위한 가상의 컴퓨터 이다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F0kg24%2Fbtq4YOOQH4J%2FEF2ISOpkYA36a1flwtLEmK%2Fimg.png)

Java 소스코드, 즉 원시코드(.java)는 CPU가 인식을 할 수 없기 때문에 이를 기계어로 컴파일해야 한다.
하지만 Java는 JVM이라는 가상머신을 거쳐 OS에 도달하기 때문에
OS가 이해할 수 있는 기계어로 바로 컴파일 되지 않고, JVM이 이해할 수 있는 Java Bytecode(.class)로 변환하고
Java Bytecode를 JVM이 실행하게 된다.
여기서 Java 소스코드를 Java Bytecode로 변환하는 일을 Java compiler가 수행하게 된다.

> #### 왜 Java는 바로 OS가 이해할 수 있는 기계어가 아닌 Java Bytecode로 변환하여 실행을 하는 걸까?
> Java의 주요 목표중 하나는 플렛폼 독립성이다.
> Java로 작성된 프로그램은 특정 운영체제나 하드웨어에 의존하지 않고 어디서든 실행이 가능해야 해야 한다.
> 이를 위해 Java는 소스 코드를 먼저 Java Bytecode라는 중간 코드로 컴파일한다.
> Java Bytecode는 운영체제나 하드웨어와 독립적이며, JVM이 이를 실행하게 된다.
> JVM은 각 운영체제에 맞게 구현되어 있어 같은 Java Bytecode를 다양한 플렛폼에서 실행할 수 있게 해준다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtclVx%2Fbtq4Xfml6Dy%2Fnzb5xxlGG1fr5iBGUMv77K%2Fimg.png)

JVM은 Class Loader, 실행 엔진, Runtime Data 영역으로 이루어져 있다.


## Class Loader
Class Loader는 Java Class 파일을 메모리에 동적으로 로드하고 링크하여 프로그램을 실행할 수 있게 하는 역할을 수행한다.

이는 총 세가지 단계로 실행되며
로딩, 링크, 초기화 순으로 진행된다.

### 로딩
Class가 JVM에 의해 처음 사용되면, Java는 Class를 메모리에 로드한다. 이때 Class 파일이 물리적으로 메모리에 로드되며, 이 과정에서 Class 객체를 생성한다.

### 링크
로드된 Class는 링크 과정을 거친다.
링크는 다시 검증, 준비, 해석 3단계로 세분화 된다.

1. 검증: 로드된 Class 파일의 유효성을 검사한다. 여기서 Class 파일이 정상적인 형식과 유효한 Bytecode를 가지는지 확인한다. 만약 이상이 있다면 VerifyError가 발생한다.
2. 준비: Class의 정적 변수가 메모리에 할당되며 기본값으로 초기화 한다.
3. 해석: Class 파일 내에서 참조된 다른 Class나 Method 등을 실제 메모리 주소로 변환한다.

### 초기화
정적 변수들이 초기화 되며, 정적 초기화 블록이 실행된다.

> ### 링크의 준비 단계에서 정적 변수를 메모리에 할당하고 기본값으로 초기화를 했는데 왜 초기화 단계에서 또 정적 변수를 초기화 할까?
> 링크의 준비 단계에서는 단순히 메모리 공간을 예약하는 단계이기 때문에 실제 사용자가 정의한 값이 설정되지 않고 기본값으로 설정된다.
> 반면 초기화 단계에서는 실제로 사용자가 정의한 값이 할당된다.


## 실행 엔진
Class를 실행하는 역할을 수행한다.
Class Loader가 JVM내에 Runtime data 영역에 배치시키고 이는 실행 엔진에 의해 실행된다.


JVM은 기본적으로 인터프리터 방식으로 실행된다. 즉 Bytecode를 한 줄씩 일어 실행된다.
그리고 적절한 시점에 JIT 컴파일러가 Bytecode 전체를 컴파일 하여 실행한다.
이렇게 컴파일된 기계어는 캐시에 보관하게 된다.

> ### 적절한 시점이 뭘까?
> JVM은 실행되는 동안 Hot Spot(반복적으로 호출되는 메서드나 빈번하게 실행되는 코드 조각을 의미)을 찾는다. 즉 반복적으로 호출 되거나 성능상 중요한 메서드를 찾고 이러한 메서드는 JIT 컴파일의 대상이 된다.

### Garbage Collection(GC)
GC는 Java에서 자동 메모리 관리를 위해 사용되는 메커니즘이다.
Java는 객체를 생성하고 사용이 끝나면 자동으로 회수하여 메모리 누수를 방지한다.
여기서 GC는 메모리를 회수하는 역할을 하고 JVM은 이 과정을 자동으로 수행한다.

#### GC의 실행 시점
1. 메모리가 부족할 때: JVM은 일정량의 Heap 메모리를 할당 받는다 하지만 이 Heap 공간이 가득 차게 되면 GC를 실행하여 더 이상 참조되지 않은 객체를 제거한다.
2. 주기적으로: JVM은 메모리 사용 상황에 따라 주기적으로 GC를 수행한다.


## Runtime Data 영역
Runtime Data 영역은 Stack, Method Area, Heap, Native method stack, PC Register로 이루어져 있다.

### Stack
메서드의 실행과 관련된 데이터를 관리하는 메모리 공간으로 주로 지역 변수를 저장한다.
메서드 호출 시마다 새로운 Stack 프레임이 생성되고, 메서드 실행이 완료되면 Stack 프레임을 제거한다.

### Method Area
Class에 대한 정보를 저장하는 영역이다. JVM에 의해 Java Class 파일이 로드되면 이 Class의 메타데이터(Class 정보와 관련된 데이터)와 정적 변수가 Method Area에 저장된다.

### Heap
JVM에서 동적 메모리 할당을 담당하는 메모리 영역이다.
Java에서 인스턴스와 배열 등 동적으로 생성되는 데이터는 Heap 영역에 저장된다.
기본적으로 Heap 영역은 JVM이 실행되는 동안 가변적이며, GC에 의해 관리되는 공간이다.

#### Young 영역
새롭게 생성된 객체가 할당되는 영역
대부분의 객체가 금방 Unreachable 상태가 되기 때문에 많은 객체가 Young 영역에 생성되었다가 사라진다.
Young 영역에 대한 GC를 Minor GC라고 한다.

Young 영역은 추가적으로 Eden, Survivor 0, Survivor 1 3가지 영역으로 나뉜다.
1. Eden: new를 통히 새로 생성된 객체가 위치한다. 정기적으로 GC가 실행되고 살아남은 객체들은 Survivor 영역으로 보낸다.
2. Survivor 0 / Survivor 1: 최소 1번의 GC가 실행되고 살아남은 객체가 존재하는 영역이다. 두개의 Survivor이 번갈아가며 사용되며, GC를 통해 살아남은 객체는 Old 영역으로 보낸다.

> ### 왜 Survivor 영역 중 하나는 비어있어야 한다. 왜 그럴까?
> Young 영역에서 GC가 발생 할 때 Eden 공간에 있는 객체중 살아 남은 객체는 Survivor 영역으로 복사되는데 이 과정에서 기존에 있던 객체들을 덮어쓰지 않기 위해서 Survivor 영역을 번갈아서 사용한다.
> 예를 들어 Eden 공간에 있는 객체들을 Survivor 0으로 이동 시키고 그 다음 GC가 발생하면 Eden 공간과 Survivor 0에서 살아남은 객체를 Survivor 1로 복사하는 방식으로 진행한다. 
> 이를 통해 효율적인 메모리 사용과 성능을 최적화 시킬수 있다. 
