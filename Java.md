# Java

## Day 1

* console 창 : alt + shift + Q, C / Window 클릭 > show view 에 있음
* 단축키
  * ctrl + shift + f : 들여쓰기 정렬
  * alt + 방향키 : 드래그 하거나 커서 있는 코드 움직이기
  * alt + ctrl + 방향키 : 드래그 하거나 커서 있는 코드 복사
  * ctrl + shift + o : 자동 import !!!!!!!!! **중요**
  * art + shift + s : getter & setter 창 띄우는 것
* print 출력

```java
public class intro01_Hello {
    // 아래 코드는 main 치고 ctrl + spacebar 누르고 탭하면 자동완성 됨
	public static void main(String[] args) {
        // sysou + ctrl + spacebar
		System.out.println("Hello SSAFY!!!");
	}
}
```

### Java 주석

* // 내용
* /* 내용 */
* /** API를 위한 주석 */



### 출력문(java intro03_PrintTest에 자세히 정리함)

* print : 한줄 출력
* println : 한번 출력하고 줄을 바꿔줌
* printf : 출력하고 포맷을 준다
  * %d : 정수(10진수)
  * %o : 정수(8진수)
  * %x or %X : 정수(16진수 소문자, 대문자)
  * %f : 실수
  * %s : 문자열
  * %c : 문자 1개



### 변수

##### 합성어

* PascalCase : 클래스 이름
* camelCase : 변수명, 함수
* snake_case : python에서 씀 / 자바에선 상수를 대문자_대문자
* kebab-case : HTML / CSS 등 속성



### 자료형

* 정수형 - int : 4byte
* 실수형 - double : 8byte



### 변수와 자료형

* 선언
* 저장(할당)
* 초기화



### 형변환 > 자료형은 물건보관소 / 데이터는 물품

##### 데이터 형변환

* 묵시적(암묵적)
  * 범위가 넓은 데이터 형에 족은 데이터 형을 대입하는 것
* 명시적
  * 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것



### 연산자

* 최우선 연산자
* 단항 연산자
* 산술 연산자
* 비교 연산자
* 논리 연산자
* 삼항 연산자
* 대입 연산자



##### 단항 연산자

* 증감연산자
  * 피연산자의 값을 1증가, 감소 시킨다.
  * 전위형 : ++i
    * 먼저 하고 연산
  * 후위형 : i--
    * 연산 후에 처리

* 부위 연산자 +, -
  * 숫자가 양수임을 표시 : +
  * 피연산자의 부호를 반대로 변경한 결과 반환 : -  (빼는 것이 아님)
* 논리 부정 연산자 : !
  * 논리 값을 반전
* 비트 부정 연산자 : ~  (물결)
  * 비트 값을 반전
* 형 변환 연산자(type)
* 산술 연산자 (python과 같음)
  * 곱하기
  * 나누기
  * 나머지
  * 더하기
  * 빼기

* 비교 연산자 (python과 같음)
  + 대소 비교 연산 
    + 다른것
    + 50 <= a < 60 이걸 사용 못함
    + 50 <= a && a < 60 이렇게 사용
  + 동등 비교 연산
    + 다른것
    + == : String변수 비교 불가능 / 똑같다라고 나올 수 있기 때문
    + String에는 equals()를 사용해야함

* 논리 연산자
  * &&
    * 논리 곱(AND) : 피연산자 모두가 true일 경우에만 true
  * ||
    * 논리 합(OR) : 피연산자 중 하나라도 true일 경우 true
  * !
    * 논리 부정(NOT) : 피연산자의 결과를 반대로 바꾼다.

* 삼항 연산자
  * 조건식? 식1:식2
  * 조건식이 참일 경우 식1 수행
  * 조건식이 거짓일 경우 식2 수행

* 복합 대입 연산자
  * += 등등



### 조건문

* if
  * 조건식의 결과에 따라 블록 실행 여부가 결정
  * java04.Control에 정리
* switch



### 반복문

* for

  * ```java
    for(초기화식; 조건식; 증감식;) {
        반복 수행할 문장
    }
    // 무한루프를 돌리려면 조건식을 비워두면된다.
    ```

* while

  * ```java
    while(조건식){
        반복 수행할 문장
    }
    ```

* do while

  * ```java
    do{
        반복 수행할 문장;
    } while(조건식);
    ```



### 배열

* 한번 생성된 배열은 크기를 바꿀 수 없음
* 배열을 객체로 취급
* 배열의 요솔르 참조하려면 배열이름과 색인(index)라고 하는 int 유형의 정수 값을 조합하여 사용



* 배열의 선언

| 타입    | 배열이름 | 선언            | 초기화    |
| ------- | -------- | --------------- | --------- |
| int     | iArr     | int[] iArr;     | 0         |
| char    | cArr     | char[] cArr;    | \0000공백 |
| bollean | bArr     | boolean[] bArr; | false     |
| Srting  | strArr   | String strArr;  | null      |
| Date    | dateArr  | Date dateArr;   | null      |

* new로 초기화

* 배열 이름.length를 통해 배열의 길이 조회 가능(python len()대신 사용)
* 길이 변경 필요시 새로운 배열을 생성 후 내용을 옮긴다.
  * 배열 선언 : int[] points;
  * 배열 생성 : new int[3];
  * 참조값 할당 : points = new int[3];
  * int[] tmp = new int[5];
  * points = tmp;

* ```java
  System.out.println(Arrays.toString(리스트 이름)); // 배열 전체를 보여줌
  ```



* 배열의 복사
* System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length)
* src : 원본배열
* srcPos: 원본배역 복사 시작 위치
* dest : 복사할 배열
* destPos : 복사 받을 시작 위치
* length : 복사할 크기



### 다차원 배열

* 2차원 배열 : 1차원 배열들의 배열
  * 1차원 배열들의 길이가 모두 같을 필요는 없다!!



###### 1일차 종료

---

## Day 2

### 객체지향 프로그래밍(OOP : Object Oriented Programming)

* 객체 : 사물과 같이 유형적인 것과 개념이나 논리와 같은 무형적인 것들
* 지향 : 작정하거나 지정한 방향으로 나아감
* 객체 모델링 : 현실세계의 객체를 SW 객체로 설계하는 것

* 정의 : 현실 세계의 모든 것은 객체로 이루어져 있고 사건과 현상은 객체간의 상호작용으로 이루어져 있다.

### 특징 (A PIE)

* 추상화 : Abstraction
* 다형성 : Ploymorphism
* 상속 : Inheritance
* 캡슐화 : Encapsulation



### Class

* 크기를 모름
* static이 있어야함 - python 전역변수처럼 사용 가능
* 클래스 == 객체를 생성하는 틀
* 클래스는 객체를 만들기 위한 설계도, 인스턴스는 설계도로 만든 객체
* 클래스 안에 클래스는 **이너 클래스**라고 부름
* 구성
  * 속성 - 필드
  * 동작 - 메소드
  * 생성자 - 인스턴스를 생성할 때 호출 메소드

* 클래스 선언

  * ```java
    [접근제한자][활용제한자] class 클래스명 {
        속성 정의(필드);
        기능 정의(메소드);
        생성자
    }
    ```

  * 접근제한자

    * public / default 등

  * 활용제한자

    * final / abstract 등



### 함수(Function)

* 반복되는 친구에게 이름을 준다.

* ```java
  public static void move(String area, String BMW) {
      System.out.println(area+"(으)로" + BMW + "(을)를 이용하여 이동한다.");
  }
  ```

  

### 변수

* 클래스 변수

  * 클래스 영역 선언(static 키워드)

  * 생성 시기 : 클래스가 메모리에 올라 갔을 때

  * 모든 인스턴스가 공유함

  * ```java
    class Person {
        // 클래스 영역
        // 값 초기화 자동 진행 x : 초기화 하면 int이기 때문에 0
        static int person count;	// 소멸 시기 : 프로그램 종료시
    }
    ```

* 인스턴스 변수
  * 클래스 영역 선언
  * 생성시기 : 인스턴스가 생성되었을 때(new)
  * 인스턴스 별로 생성됨
  * 초기화 자동으로 진행됨
* 지역 변수
  * 클래스 영역 이외(메서드, 생성자, 블록 등..)
  * 사용하기 전 초기화가 꼭 필요!
  * 생성시기 : 선언되었을 때



### 메서드

```java
[접근제한자][활용제한자] 반환값 메소드 이름 ([매개변수들]) {
    행위 기술;
}
```

* 매개변수 생략 가능
* 파라미터 전달 시 묵시적 형 변환
* 리턴 타입은 하나만 적용가능
  * 여러개 보내려면 리스트로



### 클래스와 객체 정리

* 클래스
  * 관련있는 변수와 함수를 묶어 만든 사용자 정의 자료형
* 객체
  * 하나의 역할을 수행하는 '메소드와 변수(데이터)'의 묶음
* 객체지향 프로그래밍
  * 프로그램을 단순히 데이터와 처리 방법으로 나누는 것이 아니라, 프로그램을 수많은 ''객체''라는 기본 단위로 나누고 이들의 상호작용으로 서술하는 방식



### JVM 메모리 구조

* java언어는 메모리 관리를 개발자가 하지 않음
* GC(Garbage Collection)가 메모리 관리를 해줌



* 클래스 영역(메소드 영역) - 클래스의 정보를 저장하는 영역
* 힙(Heap) - 인스턴스가 생성되는 공간
* 스택(Stack)
  * 메서드 수행시 프레임이 할당됨
  * 필요한 변수나, 중간 결과 값을 임시 기억하는 곳
  * 메소드 종료 시 할당 메모리 자동제거

```java
// Person은 같은 패키지 않에 다른 곳에 만들어져 있음

Person p1 = new Person();
// Person을 사용하기 전에 클래스 영역에 Person 설계도가 올라옴
// new를 사용하면 스택에 p1이라는 공간이 할당됨
// new 힙에 주소가 생기고 p1공간이 힙 p1주소를 가리킴

p1.name = "Yang";
// 문자열 상속에 "Yang"이 생기고 p1 name이 "Yang"을 가리킴

p1.age = 45;
// int 상속에 45가 생기고 p1 age이 45를 가리킴

p1.hobby = "Youtube";
// 문자열 상속에 "Youtube"이 생기고 p1 hobby가 "Youtube"을 가리킴
```



### Static 특징

* static : 클래스 이름으로 접근 

  * ex) Person.pCount++;  << 오류는 나지만 경고이며 사용 가능

* non-static : 객체 생성 후 접근

  * ```java
    Person p = new Person();
    p.name = "Kim";
    ```

* static 영역에서는 non-static 영역을 직접 접근이 불가능

* non-static 영역에서는 static 영역에 대한 접근이 가능



### 생성자

* 인스턴스가 생성될 때 최초 한번 수행되는 함수
  * new 키워드와 함께 호출
  * 클래스를 생성할 때 반드시 하나의 생성자 호출 - 생성자가 여러개일 수 있음
  * 성공적으로 실행되면 힙 영역에 객체 생성 후 객체의 번지가 리턴
  * 필드의 초기화, 객체 생성 시 실행되어야 한 작업 작성
  * 클래스 이름이 PascalCase로 작성하는 것이 관례이며 생성자는 클래스 이름과 동일해야함

* 기본(디폴트) 생성자
  * 클래스 내에 생성자가 하나도 정의되어 있지 않을 경우 JVM이 자동으로 제공하는 생성자
  * 형태 : 매개변수가 없는 형태, 클래스 명() {}
* 파라미터가 있는 생성자
  * 생성자의 목적이 필드 초기화
  * 생성자 호출 시 값을 넘겨주어야 함
  * 해당 생성자를 작성하면 JVM이 기본 생성자를 추가하지 않음

* 생성자 오버로딩을 지원한다.
  * 클래스 내에 메소드 이름이 같고 매개변수의 타입 또는 개수가 다른 것이 오류가 나지 않게 해줌
* this
  * 참조 변수로써 객체 자신을 가리킴
  * this를 이용하여 자신의 멤버 접근 가능
  * static영역에서는 this를 사용하지 못함
  * this([인자값]) : 생성자 호출
  * 생성자 내에서만 호출 가능
  * 생성자 내에서 첫번째 위치에 존재해야함



### 패키지(오후-1)

* PC의 파일을 관리하기 위해 폴더를 사용
* 프로그램의 많은 클래스를 관리하기 위해 패키지를 이용한다.
* 패키지의 구분은 .(dot) 연산자를 이용한다.
* 회사도메인을 반대로 사용하는게 관례
  * com.ssafy.프로젝트 이름.~ 로 사용



### 임포트(import)

* 다른 패키지에 있는 클래스를 사용하기 위해서는 import 해야 사용가능
  * import com.ssafy.class01.className;
  * 위와 같이 클래스의 이름만 쓰던지
  * import com.ssafy.class01.*;
  * 패키지의 모든 클래스를 포함할 때는 '*'를 사용
  * ctrl + shift + o : 자동 임포트



### 캡슐화

* public -> private

* 셀제 구현 내용 일부를 감추거나 숨김
* 줄건 주고 숨길건 숨김



### 접근 제한자

* 접근 제한자의 종류 - 아래로 갈수록 접근의 파워(접근 가능 범위가 작은 것)가 강해짐
  * public : 모든 위치에서 접근이 가능
  * protected : 같은 패키지에서 접근이 가능, 다른 패키지 접근 불가능, 단, 다른 패키지의 클래스와 상속관계가 있을 경우 접근 가능
  * (default) : 같은 패키지에서만 접근이 허용, 접근제한자가 선언이 안되었을 경우 기본 적용
  * private : 자신 클래스에서만 접근이 허용
* 클래스(외부) 사용가능 : public, default
* 내부 클래스, 멤버변수(필드), 메소드 사용가능 : 4가지 모두 사용가능
* 그 외 제한자
  * static : 클래스 레벨의 요소 설정
  * final : 요소를 더 이상 수정할 수 없게 함
  * abstract : 추상 메서드 및 추상 클래스 작성

| 수식어    | 클래스 내부 | 동일 패키지 | (다른 패키지내의)하위 클래스 | 다른 클래스 |
| --------- | ----------- | ----------- | ---------------------------- | ----------- |
| private   | O           | X           | X                            | X           |
| (default) | O           | O           | X                            | X           |
| protected | O           | O           | O                            | X           |
| public    | O           | O           | O                            | O           |



### 접근 제어자

* Day2
  * modifier01
    * Car, CarTest



* getter & setter를 만드는 이유는 static을 사용하면 클래스외에서 사용하지 못하기 때문에 호출할 수 있도록 만들어 주는 것

* getter & setter를 만들어주는 것
  * 오른 쪽 마우스 클릭
  * Source
  * Generate Getters and Setters... 클릭

* 전체 생성자
  * 오른 쪽 마우스 클릭
  * Source
  * 위 두개 단축키 : alt + shift + s
  * Generate Constructor using Fields...



* static = 전역변수(메모리에 먼저 올려놓기 때문에)



### 상속 - com.ssafy.Inheritance01

* 상위 클래스 / 부모 클래스 / superclass
* 하위 클래스 / 자식 클래스 / subclass



1. 확장성, 재 사용성
   * 부모의 생성자와 초기화 블록은 상속 x
2. 클래스 선언시 extends 키워드를 명시
   * 자바는 다중 상속 허용 x, 단일 상속 지원
3. 관계
   * 부모클래스 : Person
   * 자식 클래스 : Student
4. 자식 클래스는 부모 클래스의 멤버변수, 메소드를 자신의 것처럼 사용할 수 있다.
   * 접근 제한자에 따라 사용 여부가 달라진다.
5. Object 클래스는 모든 클래스의 조상 클래스
   * 별도의 extends 선언이 없는 클래스는 extends Object가 생략



7.  오버라이딩(재정의, overriding)

   * @override : 해당 메서드는 재작성 되었다! 라고 알려주는 것
     * 썼을 때의 장점은?
     * 조금더 안전한 프로그램을 작성할 수 있다.
     * 부모와 다른것을 알려주고 고치는 방법 2가지 제시
   * @~~ : Annotation
   * 컴파일러가 보는 주석

   * 부모가 private(감추기) 접근제한자를 쓰면 자식은 public(오픈) 할 수 있지만
   * 부모가 public(오픈) 을 사용했을 때 자식은 private로 못 감춘다.



##### 오버로딩과 오버라이딩의 차이!!

* 오버로딩 : 부모와 자식의 메서드의 이름은 같고 매개변수(메서드 괄호 안에 들어가는 것들) 가 다른 것들
* 오버라이딩 : 부모와 자식의 모든게 일치해야한다.



### Object 클래스

* 가장 최상위 클래스로 모든 클래스의 조상
* Object의 멤버는 모든 클래스의 멤버



##### final

* 해당 선언이 최종 상태, 결코 수정 될 수 없음
* final 클래스 : 상속 금지
* final 메소드 : overriding 금지
* final 변수 : 더 이상 값을 바꿀 수 없음, 상수화





## Day 3

### 다형성

https://edu.ssafy.com/edu/board/free/detail.do?&brdItmSeq=45903




